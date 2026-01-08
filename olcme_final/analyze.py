import re
import sys
from pypdf import PdfReader
from collections import Counter

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def parse_questions(text):
    lines = text.split('\n')
    questions = []
    current_q = None
    state = "START" # START, QUESTION, OPTION
    
    # Regex patterns
    # Matches "1. ", "2. ", "105. "
    q_start_pattern = re.compile(r'^\s*(\d+)\.\s+(.*)') 
    # Matches "A) ", "  B) "
    opt_start_pattern = re.compile(r'^\s*([A-E])\)\s+(.*)')
    # Matches "DOGRU CEVAP: C" or "DOĞRU CEVAP: E"
    answer_pattern = re.compile(r'^\s*DO?GRU CEVAP:\s*([A-E])', re.IGNORECASE)
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for Answer first (it ends a question block)
        ans_match = answer_pattern.match(line)
        if ans_match:
            if current_q:
                current_q['answer_letter'] = ans_match.group(1).upper()
                # Validate and Save
                if len(current_q['options']) >= 2 and current_q['answer_letter']:
                    questions.append(current_q)
                current_q = None
            state = "START"
            continue
            
        # Check for Option
        opt_match = opt_start_pattern.match(line)
        if opt_match:
            if current_q:
                letter = opt_match.group(1).upper()
                content = opt_match.group(2).strip()
                current_q['options'][letter] = content
                state = "OPTION"
            continue
            
        # Check for Question Start
        q_match = q_start_pattern.match(line)
        if q_match:
            # If we were building a question but didn't find an answer, discard it (or maybe it was a header looking like a question)
            # But be careful, sometimes headers like "1. Konu" might appear. 
            # We'll assume if we hit a new number, the previous one is done or broken.
            # However, looking at the sample, "1. Konu" appeared before "1. Aktif..."
            # Let's decide based on whether we are already in a question with options.
            # If we are in a question and haven't seen an answer, checking a new number is risky if the previous one wasn't a real question.
            
            # Let's clean up previous if "broken"
            current_q = {
                'number': q_match.group(1),
                'text': q_match.group(2).strip(),
                'options': {},
                'answer_letter': None
            }
            state = "QUESTION"
            continue
            
        # Append text to current state
        if state == "QUESTION" and current_q:
            current_q['text'] += " " + line
        elif state == "OPTION" and current_q:
            # Format: find the last added option and append
            # Since options are a dict, we need to know the last key. 
            # Dictionaries preserve insertion order in Python 3.7+
            if current_q['options']:
                last_key = list(current_q['options'].keys())[-1]
                current_q['options'][last_key] += " " + line

    return questions

def analyze_questions(questions):
    longest_correct_count = 0
    short_correct_list = []
    
    for q in questions:
        ans_letter = q['answer_letter']
        if ans_letter not in q['options']:
            # Something is wrong, maybe parsing error or typo in PDF
            continue
            
        correct_text = q['options'][ans_letter]
        correct_len = len(correct_text)
        
        # Check if strictly longest
        is_strictly_longest = True
        for letter, text in q['options'].items():
            if letter == ans_letter:
                continue
            if len(text) >= correct_len:
                is_strictly_longest = False
                break
        
        if is_strictly_longest:
            longest_correct_count += 1
        else:
            short_correct_list.append(q)
            
    return longest_correct_count, short_correct_list

def calculate_distribution(questions):
    letters = [q['answer_letter'] for q in questions]
    return Counter(letters)

def generate_latex(questions, distribution, total_count, longest_count, short_count, filename="short_answers.tex"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[turkish]{babel}
\usepackage{geometry}
\geometry{a4paper, margin=1in}
\usepackage{titlesec}
\usepackage{booktabs}
\usepackage{multicol}

\title{Kısa Cevaplı ve Eşit Uzunlukta Cevaplı Sorular Analizi}
\author{Analysis}
\date{\today}

\begin{document}
\maketitle

\section*{Genel İstatistikler}
\begin{itemize}
    \item \textbf{Toplam Soru Sayısı:} """ + str(total_count) + r"""
    \item \textbf{En Uzun Şıkkın Doğru Olduğu Soru Sayısı:} """ + str(longest_count) + r"""
    \item \textbf{Uzun Şık Doğruluk Oranı:} \%""" + f"{longest_count/total_count*100:.2f}" + r"""
    \item \textbf{En Uzun Olmayan (veya Eşit) Şıkkın Doğru Olduğu Soru Sayısı:} """ + str(short_count) + r"""
\end{itemize}

\section*{Kısa/Eşit Cevapların Şık Dağılımı}
Bu rapordaki sorular (toplam \textbf{""" + str(short_count) + r"""}), doğru cevabın diğer şıklardan kesin olarak daha uzun \textit{olmadığı} sorulardır.

\begin{center}
\begin{tabular}{ccc}
\toprule
\textbf{Şık} & \textbf{Soru Sayısı} & \textbf{Yüzde (\%)} \\
\midrule
""")
        
        for char in sorted(distribution.keys()):
            count = distribution[char]
            percentage = (count / short_count) * 100
            f.write(f"{char} & {count} & \%{percentage:.2f} \\\\\n")
            
        f.write(r"""\bottomrule
\end{tabular}
\end{center}

""")
        
        for q in questions:
            f.write(f"\\section*{{Soru {q['number']}}}\n")
            # Escape LaTeX special chars
            q_text = escape_latex(q['text'])
            f.write(f"{q_text}\n\n")
            
            f.write(r"\begin{itemize}" + "\n")
            for letter, text in q['options'].items():
                esc_text = escape_latex(text)
                if letter == q['answer_letter']:
                    f.write(f"  \\item[\\textbf{{{letter}}})] \\textbf{{{esc_text}}} (Doğru Cevap)\n")
                else:
                    f.write(f"  \\item[{letter})] {esc_text}\n")
            f.write(r"\end{itemize}" + "\n\n")

        # Add Summary Section at the end
        f.write(r"\newpage" + "\n")
        f.write(r"\section*{Özet Cevap Anahtarı}" + "\n")
        f.write(r"\begin{multicols}{2}" + "\n")
        f.write(r"\begin{itemize}" + "\n")
        for q in questions:
            ans_letter = q['answer_letter']
            qs_text = q['options'][ans_letter]
            esc_ans = escape_latex(qs_text)
            esc_q = escape_latex(q['text'])
            f.write(f"  \\item \\textbf{{{q['number']}.}} {esc_q} \\\\ \\textbf{{({ans_letter})}} {esc_ans}\n")
        f.write(r"\end{itemize}" + "\n")
        f.write(r"\end{multicols}" + "\n")
            
        f.write(r"\end{document}")

def escape_latex(text):
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
    }
    return "".join(replacements.get(c, c) for c in text)

def main():
    input_pdf = "final.pdf"
    if len(sys.argv) > 1:
        input_pdf = sys.argv[1]

    print(f"Extracting text from {input_pdf}...")
    try:
        text = extract_text(input_pdf)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        sys.exit(1)
    
    print("Parsing questions...")
    questions = parse_questions(text)
    print(f"Total questions found: {len(questions)}")
    
    print("Analyzing...")
    longest_count, short_list = analyze_questions(questions)
    
    total = len(questions)
    short_count = len(short_list)
    
    print("-" * 30)
    print("ISTATISTIKLER")
    print("-" * 30)
    print(f"Toplam Soru: {total}")
    print(f"En Uzun Şıkkın Doğru Olduğu Soru Sayısı: {longest_count}")
    print(f"En Uzun Olmayan (veya Eşit) Şıkkın Doğru Olduğu Soru Sayısı: {short_count}")
    if total > 0:
        print(f"Uzun Şık Doğruluk Oranı: %{longest_count/total*100:.2f}")
    
    print("-" * 30)
    print("Kısa/Eşit Cevaplar İçin Şık Dağılımı:")
    dist = calculate_distribution(short_list)
    for char in sorted(dist.keys()):
        print(f"{char}: {dist[char]}")

    print("-" * 30)
    print("Generating LaTeX file for short answers...")
    generate_latex(short_list, dist, total, longest_count, short_count, "short_answers.tex")
    print("Done. Output saved to 'short_answers.tex'.")

if __name__ == "__main__":
    main()

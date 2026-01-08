PYTHON = .venv/bin/python
VENV_DIR = .venv
PDF_FILE ?= final.pdf

.PHONY: all clean run setup pdf

all: run pdf

$(VENV_DIR):
	python3 -m venv $(VENV_DIR)

setup: $(VENV_DIR)
	$(PYTHON) -m pip install pypdf

run: setup
	@echo "Running analysis on $(PDF_FILE)..."
	@$(PYTHON) analyze.py "$(PDF_FILE)"

pdf: run
	@echo "Compiling PDF..."
	pdflatex short_answers.tex

clean:
	@echo "Cleaning up..."
	@rm -f short_answers.tex short_answers.pdf short_answers.aux short_answers.log

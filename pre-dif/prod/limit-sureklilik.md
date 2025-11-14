## Limit ve Süreklilik

Bu sayfa, türev ve diferansiyel denklemler öncesi **analiz altyapısını** hızlıca hatırlatmak için.

### 1. Limit Fikri (Gayriresmî)

Bir \(f(x)\) fonksiyonunun \(x \to a\) iken limiti \(L\) ise:
- \(x\), \(a\)'ya **yaklaştıkça**, \(f(x)\) değerleri \(L\)'ye **yaklaşır**.
- Bunu \(\lim_{x \to a} f(x) = L\) şeklinde yazarız.

**Kural:** Polinomlar ve "düzgün" fonksiyonlarda genelde
\[
\lim_{x \to a} f(x) = f(a)
\]
olur (fonksiyon orada sürekli ise).

### 2. Temel Limit Kuralları

Varsayalım \(\lim_{x \to a} f(x) = L\) ve \(\lim_{x \to a} g(x) = M\) mevcut.

- Toplama: \(\lim (f+g) = L+M\)
- Çarpma: \(\lim (f\cdot g) = L\cdot M\)
- Sabit çarpma: \(\lim (c f) = cL\)
- Bölme: \(\lim (f/g) = L/M\) (\(M \neq 0\)).

**Ders için mesaj:**
- Türev, limit tanımına dayandığı için bu kuralları içgüdüsel bilmek işlemleri hızlandırır.

### 3. Tek Taraflı ve Sonsuzda Limit

- **Sağ limit:** \(x \to a^+\) → \(x\), \(a\)'ya sağdan yaklaşır.
- **Sol limit:** \(x \to a^-\) → \(x\), \(a\)'ya soldan yaklaşır.
- İkisi eşitse ortak limit vardır.

Sonsuzda limit:
- \(\lim_{x \to \infty} f(x)\) veya \(\lim_{x \to -\infty} f(x)\): grafiğin uçlardaki davranışını verir.
- Örnek: \(\lim_{x \to \infty} \frac{1}{x} = 0\).

Bu kısım, çözümün uzun vadede neye yaklaştığını anlamak için ODE çözümlerinde işine yarar.

### 4. Süreklilik

Bir \(f\) fonksiyonu \(x=a\) noktasında **sürekli** ise:
1. \(f(a)\) tanımlı,
2. \(\lim_{x \to a} f(x)\) var,
3. \(\lim_{x \to a} f(x) = f(a).\)

Süreksizlik türleri (kısaca):
- Atlamalı, sonsuz, tanımsız noktalar vb.

**Önemli:** Polinomlar, üstel fonksiyonlar, \(\sin, \cos\) gibi temel fonksiyonlar **her yerde süreklidir**.

### 5. Türevlenebilirlik ve Süreklilik

- Bir noktada **türevlenebilir** olan fonksiyon, o noktada **kesinlikle süreklidir**.
- Tersi geçerli olmak zorunda değil (mutlak değer fonksiyonunda \(x=0\) örneği gibi).

Türev tanımı:
\[
f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}
\]

Bu tanımın arka planında hep limit kuralları vardır. Çoğu derste formülleri ezber kullanıyoruz ama teorik temel buradan geliyor.

### 6. Diferansiyel Denklemlerle Bağlantı

- Diferansiyel denklemlerde çözümler genelde **türev** ve **süreklilik** varsayımlarına dayanır.
- Çözüm fonksiyonunun tanım aralığını belirlerken limit ve süreklilik davranışını göz önünde bulundurmalısın (özellikle \(\ln x\), kök içeren fonksiyonlar vb.).

Bu sayfadaki fikirler, sınavda doğrudan uzun ispatlar olarak gelmese bile; hangi fonksiyonlarla rahat çalışabileceğini ve nerede dikkatli olman gerektiğini belirler.

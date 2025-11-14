## Diferansiyel Denklemler Özet

Bu sayfa, sınavda en çok işine yarayacak **temel ODE tipleri** için kısa bir reçete gibi.

### 1. Temel Tanımlar

- **Mertebe:** Denklemde geçen en yüksek türevin derecesi.
  - Örnek: \(y'' + 3y' - 2y = 0\) → 2. mertebe.
- **Lineer ODE:** \(y, y', y'', \dots\) terimleri 1. dereceden, çarpım yok.
  - Örnek: \(y' + p(x) y = q(x)\) lineer; \(y^2 y' = x\) lineer değil.
- **Genel çözüm:** İçinde sabitler (\(C, C_1, C_2\) gibi) barındıran çözüm ailesi.
- **Özel çözüm:** Başlangıç/kenar koşulları yerleştirilince elde edilen belirli çözüm.

### 2. Ayrılabilir Denklemler

**Form:**
\[
\frac{dy}{dx} = f(x) g(y)
\]
veya denk bir yazılış.

**Reçete:**
1. Tüm \(y\) terimlerini bir tarafa, \(x\) terimlerini diğer tarafa topla:
	\[
	\frac{1}{g(y)} dy = f(x) dx.
	\]
2. Her iki tarafı da integre et:
	\[
	\int \frac{1}{g(y)} dy = \int f(x) dx + C.
	\]
3. Mümkünse \(y\)'yi yalnız bırak.

**Mini örnek:**
\[
\frac{dy}{dx} = xy
\]
Ayır:
\[
\frac{1}{y} dy = x dx.
\]
Integralle:
\[
\ln|y| = \frac{x^2}{2} + C \Rightarrow y = C e^{x^2/2}.
\]

Bu tip denklemler, temel seviye fizik/uygulama sorularında sık gelir.

### 3. Birinci Mertebe Lineer Denklemler

**Genel form:**
\[
y' + p(x) y = q(x).
\]

**Reçete (entegrasyon faktörü):**
1. \(p(x)\)'i belirle.
2. Entegrasyon faktörünü hesapla:
	\[
	\mu(x) = e^{\int p(x) dx}.
	\]
3. Denklemin her iki yanını \(\mu(x)\) ile çarp:
	\[
	\mu(x) y' + \mu(x) p(x) y = \mu(x) q(x).
	\]
4. Sol taraf artık bir türevdir:
	\[
	\big(\mu(x) y\big)' = \mu(x) q(x).
	\]
5. Her iki tarafı integra et:
	\[
	\mu(x) y = \int \mu(x) q(x) dx + C.
	\]
6. Son olarak \(y\)'yi yalnız bırak:
	\[
	y(x) = \frac{1}{\mu(x)} \left( \int \mu(x) q(x) dx + C \right).
	\]

**Not:** `notes.tex` ve `prod/turev-integral.md` içinde bu tipe ait detaylı bir örnek var.

### 4. Sabit Katsayılı 2. Mertebe Lineer ODE'ler

**Genel form:**
\[
ay'' + by' + cy = 0, \quad a \ne 0.
\]

**Adım 1 – Karakteristik denklem:**
\[
a\lambda^2 + b\lambda + c = 0.
\]

Çözümler kök türüne göre ayrılır.

#### 4.1. İki Gerçek Ayrık Kök (\(\lambda_1 \ne \lambda_2\))

Karakteristik denklemden \(\lambda_1, \lambda_2 \in \mathbb{R}\) ve farklı olsun.

Genel çözüm:
\[
y(x) = C_1 e^{\lambda_1 x} + C_2 e^{\lambda_2 x}.
\]

#### 4.2. Çakışık Gerçek Kök (\(\lambda_1 = \lambda_2 = \lambda\))

Genel çözüm:
\[
y(x) = (C_1 + C_2 x) e^{\lambda x}.
\]

#### 4.3. Karmaşık Eşlenik Kökler (\(\lambda_{1,2} = \alpha \pm i\beta\))

Genel çözüm:
\[
y(x) = e^{\alpha x} (C_1 \cos(\beta x) + C_2 \sin(\beta x)).
\]

**Kısaca:**
- \(\Delta = b^2 - 4ac > 0\) → iki gerçek kök.
- \(\Delta = 0\) → çakışık kök.
- \(\Delta < 0\) → karmaşık kökler.

### 5. Zorlanmış (Sağ Taraflı) Sabit Katsayılı Lineer ODE – Kısa Not

Form:
\[
ay'' + by' + cy = g(x).
\]

Genel strateji:
1. Önce **homojen** kısmı çöz: \(ay'' + by' + cy = 0\) → \(y_h\).
2. Sonra, \(g(x)\)'in türüne göre bir **özel çözüm** \(y_p\) tahmin et.
	- \(g(x)\) polinom ise: polinom dene.
	- \(g(x) = e^{kx}\) ise: \(Ae^{kx}\) dene.
	- \(g(x) = \sin bx\) veya \(\cos bx\) ise: \(A\cos bx + B\sin bx\) dene.
3. Toplam çözüm: \(y = y_h + y_p\).

Detaylar ders seviyene göre değişir ama bu şema aklında dursun.

### 6. Fiziksel Yorumlar (Çok Kısa)

- **Harmonik osilatör:** \(y'' + \omega^2 y = 0\) → sinüs-kosinüs tipi çözümler (salınım).
- **Sönümlü salınım:** \(y'' + 2\gamma y' + \omega^2 y = 0\) → üstteki karakteristik kök analizini doğrudan kullanır.

Bu tip yorumlar, elde ettiğin çözümün formunun mantıklı olup olmadığını kontrol etmek için iyi bir sezgi kaynağıdır.

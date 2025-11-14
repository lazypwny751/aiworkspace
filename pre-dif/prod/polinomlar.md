## Polinomlar ve Temel Fonksiyonlar

Bu sayfa, diferansiyel denklemlerde karşına çıkan fonksiyonları rahatça tanıyıp onlarla işlem yapabilmen için kısa bir özet.

### 1. Polinom Tanımı ve Gösterim

- Genel polinom: \( P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0 \)
- \(n\): **derece**, \(a_i\): **katsayılar**, \(a_n \neq 0\).
- Örnek: \( P(x) = 2x^3 - 5x + 1 \) → derece 3, baş katsayı 2.

**Not:** Diferansiyel denklemlerde sık sık polinom katsayılarıyla çalışan denklemler göreceksin (ör: \(y'' - 3y' + 2y = 0\)). Katsayıları ve dereceleri doğru okumak önemli.

### 2. Polinomlarda Temel İşlemler

- **Toplama/çıkarma:** Benzer dereceli terimleri topla.
	- Örnek: \((2x^2 + 3x - 1) + (x^2 - x + 4) = 3x^2 + 2x + 3.\)
- **Çarpma:** Dağılma özelliği, gerekiyorsa çarpanlara ayırma.
	- Örnek: \((x+1)(x-2) = x^2 - x - 2.\)
- **Bölme:** Uzun bölme ya da sentetik bölme (sınavda genelde basit örnekler gelir).

Bu işlemler, özellikle **karakteristik polinom** çözerken önemli (ör: \(\lambda^2 - 3\lambda + 2 = 0\)).

### 3. Kökler ve Çarpanlara Ayırma

- \(P(x)\) polinomunun \(x = r\) noktasında kökü varsa, \(P(r) = 0\) ve \((x-r)\) \(P(x)\)'i böler.
- İkinci derece için standart formül:
	\[
	ax^2 + bx + c = 0 \Rightarrow x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.
	\]
- Örnek: \(x^2 - 3x + 2 = 0\) → kökler \(x=1, x=2\), dolayısıyla \(x^2 - 3x + 2 = (x-1)(x-2).\)

**Diferansiyel denklem bağlantısı:**
- 2. mertebe sabit katsayılı lineer ODE'de karakteristik denklem hep bir polinomdur.
	- Örnek: \(y'' - 3y' + 2y = 0 \Rightarrow \lambda^2 - 3\lambda + 2 = 0 \Rightarrow (\lambda-1)(\lambda-2)=0.\)
- Kökler çözüm biçimini belirler (ayrıntı `diferansiyel-denklemler.md`'de olacak).

### 4. Temel Fonksiyon Tipleri (Kısa Liste)

Bu fonksiyon tipleri diferansiyel denklemlerde **standart çözümler** olarak sık sık karşına çıkar:

1. **Polinomlar:** \(P(x)\).
2. **Üstel fonksiyonlar:** \(e^{kx}\), \(a^x\).
3. **Trigonometrik fonksiyonlar:** \(\sin x, \cos x, \tan x, \dots\)
4. **Logaritma:** \(\ln x, \log_a x\).

Bu liste ayrıntılı olarak `prod/fonksiyonlar.md` içinde genişletilecek.

---

## Temel Fonksiyonlar ve Grafik Sezgisi

Bu bölüm, polinomlar dışındaki **temel fonksiyon aileleri**ni ve bunların kaba grafik davranışını hızlıca hatırlatmak için eklendi. LaTeX tarafında `src/fonksiyonlar.tex` dosyasına karşılık gelir.

### 1. Üs, Kök ve Rasyonel Fonksiyonlar

**Üs fonksiyonları** \(f(x) = x^n\) için:

- \(n\) tek ise: grafik orijinden geçer, bir ucu aşağı, bir ucu yukarı giden S-vari şekiller (\(x\), \(x^3\) gibi).
- \(n\) çift ise: \(y\)-ekseni etrafında simetrik, yukarı (veya aşağı) doğru açılan `U` şekilli grafikler (\(x^2\), \(x^4\) gibi).

**Kök fonksiyonları** \(f(x) = \sqrt[m]{x}\) gibi fonksiyonlarda genelde sadece belli bir aralıkta tanım vardır (mesela \(\sqrt{x}\) için \(x \ge 0\)); grafik orijinden çıkıp yavaş artar.

**Rasyonel fonksiyonlar** \(f(x) = \dfrac{P(x)}{Q(x)}\):

- Payda sıfır olduğunda tanımsızdır, bu noktalarda dikey asimptot görürsün.
- Pay ve payda derecelerine göre sonsuzdaki davranış (yatay / eğik asimptot) belirlenir.

### 2. Üstel ve Logaritmik Fonksiyonlar

**Üstel fonksiyonlar** \(f(x) = a^x\) (\(a>0, a\neq 1\)):

- Tanım kümesi: \(\mathbb{R}\), değer kümesi: \((0,\infty)\).
- \(a>1\) ise artan, \(0<a<1\) ise azalan fonksiyondur.
- Diferansiyel denklemlerde \(e^{kx}\) tipi çözümler her yerde karşına çıkar.

**Logaritmik fonksiyonlar** \(f(x) = \log_a x\):

- Tanım kümesi: \((0,\infty)\), değer kümesi: \(\mathbb{R}\).
- \(a>1\) ise artan, \(0<a<1\) ise azalan.
- \(y = \log_a x\), \(y = a^x\)'in ters fonksiyonudur.

### 3. Trigonometrik Fonksiyonlar

Temel trig fonksiyonları: \(\sin x, \cos x, \tan x\).

- \(\sin x\) ve \(\cos x\): periyodik, aralıkları \([-1,1]\), düzgün (her yerde türevli) grafikler.
- \(\tan x\): periyodik ama dikey asimptotları vardır, her yerde tanımlı değildir.
- Türevler: \((\sin x)' = \cos x\), \((\cos x)' = -\sin x\).

Bu fonksiyonlar özellikle **salınım (osilasyon)** içeren diferansiyel denklemlerin çözümlerinde (ör. sarmal yay, harmonik osilatör) doğrudan çıkar.

### 4. Grafik ve Sezgi Odaklı Notlar

Farklı fonksiyon tiplerinin grafiklerini kafanda netleştirmek, hem limit / türev yorumunu hem de diferansiyel denklem çözümlerinin davranışını anlamanı çok kolaylaştırır:

- **Artan / azalan:** Grafik sağa giderken yukarı mı çıkıyor, aşağı mı iniyor?
- **Konveks / konkav:** İkinci türevin işareti grafiğin `çukur` mu `tepe` mi olduğunu söyler.
- **Asimptotlar:** Rasyonel veya logaritmik fonksiyonlarda, grafiğin yaklaşıp dokunmadığı doğrular var mı?

Bu notları, ayrıntılı anlatım için oluşturulacak `prod/fonksiyonlar.md` dosyasına taşıyabilirsin; burada fikir düzeyinde kısa bir özet tutuluyor.

### 5. Limit ve Süreklilik ile Bağlantı

- Polinomlar **her yerde sürekli ve türevlenebilir**.
- \(e^x, \sin x, \cos x\) gibi temel fonksiyonlar da aynı şekilde `iyi huylu` fonksiyonlardır.
- \(\ln x\) sadece \(x>0\) için tanımlı; \(x \to 0^+\) yaklaşırken limit davranışı kritik.

**Ders için mesaj:**

- Bu sayfadaki polinom ve temel fonksiyon notları, diferansiyel denklemlerin *ön yüzü* gibi: karakteristik denklemler, temel çözümler ve çözümün davranışını anlamak için bunlara hâkim olman gerekiyor.

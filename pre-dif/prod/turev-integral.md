# Diferansiyel Denklemler İçin Türev ve İntegral Özeti

Bu dosya, `notes.tex` belgesinde topladığımız içeriklerin **hızlı tekrar için düz metin/Markdown özeti**dir. Amaç: diferansiyel denklemler çözerken ihtiyaç duyacağın temel türev, integral ve birkaç temel ODE örneğini tek yerde görmek.

---

## 1. Temel Türev Kuralları

- **Sabitin türevi**  
  \(\dfrac{d}{dx}(c)=0\)

- **Sabit katsayılı türev**  
  \(\dfrac{d}{dx}[c f(x)] = c f'(x)\)  
  Örnek: \(f(x)=x^2\) ise \(3x^2 = 3f(x)\), dolayısıyla
  \(\dfrac{d}{dx}(3x^2) = 3 f'(x) = 6x\).

- **Toplam / fark**  
  \(\dfrac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)\).

- **Çarpım kuralı**  
  \(\dfrac{d}{dx}[f(x)g(x)] = f'(x)g(x)+f(x)g'(x)\).

- **Bölüm kuralı**  
  \(\displaystyle \dfrac{d}{dx}\Big[\dfrac{f(x)}{g(x)}\Big] = \dfrac{f'(x)g(x)-f(x)g'(x)}{[g(x)]^2}\).

- **Zincir kuralı**  
  \(y=f(g(x))\) ise \(\dfrac{dy}{dx} = f'(g(x))\,g'(x)\).

- **Güç kuralı** (türev)  
  \(\dfrac{d}{dx}(x^n) = n x^{n-1}\).

- **Üstel fonksiyonlar**  
  \(\dfrac{d}{dx}(e^x)=e^x\),  
  \(\dfrac{d}{dx}(a^x) = a^x\ln a\).

- **Temel trigonometrik türevler**  
  \(\dfrac{d}{dx}(\sin x) = \cos x\)  
  \(\dfrac{d}{dx}(\cos x) = -\sin x\)  
  \(\dfrac{d}{dx}(\tan x) = \sec^2 x\)

- **Logaritma türevleri**  
  \(\dfrac{d}{dx}(\ln x)=\dfrac{1}{x}\) (\(x>0\))  
  \(\dfrac{d}{dx}(\log_a x)=\dfrac{1}{x\ln a}\).

---

## 2. Kısmi Türevler

- \(z=f(x,y)\) için \(\partial f/\partial x\), \(\partial f/\partial y\).  
- Bir değişkene göre türev alırken diğerleri sabit kabul edilir.  
- Yüksek mertebe kısmi türevler: \(\partial^2 f / \partial x^2\), \(\partial^2 f / \partial x \partial y\) vb.

Bu kısım, çok değişkenli fonksiyon içeren diferansiyel denklemler (PDE) için temel.

---

## 3. Belirsiz İntegraller

Belirsiz integral türevin tersidir: \(F'(x)=f(x)\) ise \(\int f(x)\,dx = F(x)+C\).

- **Sabitin integrali**  
  \(\int c\,dx = c x + C\).

- **Güç kuralı** (integral)  
  \(n \neq -1\) için  
  \(\displaystyle \int x^n\,dx = \dfrac{x^{n+1}}{n+1} + C\).

- **Doğrusallık**  
  \(\int [a f(x)+b g(x)]\,dx = a \int f(x)\,dx + b \int g(x)\,dx\).

- **Temel integraller**  
  \(\int e^x\,dx = e^x + C\)  
  \(\int a^x\,dx = \dfrac{a^x}{\ln a}+C\)  
  \(\int \cos x\,dx = \sin x + C\)  
  \(\int \sin x\,dx = -\cos x + C\)  
  \(\int \sec^2 x\,dx = \tan x + C\)  
  \(\int \dfrac{1}{x}\,dx = \ln|x| + C\).

### 3.1. Değişken Dönüşümü (Substitüsyon)

- Kural: \(u = g(x)\), \(g\) tersinir ve türevlenebilir ise  
  \(\displaystyle \int f(g(x))g'(x)\,dx = \int f(u)\,du\).

- Tipik ODE motivasyonlu örnek:  
  \(\displaystyle \int 2x e^{x^2}\,dx\), \(u=x^2\) al:  
  \(\int 2x e^{x^2}\,dx = \int e^u\,du = e^u + C = e^{x^2} + C\).

### 3.2. Kısmi İntegrasyon

- Kural:  
  \(\displaystyle \int u\,dv = uv - \int v\,du\).

- Örnek: \(\displaystyle \int x e^x\,dx\), \(u=x, dv=e^x dx\):  
  \(\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C = e^x(x-1)+C\).

---

## 4. Belirli İntegraller

- **Tanım (Temel Teorem)**  
  \(F'(x)=f(x)\) ise  
  \(\displaystyle \int_a^b f(x)\,dx = F(b)-F(a)\).

- **Doğrusallık ve aralık bölme**  
  \(\int_a^b [a f(x)+b g(x)]\,dx = a \int_a^b f(x)\,dx + b \int_a^b g(x)\,dx\)  
  \(\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx\).

- **Simetri**  
  Tek fonksiyon \(f(-x)=-f(x)\): \(\int_{-a}^a f(x)\,dx=0\).  
  Çift fonksiyon \(f(-x)=f(x)\): \(\int_{-a}^a f(x)\,dx = 2\int_0^a f(x)\,dx\).

---

## 5. Katlı İntegraller (Kısaca)

- İki katlı integral:  
  Dikdörtgen bölge \(D=[a,b]\times[c,d]\):  
  \(\displaystyle \iint_D f(x,y)\,dA = \int_c^d \int_a^b f(x,y)\,dx\,dy = \int_a^b \int_c^d f(x,y)\,dy\,dx\).

- Üç katlı integral:  
  \(E=[a,b]\times[c,d]\times[e,f]\):  
  \(\displaystyle \iiint_E f(x,y,z)\,dV = \int_e^f \int_c^d \int_a^b f(x,y,z)\,dx\,dy\,dz\).

Bunlar, diferansiyel denklemlerin alan/hacim yorumları ve bazı integral biçimleri için temel araçlar.

---

## 6. Örnek Diferansiyel Denklemler

### 6.1. Ayrılabilir Denklem

\(\displaystyle \frac{dx}{dy} = \frac{x^3}{y^3}(y-3)\)

- Ayr:  
  \(\dfrac{dx}{x^3} = \Big(\dfrac{y-3}{y^3}\Big) dy = \Big(\dfrac{1}{y^2} - \dfrac{3}{y^3}\Big) dy\).
- İntegral al:  
  \(\int x^{-3} dx = -\dfrac{1}{2x^2} + C_1\)  
  \(\int (y^{-2} - 3y^{-3}) dy = -\dfrac{1}{y} + \dfrac{3}{2y^2} + C_2\).
- Sabitleri birleştir:  
  \(-\dfrac{1}{2x^2} = -\dfrac{1}{y} + \dfrac{3}{2y^2} + C\).  
  Düzenleyerek:  
  \(\dfrac{1}{2x^2} = \dfrac{1}{y} - \dfrac{3}{2y^2} + C'\).

Bu, \(x\) ile \(y\) arasındaki **implicit** çözüm bağıntısıdır. İstenirse \(x(y)\) açık da yazılabilir.

### 6.2. Birinci Mertebe Lineer Denklem

\(\displaystyle y' + 2xy = 2x e^{-x^2}\)

- Standart form: \(y' + P(x)y = Q(x)\), burada \(P(x)=2x\), \(Q(x)=2x e^{-x^2}\).
- Entegrasyon faktörü:  
  \(\mu(x) = e^{\int 2x dx} = e^{x^2}\).
- Denklem:  
  \(e^{x^2} y' + 2x e^{x^2} y = 2x\)  
  Sol taraf: \(\dfrac{d}{dx}(e^{x^2} y) = 2x\).
- İntegral al:  
  \(e^{x^2} y = \int 2x dx = x^2 + C\).  
  \(\Rightarrow y(x) = e^{-x^2}(x^2 + C)\).

Bu iki örnek, nottaki türev/integral kurallarının diferansiyel denklemlere nasıl uygulandığını gösteren temel şablonlardır.

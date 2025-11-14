## Katlı İntegraller

Bu sayfa, iki ve üç katlı integralleri **reçete gibi** hatırlaman için kısa bir özet.

### 1. İki Katlı İntegralin Temel Fikri

\(f(x,y)\) sürekli bir fonksiyon olsun.

- Dikdörtgensel bölgede:
	\[
	R = [a,b] \times [c,d]
	\]
	için iki katlı integral:
	\[
	\iint_R f(x,y) \, dA = \int_a^b \int_c^d f(x,y) \, dy \, dx
	\]
	veya ters sırayla:
	\[
	\iint_R f(x,y) \, dA = \int_c^d \int_a^b f(x,y) \, dx \, dy.
	\]

**Not:** Sınavda çoğu soru, önce bu formu tanımayı ve doğru sınırları yazmayı gerektirir.

### 2. Dikdörtgen Olmayan Bölgeler

Bölge, genelde şu iki tipten biri gibi verilir:

1. \(D = \{(x,y) : a \le x \le b, \ g_1(x) \le y \le g_2(x)\}\)
2. \(D = \{(x,y) : c \le y \le d, \ h_1(y) \le x \le h_2(y)\}\)

Bu durumda:
\[
\iint_D f(x,y)\,dA = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} f(x,y)\,dy \right) dx
\]
veya ikinci tipe göre benzer.

**Yapman gereken:**
- Bölgeyi kağıda çiz.
- \(x\) veya \(y\)'ye göre kesit al, alt/üst sınır fonksiyonlarını belirle.

### 3. Koordinat Dönüşümleri (Kısaca)

Bazı integrallerde, polar/silindirik/küresel koordinatlara geçmek hesabı kolaylaştırır.

- **Kutupsal (polar) koordinatlar:**
	- Dönüşüm: \(x = r \cos\theta, \ y = r \sin\theta\).
	- Alan elemanı: \(dA = r\,dr\,d\theta\).

Örnek form:
\[
\iint_D f(x,y)\,dA = \int_{\theta_1}^{\theta_2} \int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta) \, r\,dr\,d\theta.
\]

Genelde daire/disk tipi bölgelerde bu yöntem işini kolaylaştırır.

### 4. Üç Katlı İntegraller

Üç değişkenli bir fonksiyon için hacim üzerinde integral:
\[
\iiint_E f(x,y,z)\,dV
\]
- Dikdörtgensel bölgede:
	\[
	E = [a,b]\times[c,d]\times[e,f]
	\]
	ise integral, iç içe üç tekli integral hâline gelir.

**Uygulama:** Hacim hesabı, kütle hesabı (yoğunluk fonksiyonu ile), ortalama değer vb.

### 5. Diferansiyel Denklemlerle Bağlantı

Katlı integraller doğrudan başlangıç diferansiyel denklemlerinde çok sık sorulmayabilir fakat:

- Sınır değer problemlerinde (PDE tarafı) ve fiziksel modellerde (ısı iletimi, kütle/enerji korunumu) hacim/alan hesapları gerekir.
- Bir çözümün **ortalama değeri** veya belirli bir bölgedeki toplam etkisini hesaplarken katlı integral fikri kullanılır.

Bu sayfa, PDE ağırlıklı kısma geçtiğinde (veya fizik uygulamalarında) hızlıca geri dönüp bakabileceğin bir özet olarak duracak.

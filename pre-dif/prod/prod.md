# Diferansiyel Denklemler İçin Genel Özet

Bu dosya, diferansiyel denklemler dersine gelirken el altında bulunması gereken **genel özet haritasıdır**. Her başlık altında çok kısa hatırlatma var; detaylar ilgili prod dosyalarında tutulacak.

## 1. Polinomlar ve Temel Fonksiyonlar (ÖZET)

- Polinom tanımı, derece, katsayılar
- Kök ve çarpanlara ayırma
- Temel fonksiyon tipleri: polinom, üstel, logaritma, trigonometrik fonksiyonlar
- Bu fonksiyonların grafiksel davranışı

**Detaylı özet için:** `prod/polinomlar.md`

## 2. Limit ve Süreklilik (ÖZET)

- Limit fikri ve temel limit kuralları
- Tek taraflı limitler, sonsuzda limit
- Süreklilik tanımı ve tipik süreksizlik türleri
- Türevlenebilirlik ⇒ süreklilik ilişkisi

**Detaylı özet için:** `prod/limit-sureklilik.md`

## 3. Türev ve Diferansiyel (ÖZET)

Türev; değişim oranı, eğim ve lineer yakınsama kavramlarını taşır. Diferansiyel denklemlerde, türev operatörü temel yapı taşıdır.

- Temel türev kuralları (sabit, sabit katsayı, toplam, çarpım, bölüm, zincir, güç)
- Üstel, logaritma ve trigonometrik fonksiyonların türevleri
- Kısmi türevler ve yüksek mertebeden türevler

**Detaylı türev/integral kuralları ve örnekler için:**
- `prod/turev-integral.md`

## 4. İntegral (Belirsiz/Belirli) (ÖZET)

İntegral; alan, birikim ve türevin tersi olarak yorumlanır. Diferansiyel denklemleri çözerken sıkça kullanılır.

- Belirsiz integral: \(\int f(x)\,dx = F(x)+C\)
- Temel integral kuralları ve tabloları
- Substitüsyon (değişken değiştirme)
- Kısmi integrasyon
- Belirli integraller ve Temel Teorem
- Simetri kuralları

**Tüm ayrıntılar ve örnekler için yine:**
- `prod/turev-integral.md`

## 5. Katlı İntegraller (ÖZET)

Çok değişkenli fonksiyonların alan/hacim yorumları ve bazı diferansiyel denklemlerin integral biçimleri için gerekir.

- İki katlı integraller: \(\iint_D f(x,y)\,dA\)
- Üç katlı integraller: \(\iiint_E f(x,y,z)\,dV\)
- Dikdörtgen/Dikdörtgensel bölgelerde sıralı integraller

**Detaylı özet için:** `prod/katli-integraller.md`

## 6. Diferansiyel Denklemlere Giriş (ÖZET)

- Diferansiyel denklem: içinde türev bulunan denklem.
- Derece, mertebe (order), genel ve özel çözüm kavramları.
- Önemli türler:
  - Ayrılabilir denklemler
  - Birinci mertebe lineer denklemler (entegrasyon faktörü)
  - Sabit katsayılı 2. mertebe lineer ODE'ler

**Detaylı özet ve çözüm reçeteleri için:** `prod/diferansiyel-denklemler.md`

---

## Yol Haritası

1. `prod/turev-integral.md` — türev/integral + iki temel ODE örneği  
2. `prod/polinomlar.md` — polinom ve temel fonksiyonlar özeti  
3. `prod/limit-sureklilik.md` — limit, süreklilik, türev öncesi analiz özeti  
4. `prod/katli-integraller.md` — çok değişkenli integraller özeti  
5. `prod/diferansiyel-denklemler.md` — temel ODE türleri ve çözüm reçeteleri

Bu dosya (`prod/prod.md`), hepsi için **ana index**/içindekiler gibi düşünülebilir.

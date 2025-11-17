# Fair-Meetup-Finder

**Adil Buluşma Noktası Belirleyici**

Bu proje, üç farklı konumdaki arkadaş grubu için herkesin yolculuk süresinin birbirine en yakın (yani *en adil*) olduğu buluşma noktasını hesaplayan, Python tabanlı bir öğrenme projesidir. Düz çizgi mesafe yerine gerçek yolculuk sürelerini kullanarak karar verir.

---

## Özellikler

* Üç kullanıcı için aday buluşma noktalarından en adilini seçer.
* OpenRouteService (ORS) API'si ile gerçek yolculuk sürelerini çeker (sürüş yaya vb. modlar desteklenir).
* Adalet puanını, üç kullanıcının aday mekana varış süreleri arasındaki **maksimum fark** olarak hesaplar (düşük puan = daha adil).
* Kolayca genişletilebilir: POI (restoran/kafe) çekme, harita görselleştirme, farklı optimizasyon kriterleri eklenebilir.

---

## Hızlı Başlangıç (Quickstart)

Aşağıdaki adımlar, projeyi yerel makinenizde çalıştırmak için yeterlidir.

### Gereksinimler

* Python 3.8 veya üstü
* Bir sanal ortam (önerilir)
* OpenRouteService API anahtarı (ücretsiz üyelik ile alınabilir)

### 1) Depoyu klonlayın

```bash
git clone https://github.com/bilalyazicioglu/Fair-Meetup-Finder.git
cd Fair-Meetup-Finder
```

### 2) Sanal ortam oluşturun ve bağımlılıkları kurun

```bash
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
.\.venv\Scripts\activate   # Windows (PowerShell)

pip install -r requirements.txt
```

### 3) ORS API anahtarını ayarlayın

Ana dizinde `.env` dosyası oluşturun ve içine şu satırı ekleyin:

```
ORS_API_KEY="SİZİN_GERÇEK_API_ANAHTARINIZ"
```

> Not: `.gitignore` zaten `.env` dosyasını hariç tutuyorsa, anahtarınız GitHub'a gönderilmez.

### 4) `main.py` içindeki konum ve ayarları düzenleyin

`main.py` içinde bulunan değişkenleri kendi koordinatlarınıza ve tercihlerinize göre güncelleyin:

* `ARKADAS_KONUMLARI` — 3 arkadaşın `[enlem, boylam]` formatında listesi.
* `GEÇİCİ_ADAY_MEKANLAR` — kontrol etmek istediğiniz aday lokasyonların listesi.
* `YOLCULUK_MODU` — örn: `'driving-car'`, `'foot-walking'`, `'cycling-regular'`.

Örnek:

```python
ARKADAS_KONUMLARI = [
    (40.990, 29.124),  # Arkadaş A
    (41.005, 28.976),  # Arkadaş B
    (40.987, 29.035),  # Arkadaş C
]

YOLCULUK_MODU = 'driving-car'
```

### 5) Çalıştırın

Sanal ortam aktifken:

```bash
python main.py
```

Çıktıda her aday mekan için üç kullanıcının süreleri, hesaplanan "Adalet Puanı" ve en adil yer gösterilir.

---

## Nasıl Çalışır? (Detaylı)

1. Kullanıcı konumları (`ARKADAS_KONUMLARI`) ve aday mekanlar (`GEÇİCİ_ADAY_MEKANLAR`) alınır.
2. Her aday mekan için, proje ORS Directions API'yi kullanarak **her kullanıcıdan o mekana olan gerçek yolculuk süresini** çeker.
3. Aday mekanın adalet puanı, üç sürenin maksimum eksi minimum farkı veya en uzun ve en kısa süre arasındaki fark şeklinde hesaplanır.
4. Adalet puanı en düşük olan aday, önerilen "En Adil Buluşma Noktası" olur.

> İleri seviyede alternatif adalet fonksiyonları: ağırlıklı farklar (ör. toplam süre + normalize fark), medyan bazlı ölçümler, veya kullanıcı tercihleri (ör. bir kullanıcının daha az yolculuk yapmasını istemesi).

---

## Dosya Yapısı

```
Fair-Meetup-Finder/
├─ .gitignore
├─ README.md                    # (Bu dosya)
├─ main.py                      # Uygulamanın giriş noktası
├─ requirements.txt             # Bağımlılıklar
└─ (isteğe bağlı) examples/     # Örnek konum/çalıştırma çıktıları
```

`main.py` içinde kod; ORS istekleri, süre hesaplama ve adalet metriğinin uygulanması bulunur.

---

## requirements.txt

Projede kullanılan temel paketler (örnek):

```
requests
geopy
python-dotenv
```

Mevcut `requirements.txt` dosyasını kontrol edin; eksikse `pip freeze` ile proje ihtiyaçlarına göre güncelleyin.

---

## Örnek Çıktı

```
Aday Mekan: Cafe X
 - Süreler: [12, 15, 14] dakika
 - Adalet Puanı: 3

Aday Mekan: Restaurant Y
 - Süreler: [25, 10, 18] dakika
 - Adalet Puanı: 15

En Adil Buluşma Noktası: Cafe X (Adalet Puanı: 3)
```

---

## Geliştirme Fikirleri / Yol Haritası

* **Dinamik POI çekme:** Aday mekan listesini elle girmek yerine, ORS veya başka bir Places API ile merkezin etrafındaki restoran/kafe/POI'leri otomatik çek.
* **Harita Görselleştirme:** Sonucu interaktif bir haritada göster (Folium veya Leaflet).
* **Web Arayüzü / CLI:** Terminal tabanlı input yerine adres tabanlı veya web arayüzü ile kullanıcı dostu giriş.
* **Çoklu kullanıcı desteği:** 3'ten fazla kullanıcıyı destekleyecek şekilde genişletme.
* **Alternatif optimizasyonlar:** Minimum toplam seyahat süresi + adalet dengesi gibi kombinasyonlar.

---

## İletişim

Proje sahibi: **bilalyazicioglu**

Sorular/öneriler için GitHub Issues veya doğrudan repo sahibiyle iletişime geçebilirsiniz.

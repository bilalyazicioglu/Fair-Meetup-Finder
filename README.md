🤝 Fair-Meetup Finder: Adil Buluşma Noktası Belirleyici
Bu proje, üç farklı konumdaki arkadaş grubu için, herkesin yolculuk süresinin birbirine en yakın (en adil) olduğu buluşma noktasını bulmayı amaçlayan, Python tabanlı bir hafta sonu öğrenme projesidir.

Proje, düz çizgi mesafesi yerine, OpenRouteService (ORS) API'sinden alınan gerçek yolculuk sürelerini baz alarak en uygun çözümü optimize eder.

✨ Nasıl Çalışır?
Konum Girişi: Üç arkadaşın koordinatları (ARKADAS_KONUMLARI) koda girilir.

Aday Mekanlar: Önceden belirlenmiş potansiyel buluşma mekanları listesi (GEÇİCİ_ADAY_MEKANLAR) kullanılır.

Gerçek Süre Hesaplama: Her arkadaşın her bir aday mekana olan yolculuk süresi (YOLCULUK_MODU dikkate alınarak) ORS API aracılığıyla çekilir.

Adalet Puanı: Her aday mekan için, üç yolculuk süresi arasındaki en büyük fark hesaplanır. Bu fark, mekanın "Adalet Puanı"dır.

Optimizasyon: Adalet Puanı en düşük olan mekan (yani sürelerin birbirine en yakın olduğu yer) En Adil Buluşma Noktası olarak seçilir.

⚙️ Kurulum ve Çalıştırma
1. Kütüphaneleri Kurma

Proje için gerekli Python kütüphanelerini requirements.txt dosyasından kurun:

Bash
pip install -r requirements.txt
2. API Anahtarını Ayarlama (Çok Önemli!)

Bu proje, kodunuzu GitHub'a güvenle yüklemeniz için .env dosyası kullanır.

OpenRouteService (ORS) API sitesinden ücretsiz bir anahtar alın.

Projenizin ana klasöründe .env adında bir dosya oluşturun.

.env dosyasına anahtarınızı şu formatta yazın:

Kod snippet'i
# .env dosyasının içeriği
ORS_API_KEY="SİZİN_GERÇEK_API_ANAHTARINIZ" 
Not: .gitignore dosyası sayesinde bu hassas bilgi GitHub'a yüklenmez.

3. Konumları ve Modu Güncelleme

main.py dosyasını açın ve aşağıdaki değişkenleri kendi ihtiyacınıza göre ayarlayın:

ARKADAS_KONUMLARI: 3 arkadaşın (Enlem, Boylam) koordinatlarını güncelleyin.

YOLCULUK_MODU: Tercih ettiğiniz modu seçin. (Örn: 'driving-car' veya 'foot-walking')

4. Çalıştırma

Sanal ortamınız aktifken terminalde kodu çalıştırın:

Bash
python main.py
🔑 Kullanılan Teknolojiler
Python 3: Projenin ana dili.

requests: Harita API'lerine HTTP istekleri göndermek için.

geopy: Koordinatların işlenmesi için.

python-dotenv: API anahtarını .env dosyasından güvenli bir şekilde okumak için.

OpenRouteService (ORS) API: Gerçek yolculuk mesafesi ve süresi verilerini çekmek için.

💡 İleri Geliştirme Fikirleri
Bu bir öğrenme projesi olduğu için, aşağıdaki özellikler eklenerek proje daha da geliştirilebilir:

Dinamik POI (Point of Interest) Çekme: GEÇİCİ_ADAY_MEKANLAR listesini elle girmek yerine, merkez noktanın etrafındaki restoranları/kafeleri ORS POI API'si veya Google Places API'si ile otomatik olarak çekme.

Görselleştirme: Elde edilen sonucu, arkadaşların konumları ve önerilen en adil buluşma noktasının işaretlendiği interaktif bir haritada (Folium kütüphanesi ile) gösterme.

Daha Karmaşık Optimizasyon: Sadece farkı değil, aynı zamanda toplam minimum süreyi de hesaba katan ağırlıklı bir adalet puanı kullanma.

Kullanıcı Girişi: Koordinatları koda yazmak yerine, programın başında kullanıcıdan terminal aracılığıyla adresleri isteme.
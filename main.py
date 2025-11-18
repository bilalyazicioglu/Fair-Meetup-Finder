import requests
import math
from geopy.distance import geodesic
import os

from dotenv import load_dotenv
load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY") 
YOLCULUK_MODU = 'foot-walking' 

ARKADAS_KONUMLARI = [
    (41.0005706, 29.1366665),  # 1. Arkadaş: Değiştirilmiş Konum
    (41.0325548, 29.0904451),  # 2. Arkadaş: Değiştirilmiş Konum 2
    (41.0209485, 29.0394974)   # 3. Arkadaş: Capitol AVM
]

def hesapla_geometrik_merkez(koordinatlar):
    """Verilen koordinatların geometrik merkezini hesaplar (Ortalama Enlem/Boylam)."""
    toplam_enlem = sum(lat for lat, lon in koordinatlar)
    toplam_boylam = sum(lon for lat, lon in koordinatlar)
    
    merkez = (toplam_enlem / len(koordinatlar), toplam_boylam / len(koordinatlar))
    return merkez

GEÇİCİ_ADAY_MEKANLAR = [
    {"Ad": "Kadıköy Sahil", "Koord": (41.0003, 29.0357)},
    {"Ad": "Kız Kulesi Yakını", "Koord": (41.0205, 29.0040)},
    {"Ad": "Metropol AVM", "Koord": (40.9939749, 29.1226758)},
    {"Ad": "Cadde McDonalds", "Koord": (40.963919, 29.0656023)},
    {"Ad": "Beşiktaş İskele", "Koord": (41.04103, 29.007345)}
]

def get_travel_time_ors(start_lat_lon, end_lat_lon, mode):
    """OpenRouteService API'den yolculuk süresini (dakika) çeker."""
    payload = {
        "coordinates": [[start_lat_lon[1], start_lat_lon[0]], [end_lat_lon[1], end_lat_lon[0]]]
    }
    
    url = f"https://api.openrouteservice.org/v2/directions/{mode}/json"
    headers = {
        'Accept': 'application/json, application/geo+json',
        'Authorization': ORS_API_KEY,
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"!!! UYARI: API HTTP Kodu: {response.status_code}")
            print(f"!!! UYARI: API Yanıt Metni: {response.text[:100]}") 
            response.raise_for_status() # Hata kodu fırlat

        data = response.json()
        duration_seconds = data['routes'][0]['summary']['duration']
        return duration_seconds / 60
        
    except Exception as e:
        return None

def main():
    """Projenin ana çalışma döngüsü."""
    print("--- Arkadaş Konumları ---")
    print("Birinci Konum: ", ARKADAS_KONUMLARI[0])
    print("İkinci Konum: ", ARKADAS_KONUMLARI[1])
    print("Üçüncü Konum: ", ARKADAS_KONUMLARI[2])
    merkez_nokta = hesapla_geometrik_merkez(ARKADAS_KONUMLARI)
    print("--- Konum Ortaklama Projesi Başladı ---")
    print(f"Hesaplanan Geometrik Merkez: {merkez_nokta}")
    print(f"Yolculuk Modu: {YOLCULUK_MODU}\n")

    sonuclar = []

    for mekan in GEÇİCİ_ADAY_MEKANLAR:
        aday_sureler = []
        
        for i, arkadas_koordinat in enumerate(ARKADAS_KONUMLARI):
            sure = get_travel_time_ors(arkadas_koordinat, mekan["Koord"], YOLCULUK_MODU)
            aday_sureler.append(sure)

        if all(s is not None for s in aday_sureler):
            min_sure = min(aday_sureler)
            max_sure = max(aday_sureler)
            adalet_puani = max_sure - min_sure

            sonuclar.append({
                "Mekan Adı": mekan["Ad"],
                "Süreler (dk)": [round(s, 1) for s in aday_sureler],
                "Adalet Puanı (Fark)": round(adalet_puani, 1),
                "Ortalama Süre": round(sum(aday_sureler) / len(aday_sureler), 1)
            })

    sonuclar.sort(key=lambda x: x['Adalet Puanı (Fark)'])

    print("--- Aday Mekan Karşılaştırma Tablosu ---")
    for s in sonuclar:
        print(f"Mekan: {s['Mekan Adı']:<25} | Süreler: {s['Süreler (dk)']} | Fark: {s['Adalet Puanı (Fark)']:<5} dk")
    
    if sonuclar:
        en_iyi = sonuclar[0]
        print("\n" + "="*50)
        print(f"🏆 EN ADİL BULUŞMA NOKTASI: **{en_iyi['Mekan Adı']}**")
        print(f"Fark (Adalet Puanı): {en_iyi['Adalet Puanı (Fark)']} dakika")
        print(f"Yolculuk Süreleri: {en_iyi['Süreler (dk)']} dakika")
        print("="*50)
    else:
        print("Yeterli API sonucu alınamadı. Lütfen API anahtarınızı kontrol edin.")

if __name__ == "__main__":
    main()

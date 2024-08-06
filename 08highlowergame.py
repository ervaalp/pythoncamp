# datasetten A ve B adında 2 tane rastgele data seç +
# A datasının tüm bilgilerini yaz, B datasının takipçi sayısı hariç yüm bilgilerini yaz. +
# Hangisinin takipçisi yüksektir, A or B sor: Doğruysa B ile devam, A yerine başka data getir. Yanlış olana kadar devam et.
# Yanlış olduğunda skor yazdır

import random

data = [
    {'name': 'Ahmet Hamdi Tanpınar', 'book_count': 6, 'famous_work': 'Huzur'},
    {'name': 'Yaşar Kemal', 'book_count': 36, 'famous_work': 'İnce Memed'},
    {'name': 'Sabahattin Ali', 'book_count': 9, 'famous_work': 'Kürk Mantolu Madonna'},
    {'name': 'Orhan Pamuk', 'book_count': 12, 'famous_work': 'Kara Kitap'},
    {'name': 'Halide Edib Adıvar', 'book_count': 21, 'famous_work': 'Sinekli Bakkal'},
    {'name': 'Kemal Tahir', 'book_count': 25, 'famous_work': 'Kurt Kanunu'},
    {'name': 'Nazım Hikmet', 'book_count': 25, 'famous_work': 'Kuvayi Milliye Destanı'},
    {'name': 'Halit Ziya Uşaklıgil', 'book_count': 18, 'famous_work': 'Aşk-ı Memnu'},
    {'name': 'Hüseyin Rahmi Gürpınar', 'book_count': 30, 'famous_work': 'Saraydan Kız Kaçırma'},
    {'name': 'Refik Halit Karay', 'book_count': 25, 'famous_work': 'Kiralık Konak'},
    {'name': 'Ahmet Mithat Efendi', 'book_count': 60, 'famous_work': 'Felatun Bey ile Rakım Efendi'},
    {'name': 'Recaizade Mahmud Ekrem', 'book_count': 10, 'famous_work': 'Araba Sevdası'},
    {'name': 'Süleyman Nazif', 'book_count': 15, 'famous_work': 'İstanbul'},
    {'name': 'Mehmet Rauf', 'book_count': 10, 'famous_work': 'Eylül'},
    {'name': 'Sait Faik Abasıyanık', 'book_count': 15, 'famous_work': 'Kumpanya'},
    {'name': 'Fazıl Hüsnü Dağlarca', 'book_count': 40, 'famous_work': 'Çocuk ve Allah'},
    {'name': 'İsmail Güzelsoy', 'book_count': 8, 'famous_work': 'Aynada Kırık İzdüşümler'},
    {'name': 'İskender Pala', 'book_count': 20, 'famous_work': 'Katre-i Matem'},
    {'name': 'Ayşe Kulin', 'book_count': 30, 'famous_work': 'Adı: Aylin'},
    {'name': 'Ece Temelkuran', 'book_count': 15, 'famous_work': 'Düğümlere Üflemek'},
    {'name': 'Barış Bıçakçı', 'book_count': 8, 'famous_work': 'Küçük Aptallar Cemiyeti'},
    {'name': 'Selim İleri', 'book_count': 25, 'famous_work': 'Gece Yalanları'},
    {'name': 'Aka Gündüz', 'book_count': 12, 'famous_work': 'Beyoğlu Rüzgarları'},
    {'name': 'Orhan Veli Kanık', 'book_count': 7, 'famous_work': 'Karakılçık'},
    {'name': 'Turgut Uyar', 'book_count': 10, 'famous_work': 'Dünyanın En Güzel Arabistanı'},
    {'name': 'Cemil Meriç', 'book_count': 5, 'famous_work': 'Bu Ülke'},
    {'name': 'Muzaffer İzgü', 'book_count': 15, 'famous_work': 'Çocuklar İçin Masallar'},
    {'name': 'Tuna Kiremitçi', 'book_count': 9, 'famous_work': 'Hikayeler'},
    {'name': 'Gülten Dayıoğlu', 'book_count': 25, 'famous_work': 'Fadiş'}
]

A = random.choice(data)
sayac =0

def newdata():
    global B
    B = random.choice([item for item in data if item is not A])  # seçimi a ya eşit olmadan datalardan seç
    Bdict = {'name': B["name"] , 'famous_work': B["famous_work"]}
    return Bdict

def fsonuc():
    if A["famous_work"] >= B["famous_work"]:
        sonuc = "A"
    else:
        sonuc = "B"

    return sonuc

def game():

    global A
    print(A)

    global sayac

    Bdict = newdata()
    # global B
    print(Bdict)

    secim = input(f"Who is more flower? A or B: ")
    sayac += 1
    if secim == fsonuc():
        print(f"Doğru: {sayac}")
        A = B
        game()
    else:
        print(f"Tekrar deneyiniz, skorunuz: {sayac} ")

game()

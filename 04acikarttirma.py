from replit import clear #çıktıyı temizler.
#başka teklif veren olması durumunda ekranı temizler

d = { }

t = False

def teklifbulma (rekorteklif):
  enyüksekteklif = 0
  kazanan = ""

  for i in rekorteklif:
    yapılanteklif = rekorteklif[i]

    if yapılanteklif > enyüksekteklif:
      enyüksekteklif = yapılanteklif
      kazanan = i

  print(f"{enyüksekteklif} ile kazanan {kazanan}")

while not t:
  name = input("isim giriniz:")
  price = int(input("fiyat giriniz:"))
  d[name] = price

  teklif = str(input("başka teklif veren var mı?"))
  if teklif == "hayır":
    t = True
    teklifbulma(d)

  elif teklif == "evet":
    clear()
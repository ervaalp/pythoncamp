# 3 ayrı liste oluştur sonra bu listeleri birleştir. rastgele x'ler koysun
line1 = ['⬜️','⬜️','⬜️']
line2 = ['⬜️','⬜️','⬜️']
line3 = ['⬜️','⬜️','⬜️']

map = [line1, line2, line3]
# pozisyon bilgisi al:
# harf: satır: 0.indis, sayı: sütun:1.indis
position = input("?:")

letter = position[0].lower()
abc=["a","b","c"]

letter_index = abc.index(letter) #harfin indexini vermiş olacak

number_index = int(position[1]) - 1 #0.indisten başladığı için '-1' dedik

map[letter_index][number_index] = "x"
print(f"{line1}\n{line2}\n{line3}")
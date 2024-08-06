#TODO-1: Giriş olarak 'metin' ve 'shift'i alan 'şifreleme' metotunu oluşturun.
  #TODO-2: 'Şifreleme' fonksiyonu içinde, 'metnin' her harfini alfabedeki kaydırma miktarı kadar ileri kaydırın ve şifrelenmiş metni yazdırın.
  #plain_text = "merhaba", kaydırma = 5, cipher_text = "mjqqt", çıktısı: "Kodlanmış metin mjqqt'tir"
#TODO-3: Şifreleme işlevini çağırın ve kullanıcı girişlerini iletin. Kodu test edebilmeniz ve bir mesajı şifreleyebilmeniz gerekir.

def encrypt(d,t,s):
  final_text = "" #şifrelenmiş mesaj
  s = s % 26

  for letter in t:
    position = alphabet.index(letter)

    if d == "encode":
      new_position = position + s
    elif d == "decode":
      new_position = position - s

    final_text += alphabet[new_position]

  print(f"şifrelenmiş mesaj: {final_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("encode or decode? :\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(d=direction, t=text, s=shift)

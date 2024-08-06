# Sayı tahmin oyunu,
# Bilgisayar random bir sayı tutsun
# Klavyeden 5 giriş hakkı ile sayıyı tahmin etmeye çalış, yüksek/düşük değer ve x hakkınız kaldı şeklinde yazdır. (aradaki farkı da söylet)
# Sayıyı hakları bitmeden tahmin ederse kazandı edemezse yandı.
# ⚡guess=tahmin, counter=sayaç, turns: dönüş

import random

# Kontrol fonksiyonu
def control(guess, number, turns):
  if guess > number:
    print("Too high.")
    return turns - 1
  elif guess < number:
    print("Too low.")
    return turns - 1

# Seviyeye göre hak sayısı
def level():
  level = input("Choose a difficulty, 'easy' or 'hard'? ")
  if level == "easy":
    return 10
  else:
    return 3

# Oyunun ana yapısı:
def game():
  print("Guess numbers between 1-100")
  answer = random.randint(1,100)
  print(answer)

  turns = level() #dönüş sayısını level fonktan al

  guess = 0 #false
  while guess != answer:
    print(f"attempts remaining: {turns}")

    guess = int(input("Make a guess: "))

    turns = control(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

    if guess == answer:
      print("You win!")

game()
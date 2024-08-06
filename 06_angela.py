def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def score(cards):
  if sum(cards) == 21 and len(cards) == 2: #2 kart varsa ve puanı 21 ise bj
    return 0 # 0 bjyi temsil edecek

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score): #compare:karşılaştırma
  if user_score > 21 and computer_score > 21:
    return "User is lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

  def play_game():
      user_cards = []
      computer_cards = []
      is_game_over = False

      for _ in range(2):
          user_cards.append(deal_card())
          computer_cards.append(deal_card())

      while not is_game_over:
          user_score = score(user_cards)
          computer_score = score(computer_cards)
          print(f"   Your cards: {user_cards}, current score: {user_score}")
          print(f"   Computer's first card: {computer_cards[0]}")

          if user_score == 0 or computer_score == 0 or user_score > 21:
              is_game_over = True
          else:
              user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
              if user_should_deal == "y":
                  user_cards.append(deal_card())
              else:
                  is_game_over = True

          while computer_score != 0 and computer_score < 17:
              computer_cards.append(deal_card())
              computer_score = calculate_score(computer_cards)

          print(f"   Your final hand: {user_cards}, final score: {user_score}")
          print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
          print(compare(user_score, computer_score))

  while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
      import os

      if tekrar == "y":
          os.system('cls')
          print("iyi şanslar")
      else:
          print("iyi günler")

      play_game()


# Windows'da konsolu temizlemek için os.system('cls')
# OS MODÜLÜ:
# os Modülü os modülü, Python'da işletim sistemiyle etkileşim kurmanızı sağlayan standart bir modüldür. Bu modül, dosya ve dizin işlemleri, çevre değişkenlerine erişim, sistem komutlarının çalıştırılması gibi çeşitli işlemler için kullanılır.
# os.system Fonksiyonu os.system fonksiyonu, işletim sistemine bir komut göndermek için kullanılır. Bu komut, aynı komutu bir komut satırında yazdığınızda olduğu gibi çalıştırılır. Örneğin, Windows'ta os.system('cls') komutu, komut istemcisini temizler.
# os.name Değişkeni os.name değişkeni, Python'un çalıştığı işletim sistemini tanımlamak için kullanılır. Bu değişken, işletim sisteminin türüne göre farklı değerler alabilir:
# 'nt': Windows işletim sistemleri için kullanılır. 'posix': Unix benzeri işletim sistemleri (Linux, macOS, vb.) için kullanılır. cls ve clear Komutları Windows'ta cls komutu, komut istemcisini temizlemek için kullanılır. Bu komut, komut istemcisindeki tüm metinleri siler ve ekranı temizler. Unix benzeri sistemlerde clear komutu, terminali temizlemek için kullanılır. Bu komut da terminaldeki tüm metinleri siler ve ekranı temizler.

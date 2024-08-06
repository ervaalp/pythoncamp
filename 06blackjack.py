import random
cardlist= ["A",2,3,4,5,6,7,8,9,10,"J","O","K"]
puanlist = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

l = dict(zip(cardlist,puanlist)) # değerlere karşılık gelen puanları hesaplamak için sözlük oluşturmak istedim:l={cardlist:puanlist} şeklinde yapamayız,zip ile eşleştirerek yapabiliriz

kullanıcı = []
bilgisayar = []

for i in range(2):
  newcard = random.choice(cardlist)
  bilgisayar.append(newcard)

for i in range(2):
  newcard = random.choice(cardlist)
  kullanıcı.append(newcard)

print(f"B:{bilgisayar}")
print(f"K:{kullanıcı}")

#
def byenikart():

  for i in range(1):
      newcard = random.choice(cardlist)
      bilgisayar.append(newcard)
  print(f"B:{bilgisayar}")

def kyenikart():
  for i in range(1):
    newcard = random.choice(cardlist)
    kullanıcı.append(newcard)
  print(f"K:{kullanıcı}")

#
def bpuan():
  bilgisayarpuanı = 0

  for i in bilgisayar:
    bilgisayarpuanı += l[i]

    if  sum(bilgisayar) > 21 and "A" in bilgisayar :
        bilgisayarpuanı -=10  # l["A"] = 1 #bu şekilde de olması lazım ?

  return bilgisayarpuanı

def kpuan():
  kullanıcıpuanı = 0

  for i in kullanıcı:
    kullanıcıpuanı = kullanıcıpuanı + l[i]

    if  kullanıcıpuanı > 21 and "A" in kullanıcı :
        kullanıcıpuanı -=10

  return kullanıcıpuanı

def bj():
  if bpuan() == 21:
    print("Bilgisayar blackjack yaptı, kullanıcı kaybetti")
  elif kpuan() == 21:
    print("Kullanıcı blackjack yaptı, bilgisayar kaybetti")
  else:
    print("Devam")

if kpuan() > 21 or bpuan() > 21:
    print("Oyun bitti")
else:
    print("Devam")
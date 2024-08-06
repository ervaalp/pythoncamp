#çizim skor oyunu
# sağ-sol? sağ:game over, sol: yüz ya da bekle
  #yüz:game over, bekle: kapı seç
    # kırmızı ve mavi kapı game over; yeşilkapı: kazandın

print("welcome")
choice1 = input('make your choice? Type" left "or" right').lower()

if choice1=="right":
  print("game over")
else:
  choice2 = input('make your choice? Type" swim "or" wait').lower()
  if choice2 == "swim":
    print("game over")
  else:
    choice3 = input('make your choice? Type" red "or" blue "or" green').lower()
    if(choice3=="red" or choice3=="blue"):
      print("game over")
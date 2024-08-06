year = int(input("Yıl giriniz: "))
month = int(input("Ay giriniz: "))

def artikyil(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def ayin_gun_sayisi(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and artikyil(year):
    return 29
  else:
    return month_days[month - 1]

gün = ayin_gun_sayisi(year, month)
print(gün)
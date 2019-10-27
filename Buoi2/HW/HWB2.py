D = int(input('Nhap vao ngay: '))
M = int(input('Nhap vao thang: '))
Y = int(input('Nhap vao nam: '))

if 2000 <= Y <= 2099:
  existed = True
  if M == 2:
    if (Y % 400 == 0 or (Y % 4 == 0 and  Y % 100 != 0)) and D <= 29:
      existed = True
    else:
      if D > 28:
        existed = False
      else:
        existed = True
  else:
    if (M in [4,6,9,11] and D <= 30):
      existed = True
    elif (M not in [4,6,9,11] and D <= 31):
      existed = True
    else:
      existed = False
else:
  existed = False

print(existed)


# Bai 2
M = float(input('Gia san pham: '))
M1 = float(input('So tien thanh toan tai thoi diem mua: '))
m = float(input('So tien tra gop moi thang: '))
r = float(input('Lai suat mua tra gop: '))
money_left = M - M1
t = 0

while money_left > 0:
    money_left += money_left * r/1200 - m 
    t += 1

print(f"So thang can phai tra la {t}")

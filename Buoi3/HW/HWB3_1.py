# Bai 1
a = [10, 3, 1, 5, 0, 8]
N = int(input("Nhap so N: "))
S = 0
K = -1

while S <= N:
    K += 1
    if K > len(a) - 1:
        break
    else:
        S += a[K]
print(K if K <= len(a) - 1 else "Khong ton tai")


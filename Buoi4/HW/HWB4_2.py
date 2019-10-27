s1 = input("Chuoi 1: ")
s2 = input("Chuoi 2: ")

for i in range(len(s1)):
    if s1[i] != s2[i]:
        print(i)
        break

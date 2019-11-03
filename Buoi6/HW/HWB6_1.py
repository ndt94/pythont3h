def arr_to_set(arr):
    arr = arr.split(" ")
    s = set()
    for x in arr:
        s.add(str(x))
    return s


def bai6(s1, s2):
    I = s1.intersection(s2)
    U = s1.union(s2)
    result = len(I) / len(U)
    return result


a = input("Cau van 1:")
b = input("Cau van 2:")
s1 = arr_to_set(a)
s2 = arr_to_set(b)

print("Muc do giong nhau cua 2 cau van la:", bai6(s1, s2))

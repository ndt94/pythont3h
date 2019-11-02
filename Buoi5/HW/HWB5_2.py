products = [
    ("P1", 1, 10000),
    ("P2", 2, 15000),
    ("P3", 3, 20000),
    ("P2", 1, 15000),
    ("P1", 2, 10000),
]

products = sorted(products, reverse=True, key=lambda p: p[1] * p[2])
print(products)

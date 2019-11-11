import base64

with open('brand.png', 'rb') as f:
    data = f.read()

# print(data.__class__)
# print(len(data))

b64data = base64.b64encode(data)
# print(len(b64data))

with open('data.txt', 'wb') as f:
    f.write(b64data)
import base64

with open('data.txt') as f:
    data = f.read()

b64data = base64.b64decode(data)
# print(len(b64data))

with open('test.png', 'w') as f:
    f.write(b64data)
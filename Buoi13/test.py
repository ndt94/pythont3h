import os
dir = '/home/jessenguyen/Downloads'
items = os.listdir(dir)
for item in items:
    path = os.path.join(dir, item)
    print(item, 'la thu muc') if not os.path.isfile(path) else ""
    print(item, 'la file') if os.path.isfile(path) else ""
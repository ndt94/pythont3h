import sys
if len(sys.argv) != 3:
    print('Usage: python copy.py <src_path> <dst_path>')
    exit()

src = sys.argv[1]
dst = sys.argv[2]

import os
if not os.path.exists(src):
    print('File not found:', src)
    exit()

with open(src, 'rb') as f: data = f.read()
with open(dst, 'wb') as f: f.write(data)
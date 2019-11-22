import json
import base64

with open('students.json') as f:
    data = json.load(f)

for student in data:
    with open(student['studentId'] + '.jpg', 'wb') as f:
        f.write(base64.b64decode(student['image']))



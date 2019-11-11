import json


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address


persons = [Person("Nguyen Van A", "Ha Noi"), Person("Nguyen Van B", "TP HCM")]

lst = []
for p in persons:
    lst.append({"name": p.name, "address": p.address})

with open("data.json", "w") as f:
    f.write(json.dumps(lst))
    # json.dump(lst, f)

import json


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address


with open("data.json") as f:
    lst = json.loads(f.read())
    # lst = json.load(f)

person = []

for item in lst:
    name = item["name"]
    address = item["address"]
    person.append(Person(name, address))

for p in person:
    print(p.name, p.address)
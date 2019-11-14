import json
import csv

with open('products.json') as f:
    data = json.load(f)

with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['code', 'name', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
import csv
import MySQLdb

host = '172.17.0.2'
username = 'test'
password = 'abc@123'
db_name = 'trung_db'

conn = MySQLdb.connect(host, username, password, db_name, charset='utf8')
cursor = conn.cursor()
with open('category.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    arr = list(reader)
    for row in arr:
        cursor.execute(
            "INSERT INTO category(id, parent_id, name) VALUES (%s, %s, %s)",
            (row[0], row[1], row[2].strip())
        )
conn.commit()

with open('product.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    arr = list(reader)
    for row in arr:
        cursor.execute(
            "INSERT INTO product(id, category_id, name, price) VALUES (%s, %s, %s, %s)",
            (row[0], row[1], row[2].strip(), row[3])
        )
conn.commit()
import MySQLdb
host = '172.17.0.2'
username = 'test'
password = 'abc@123'
db_name = 'trung_db'

conn = MySQLdb.connect(host, username, password, db_name, charset='utf8')
cursor = conn.cursor()

students = [
    ('1001', 'Nguyễn Văn A', 'Hà Nội', 7.0),
    ('1002', 'Nguyễn Văn B', 'TP.HCM', 8.0)
]

for st in students:
    cursor.execute('''INSERT INTO student(student_no, name, address, gpa)
    VALUES(%s,%s,%s,%s)
    ''',
    (st[0], st[1], st[2], st[3]))

conn.commit()
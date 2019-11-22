import MySQLdb
host = '172.17.0.2'
username = 'test'
password = 'abc@123'
db_name = 'trung_db'

conn = MySQLdb.connect(host, username, password, db_name, charset='utf8')
# print('Connected to database server')

#id = '100 OR 1=1'
#sql = 'SELECT * FROM student WHERE id=' + id
cursor = conn.cursor()
cursor.execute('SELECT * FROM student WHERE gpa>=7.0')
rows = cursor.fetchall()
for row in rows:
    print(row)


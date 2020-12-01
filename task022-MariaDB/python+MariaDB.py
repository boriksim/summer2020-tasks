import mariadb as mdb
import random


abc = "abcdefghijklmnopqrstuvwxyz"

conn = mdb.connect(
    user="root",
    password="",
    host="127.0.0.1",
    port=3306,
    database="classmates"
)
cur = conn.cursor(dictionary=True)

cur.execute("truncate users")

for i in range(10):
    rword = ""
    for j in range(random.randint(2, 15)):
        rword += abc[random.randint(0, 25)]

    rint = random.randint(0, 100)
    string = F"insert into users (name, age) values (\"{rword}\", {rint});"
    cur.execute(string)

cur.execute("select count(*) from users")
print(cur.fetchone())

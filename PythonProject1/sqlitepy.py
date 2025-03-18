import sqlite3
conn=sqlite3.connect("staff.db")
cursor=conn.cursor()
# cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS staff(
#                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                 NAME TEXT NOT NULL,
#                 AGE INTEGER,
#                 ADDRESS TEXT,
#                 SALARY REAL
#                 )''')
# print("Table created successfully")
# cursor.executemany("INSERT INTO staff(NAME,AGE,ADDRESS,SALARY)VALUES(?,?,?,?)",[
#     ('Raj',22,'Trichy',23000),
#     ('Saj',32,'Madurai',23400),
#     ('Taj',32,'Trichy',23000),
#     ('Maj',42,'Trichy',23500),
#     ('Rhaj',53,'Chennai',24000)
# ])
# cursor.execute("UPDATE staff SET NAME='Ravi',AGE=33,ADDRESS='Mayiladuthurai',SALARY=25000 WHERE ID=16")
# cursor.execute("UPDATE staff SET STAFF_ID=101 WHERE ID=1")
# cursor.execute("UPDATE staff SET STAFF_ID=102 WHERE ID=4")
# cursor.execute("UPDATE staff SET STAFF_ID=103 WHERE ID=5")
# cursor.execute("UPDATE staff SET STAFF_ID=104 WHERE ID=6")
# cursor.execute("UPDATE staff SET STAFF_ID=105 WHERE ID=7")
# cursor.execute("UPDATE staff SET STAFF_ID=106 WHERE ID=8")
# cursor.execute("UPDATE staff SET STAFF_ID=107 WHERE ID=9")
# cursor.execute("UPDATE staff SET STAFF_ID=108 WHERE ID=15")
# cursor.execute("UPDATE staff SET STAFF_ID=111 WHERE ID=18")
# cursor.execute("UPDATE staff SET STAFF_ID=112 WHERE ID=19")
# cursor.execute("UPDATE staff SET STAFF_ID=113 WHERE ID=20")
# cursor.execute("UPDATE staff SET STAFF_ID=109 WHERE ID=16")
# cursor.execute("UPDATE staff SET STAFF_ID=110 WHERE ID=17")
# print("Table updated")
#cursor.execute("DELETE FROM staff WHERE AGE=32")
# cursor.execute("DELETE FROM staff WHERE ID=13 OR ID=14")
#cursor.execute("DELETE FROM staff WHERE ID IN(19,20)")
# print("Id Deleted")
#cursor.execute("SELECT ID,NAME,AGE FROM staff WHERE SALARY<24000")
#cursor.execute("SELECT ID,NAME,SALARY FROM staff WHERE SALARY<=24000")
#cursor.execute("ALTER TABLE staff ADD STAFF_ID INTEGER")
#cursor.executemany("INSERT INTO staff(STAFF_ID)VALUE(?)",[])
conn.commit()
cursor.execute("SELECT*FROM staff")
students=cursor.fetchall()
for std in students:
    print(std)
#print(students)
conn.close()
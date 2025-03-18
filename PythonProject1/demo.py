# print("ji")
# print("Nallas")
# a=10
# b=30
# print(a+b)
# SQL server conection
# import sqlite3
# conn=sqlite3.connect("student.db")
# cursor=conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS student(
#                ID INTEGER PRIMARY KEY
#                 AUTOINCREMENT,
#                 NAME TEXT NOT NULL,
#                 AGE INTEGER,
#                 ADDRESS TEXT,
#                 SALARY REAL
# )
# ''')
# print("table created")
# cursor.execute("INSERT INTO student(NAME,AGE,ADDRESS,SALARY)VALUES(?,?,?,?)",('Raj',22,'Trichy',23000))
# cursor.execute("INSERT INTO student(NAME,AGE,ADDRESS,SALARY)VALUES(?,?,?,?)",('Saj',32,'Madurai',23400))
# cursor.execute("INSERT INTO student(NAME,AGE,ADDRESS,SALARY)VALUES(?,?,?,?)",('Taj',32,'Trichy',23000))
# cursor.execute("INSERT INTO student(NAME,AGE,ADDRESS,SALARY)VALUES(?,?,?,?)",('Maj',42,'Trichy',23000))
# cursor.execute("INSERT INTO student(NAME,AGE,ADDRESS,SALARY)VALUES(?,?,?,?)",('Rhaj',52,'Trichy',23000))
# # cursor.execute("UPDATE student SET NAME='Vicky',AGE=33,ADDRESS='Mayiladuthurai',SALARY=24000 WHERE ID=1")
# # cursor.execute("DELETE FROM student WHERE AGE=33")
# conn.commit()
# cursor.execute('select*from student')
# a=cursor.fetchall()
# for row in a:
#  print(row)
# # print(a)
# conn.close()

#select query
# import sqlite3
# conn=sqlite3.connect("student.db")
# curses=conn.cursor()
# curses.execute("SELECT*FROM student")
# rows=curses.fetchall()
# for row in rows:
#  print(row)
# conn.close()
#update query
import sqlite3
conn=sqlite3.connect("student.db")
curses=conn.cursor()
curses.execute('''UPDATE student
                SET NAME='vicky',AGE=33,ADDRESS='Mayiladuthurai',SALARY=23500 
                WHERE ID=1''')
conn.commit()
curses.execute("SELECT*FROM student")
c=curses.fetchall()
print(c)
conn.close()
print("Record update successfully")
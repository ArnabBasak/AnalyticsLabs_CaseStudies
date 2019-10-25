import sqlite3
conn = sqlite3.connect('practice.db')
cursor = conn.cursor()
cursor.execute("""INSERT OR IGNORE INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES
              (1,'ARNAB',28,'NAGPUR',200000.0)""")
cursor.execute("""INSERT OR IGNORE INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES
              (2,'RAHUL',27,'BANGALORE',500000.0)""")
cursor.execute("""INSERT OR IGNORE INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES
              (3,'RAJ',30,'MUMBAI',100000.0)""")
cursor.execute("""INSERT OR IGNORE INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES
              (4,'VIKRAM',22,'PUNE',250000.0)""")
cursor.execute("select count(*) From employees")
value = cursor.fetchone()[0]
print(value)
if value == 4:
    print('records inserted successfully')
else:
    print('records not inserted properly please check')
conn.commit()
conn.close()

#This program will check if the tables exists or not
#importing sqlite api
import sqlite3
#creating the connection
conn = sqlite3.connect('practice.db')
#creating the cursor
cursor = conn.cursor()
#executing the cursor
cursor.execute("""select count(name) from sqlite_master where type =  'table' and name like 'employees'""")
#getting the value in the integer format
table_value  = cursor.fetchone()[0]
#comparing it
if table_value == 1:
    print('table exists')
else:
    print('table does not exists')
conn.commit()
conn.close()


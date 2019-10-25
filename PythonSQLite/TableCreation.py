#this program is to connect to the database and create a table
#importing the database
import sqlite3
#creating a connection
conn = sqlite3.connect('practice.db')
#checking if the databse is connected or not
print('Db opened successfully')
#executing a query to create a table the query will execute successfully even if table exists
conn.execute("""create table if not exists employees 
            (ID INT PRIMARY KEY  NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL,
            ADDRESS CHAR(50),
            SALARY REAL);""")
#printing the note to check if the table is created or not
print("table created successfully")
#closing the connection
conn.close()
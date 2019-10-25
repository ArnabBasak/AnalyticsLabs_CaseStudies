#This program is to see how many tables are present in a perticular database
#importing sqlite api
import sqlite3
#connecting to the practice database
conn = sqlite3.connect('practice.db')
#creating a cursor so that we can execute query on the database
cursor = conn.cursor()
#executing the query
cursor.execute("""select name from sqlite_master where type = 'table'""")
#printing the result the fetchall() function returns a list with the table names
print(cursor.fetchall())
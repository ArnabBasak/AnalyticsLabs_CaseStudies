import sqlite3
conn = sqlite3.connect('practice.db')
data = conn.execute('select * from employees')
for element in data.fetchall():
    print('ID: ',element[0])
    print('NAME: ',element[1])
    print('AGE: ',element[2])
    print('ADDRESS: ',element[3])
    print('SALARY: ',element[4])
import mysql.connector as connector
import myloginpath
import os
from pprint import pprint as pp

option_file=os.path.expanduser('~/.mylogin.cnf')
option_file_section='client'

conf = myloginpath.parse(login_path=option_file_section, path=option_file)
cnx = connector.connect(user=conf['user'], password=conf['password'], database='stamps')

cursor = cnx.cursor()
default_sql = "SELECT * from Sets"
input_sql = input("What is your SQL statement ? [default: SELECT * from Sets]")
cursor.execute(input_sql or default_sql)

print(cursor.column_names)
[print(row) for row in cursor]

cursor.close()
cnx.close()


''' 
I found this in the internet
 pip install myloginpath worked 

import myloginpath
import pymysql
conf = myloginpath.parse('client')
db = pymysql.connect(**conf, host='mydbhost', db='whatever')
#https://stackoverflow.com/questions/36345273/connecting-python-to-mysql-using-an-encrypted-option-file
'''
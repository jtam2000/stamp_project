import mysql.connector as connector
import myloginpath
import os


option_file=os.path.expanduser('~/.mylogin.cnf')
conf = myloginpath.parse(login_path='client', path=option_file)

cnx = connector.connect(user=conf['user'], password=conf['password'], database='stamps')
cursor = cnx.cursor()
query = ("SELECT * from Sets")

cursor.execute(query)
for row in cursor:
  print(row)

cursor.close()


''' 
I found this in the internet
 pip install myloginpath worked 

import myloginpath
import pymysql
conf = myloginpath.parse('client')
db = pymysql.connect(**conf, host='mydbhost', db='whatever')
#https://stackoverflow.com/questions/36345273/connecting-python-to-mysql-using-an-encrypted-option-file
'''
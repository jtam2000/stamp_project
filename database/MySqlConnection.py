import mysql.connector as connector
import myloginpath
import os
from database.MySqlOptionalFile import MySqlOptionalFile


class DatabaseConnection:
    """
        This connects to the MySql database using the user's Optional file
        then you can
            1.  connect_to_db()
            2. execute_sql(sql_string)
            3. print_sql_result()
    """

    def __init__(self, config_file: MySqlOptionalFile):
        self.MySqlConfigFile = config_file
        self.connection = None
        self.query_results = None

    def connect_to_db(self, set_results=True):
        conf = self.MySqlConfigFile.get_config()
        self.connection = connector.connect(user=conf['user'],
                                            password=conf['password'],
                                            database=conf['database'])
        if set_results:
            self.query_results = self.connection.cursor()

    def execute_sql(self, sql: str):
        self.connect_to_db()
        print("executing the sql: ", sql)
        self.query_results.execute(sql)

    def get_sql_results(self):
        return self.query_results

    def print_sql_result(self):
        [print(row) for row in self.get_sql_results()]

    @staticmethod
    def sample_connection(sql: str = "SELECT * from Sets"):
        db = DatabaseConnection(MySqlOptionalFile())
        db.execute_sql(sql)
        db.print_sql_result()

    @staticmethod
    def sample_connection_long_form():
        option_file = os.path.expanduser('~/.mylogin.cnf')
        option_file_section = 'client'

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

        country_view = CountryInventory()
        print(country_view.get_columns())


DatabaseConnection.sample_connection("SELECT * FROM vw_country_inventory")

''' 
Information regarding decoding of the option_file from mysql set up for the user:
#https://stackoverflow.com/questions/36345273/connecting-python-to-mysql-using-an-encrypted-option-file

I found this in the internet
 pip install myloginpath worked 

import myloginpath
import pymysql
conf = myloginpath.parse('client')
db = pymysql.connect(**conf, host='mydbhost', db='whatever')

'''

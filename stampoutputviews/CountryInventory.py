from database.MySqlOptionalFile import MySqlOptionalFile
from database.MySqlConnection import DatabaseConnection
from mysql.connector import cursor


class CountryInventory:
    database_view = 'vw_country_inventory'

    def __init__(self):
        self.config = MySqlOptionalFile()
        self.mysql_cnx = DatabaseConnection(self.config)

    def print_view(self):
        self.mysql_cnx.execute_sql("select * from " + self.database_view)
        self.mysql_cnx.print_sql_result()

    def get_columns(self):
        return self.mysql_cnx.execute_sql("select * from " + self.database_view).column_names

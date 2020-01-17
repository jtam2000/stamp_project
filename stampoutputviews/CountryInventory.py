from database.MySqlOptionalFile import MySqlOptionalFile
from database.MySqlConnection import DatabaseConnection


class CountryInventory:
    database_view = 'vw_country_inventory'

    def __init__(self):
        self.config = MySqlOptionalFile()
        self.mysql_cnx = DatabaseConnection(self.config)

    def print_view(self):
        self.mysql_cnx.execute_sql("select * from ".join(self.database_view))
        self.mysql_cnx.print_sql_result()

    def get_columns(self):
        return ["Country:",
                "Stock_Count",
                "Year",
                "Set_Name",
                "Set",
                "Cardinality",
                "Member",
                "Member_Name",
                "Face_Value",
                "FV_Denom",
                ]


#CountryInventory().print_view()

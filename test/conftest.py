import pytest
from stampoutputviews.CountryInventory import CountryInventory
from database.MySqlOptionalFile import MySqlOptionalFile
from database.MySqlConnection import DatabaseConnection


@pytest.fixture(scope="session")
def __cnx_config_file():
    """
        pytest fixture: parse the mysql optional file
    """

    option_file = MySqlOptionalFile(optional_file='~/.mylogin.cnf',
                                    file_section='client',
                                    use_db='stamps')
    return option_file


@pytest.fixture(scope="session")
def __cnx_config(__cnx_config_file):
    """
        pytest fixture: parse the user's optional file for MySql
    """
    return __cnx_config_file.get_config()


@pytest.fixture(scope="session")
def __stamp_db_connection(__cnx_config_file):
    """
        pytest fixture: a default connection to the database
    """
    return DatabaseConnection(__cnx_config_file)


@pytest.fixture(scope="session")
def __stamp_db_cursor(__stamp_db_connection):
    """
    pytest fixture: a default cursor to the database
    """

    pass


@pytest.fixture(scope="session")
def __country_inventory_data():
    return CountryInventory()

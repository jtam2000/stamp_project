import mysql.connector as connector
import myloginpath
import os
import pytest
from stampoutputviews.CountryInventory import CountryInventory
from database.MySqlOptionalFile import MySqlOptionalFile


@pytest.fixture(scope="session")
def __cnx_config_test_param():
    """
        pytest fixture: The parameters used for MySql Connection configuration
    """

    params = {}
    params.update(optional_file=os.path.expanduser('~/.mylogin.cnf'))
    params.update(option_file_section="client")
    params.update(database="stamps")

    option_file = MySqlOptionalFile()
    return params


@pytest.fixture(scope="session")
def __cnx_config(__cnx_config_test_param):
    """
        pytest fixture: parse the user's optional file for MySql
    """
    optional_file = __cnx_config_test_param["optional_file"]
    file_section = __cnx_config_test_param["option_file_section"]
    database = __cnx_config_test_param["database"]

    # parse the optional file
    config = myloginpath.parse(path=optional_file, login_path=file_section)
    config.update(database=database)
    return config


@pytest.fixture(scope="session")
def __stamp_db_connection(__cnx_config):
    """
        pytest fixture: a default connection to the database
    """

    connection = connector.connect(user=__cnx_config['user'],
                                   password=__cnx_config['password'],
                                   database=__cnx_config["database"])
    yield connection
    connection.close()


@pytest.fixture(scope="session")
def __stamp_db_cursor(__stamp_db_connection):
    """
    pytest fixture: a default cursor to the database
    """
    cursor = __stamp_db_connection.cursor()
    yield cursor


@pytest.fixture(scope="session")
def __country_inventory_data():
    return CountryInventory()

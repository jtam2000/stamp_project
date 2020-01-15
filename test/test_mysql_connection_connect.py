import mysql.connector as connector


def test_connection_optional_file_is_parsable(__cnx_config):

    """
        test1: make sure that the optional file for mysql is parsable using myloginpath library
    """
    assert __cnx_config


def test_connection_optional_file_has_user(__cnx_config):

    """
        test2: make sure optional file defines mysql "user"
    """
    assert __cnx_config['user']


def test_connection_optional_file_has_password(__cnx_config):

    """
        test3: make sure optional file defines mysql "password"
    """
    assert __cnx_config['password']


def test_mysql_connector_connection(__cnx_config):
    """
        test4: make sure connection the database is possible using MySql Optional file parameters
    """
    cnx = connector.connect(user=__cnx_config['user'],
                            password=__cnx_config['password'],
                            database=__cnx_config["database"])

    assert cnx



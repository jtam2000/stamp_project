def test_stamps_table_is_selectable(__stamp_db_cursor):
    """
        pytest: make sure you can select from the Stamps table
    """
    cursor = __stamp_db_cursor
    sql = "SELECT * from Stamps"
    cursor.execute(sql)
    assert cursor.fetchone()

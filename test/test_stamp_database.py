def test_stamps_table_is_selectable(__stamp_db_cursor):
    """
        pytest: make sure you can select from the Stamps table
    """
    __stamp_db_cursor.execute("SELECT * from Sets")
    assert __stamp_db_cursor.fetchone()

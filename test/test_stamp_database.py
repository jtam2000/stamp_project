def test_stamps_table_is_selectable(__stamp_db_connection):
    """
        pytest: make sure you can select from the Stamps table
    """
    cursor_result = __stamp_db_connection.execute_sql("SELECT * from Sets")
    assert cursor_result.fetchone()

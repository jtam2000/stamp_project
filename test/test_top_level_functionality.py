def test_country_inventory_has_required_columns(__country_inventory_data):

    required_columns = ["Country:",
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
    assert __country_inventory_data.get_columns() == required_columns


def test_print_collection_valuation():
    pass


def test_print_inventory_annotation():
    pass

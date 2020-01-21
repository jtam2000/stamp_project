import pytest


@pytest.mark.core
def test_country_inventory_has_required_columns(__country_inventory_data):

    required_columns = ("Country",
                        "Stock_Count",
                        "Year",
                        "Set_Name",
                        "Set_ID",
                        "Cardinality",
                        "Member_ID",
                        "Member_Name",
                        "Face_Value",
                        "FV_Denom",
                        )
    assert __country_inventory_data.get_columns() == required_columns


@pytest.mark.wip
def test_this_test_is_marked_as_wip():
    print("running a test marked as wip")
    pass


def test_print_collection_valuation():
    pass


def test_print_inventory_annotation():
    pass

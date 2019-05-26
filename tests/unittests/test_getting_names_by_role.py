import pytest


@pytest.fixture(params=["manager", "salesman"])
def param_test(request):
    return request.param


def test_getting_names_by_role_positive(param_test, mocked__cafe_db__select_as_list):
    cafe_db_obj, list_of_names = mocked__cafe_db__select_as_list
    names = cafe_db_obj.get_names_by_role(param_test)
    assert names == list_of_names


def test_getting_names_by_role_negative(mocked__cafe_db__select_as_list):
    cafe_db_obj, _ = mocked__cafe_db__select_as_list
    with pytest.raises(KeyError):
        cafe_db_obj.get_names_by_role("incorrect_role")
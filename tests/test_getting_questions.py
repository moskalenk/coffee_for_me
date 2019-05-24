from db.cafe_db import CafeDB
from questions import get_questions
import pytest


def test_questions_for_salesman(create_salesman_object):
    salesman_role = create_salesman_object
    func = get_questions(salesman_role)
    assert callable(func) and func.__name__ == "salesman_questions"


def test_no_questions_for_manager(create_manager_object):
    manager_role = create_manager_object
    with pytest.raises(NotImplementedError):
        get_questions(manager_role)


@pytest.fixture(scope="function", params=["manager", "salesman"])
def param_test(request):
    return request.param


def test_getting_names_by_role_positive(param_test, mocked__cafe_db__select_as_list):
    cafe_db, list_of_names = mocked__cafe_db__select_as_list
    names = cafe_db.get_names_by_role(param_test)
    assert names == list_of_names


def test_getting_names_by_role_negative(mocked__cafe_db__select_as_list):
    cafe_db, _ = mocked__cafe_db__select_as_list
    with pytest.raises(KeyError):
        cafe_db.get_names_by_role("incorrect_role")

def test_sda(belonging_name_to_role):
    processing_service = belonging_name_to_role
    processing_service.check_belonging_name_to_role("Het", "manager")
    assert True

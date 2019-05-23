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



@pytest.fixture()
def names_list(mocker):
    mocker.patch.object(CafeDB, "select_as_list")
    CafeDB.select_as_list.return_value = ["lisa", "Bob"]
    cafe_db = CafeDB("None")
    return cafe_db


@pytest.fixture(scope="function", params=["manager", "salesman", "incorrect_role"])
def param_test(request):
    return request.param

def test_getting_names_by_role(param_test, names_list):
    cafe_db = names_list
    res = cafe_db.get_names_by_role(param_test)
    print(res)

def test_sda(belonging_name_to_role):
    processing_service = belonging_name_to_role
    processing_service.check_belonging_name_to_role("Bob", "manager")
    assert True
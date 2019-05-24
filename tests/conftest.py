import pytest

from db.cafe_db import CafeDB
from roles import Salesman, Manager


@pytest.fixture()
def create_salesman_object():
    return Salesman(name="Bob")


@pytest.fixture()
def create_manager_object():
    return Manager(name="Garry")


@pytest.fixture()
def mocked__cafe_db__select_as_list(mocker):
    list_of_names = ["lisa", "Bob"]
    mocker.patch.object(CafeDB, "select_as_list")
    CafeDB.select_as_list.return_value = list_of_names
    cafe_db = CafeDB("test_db_coffee.db")
    return cafe_db, list_of_names

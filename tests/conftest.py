import pytest

from db.connection import DBConnection
from roles import Salesman, Manager


@pytest.fixture()
def create_salesman_object():
    return Salesman(name="Bob")


@pytest.fixture()
def create_manager_object():
    return Manager(name="Garry")


# @pytest.fixture()
# def names_list(mocker):
#     mocker.patch.object(DBConnection, "select_as_list")
#     mocker.select_as_list.return_value(["lisa", "Bob"])


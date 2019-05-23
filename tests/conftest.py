import pytest

from db.cafe_db import CafeDB
from db.connection import DBConnection
from roles import Salesman, Manager
from services.processing_service import ProcessingService


@pytest.fixture()
def create_salesman_object():
    return Salesman(name="Bob")


@pytest.fixture()
def create_manager_object():
    return Manager(name="Garry")



@pytest.fixture()
def belonging_name_to_role(mocker):
    names_list = ["lisa", "Bob"]
    mocker.patch.object(CafeDB, "get_names_by_role")
    CafeDB.get_names_by_role.return_value = names_list
    processing_service = ProcessingService("None")
    return processing_service

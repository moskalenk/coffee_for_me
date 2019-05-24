import pytest

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
    names_list = ["lisa", "Bob", "Het"]

    mocked_cafe_db = mocker.patch('db.cafe_db.CafeDB')
    mocked_cafe_db.return_value.get_names_by_role.return_value = names_list

    cafe_db = mocked_cafe_db()
    processing_service = ProcessingService(cafe_db)

    return processing_service

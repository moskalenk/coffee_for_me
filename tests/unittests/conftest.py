import pytest

from db.cafe_db import CafeDB
from db.connection import DBConnection
from roles import Salesman, Manager
from services.processing_service import ProcessingService
from services.reporting_service import ReportingService


@pytest.fixture()
def create_salesman_object():
    return Salesman(name="Bob")


@pytest.fixture()
def create_manager_object():
    return Manager(name="Garry")


@pytest.fixture()
def mocked__cafe_db__select_as_list(mocker):
    list_of_names = ["lisa", "Bob"]

    mocker.patch.object(DBConnection, "__init__", lambda db_name: None)
    mocker.patch.object(CafeDB, "select_as_list")
    CafeDB.select_as_list.return_value = list_of_names
    cafe_db_obj = CafeDB()
    return cafe_db_obj, list_of_names


@pytest.fixture()
def belonging_name_to_role(mocker):
    names_list = ["lisa", "Bob", "Het"]

    mocked_cafe_db = mocker.patch('db.cafe_db.CafeDB')
    mocked_cafe_db.return_value.get_names_by_role.return_value = names_list

    cafe_db = mocked_cafe_db()
    processing_service = ProcessingService(cafe_db)

    return processing_service


@pytest.fixture()
def show_common_report_mocker(mocker):
    create_summary_table_mocker = mocker.patch.object(ReportingService, "_create_summary_table")
    text_for_print = create_summary_table_mocker.return_value = "common report here"
    mocker.patch.object(ReportingService, "__init__", lambda cafe_db: None)
    reporting_service_obj = ReportingService()
    return reporting_service_obj, text_for_print

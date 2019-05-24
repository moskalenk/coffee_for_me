from questions import get_questions
import pytest

# ---------------------------------------------
from services.reporting_service import ReportingService


def test_questions_for_salesman(create_salesman_object):
    salesman_role = create_salesman_object
    func = get_questions(salesman_role)
    assert callable(func) and func.__name__ == "salesman_questions"


def test_no_questions_for_manager(create_manager_object):
    manager_role = create_manager_object
    with pytest.raises(NotImplementedError):
        get_questions(manager_role)

# ---------------------------------------------
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

# -------------------------------------------
def test_belonging_name_to_role_positive(belonging_name_to_role):
    processing_service = belonging_name_to_role
    processing_service.check_belonging_name_to_role("Het", "manager")
    assert True


def test_belonging_name_to_role_negative(belonging_name_to_role):
    processing_service = belonging_name_to_role
    with pytest.raises(NameError):
        processing_service.check_belonging_name_to_role("incorrect_name", "manager")

def test_common_report(capsys, show_common_report_mocker):
    reporting_service_obj, text_for_print = show_common_report_mocker
    reporting_service_obj.show_common_report()
    out_flow = capsys.readouterr().out.rstrip()
    assert out_flow == text_for_print

def test_show_bill(capsys):
    text_for_print = "bill here"
    ReportingService.show_bill(text_for_print)
    out_flow = capsys.readouterr().out.rstrip()
    assert out_flow == text_for_print

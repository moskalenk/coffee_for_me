from questions import get_questions
import pytest


def test_questions_for_salesman(create_salesman_object):
    salesman_obj = create_salesman_object
    func = get_questions(salesman_obj)
    assert callable(func) and func.__name__ == "salesman_questions"


def test_no_questions_for_manager(create_manager_object):
    manager_obj = create_manager_object
    with pytest.raises(NotImplementedError):
        get_questions(manager_obj)

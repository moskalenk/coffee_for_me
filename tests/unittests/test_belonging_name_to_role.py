import pytest


def test_belonging_name_to_role_positive(belonging_name_to_role):
    processing_service = belonging_name_to_role
    processing_service.check_belonging_name_to_role("Het", "manager")
    assert True


def test_belonging_name_to_role_negative(belonging_name_to_role):
    processing_service = belonging_name_to_role
    with pytest.raises(NameError):
        processing_service.check_belonging_name_to_role("incorrect_name", "manager")
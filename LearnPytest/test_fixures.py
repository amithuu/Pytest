import pytest


# @pytest.fixture()
def setUp():
    print("Login")
    print("click on take assesment")
    print("back to dashboard")


# """As we are using setup here beacuse the setup is an function which can assessed my all the other function,
# so were ever import that function the function first runs the setUp and runs the imported function"""
def test_viewreport(setUp):
    print("navigate through all Reports and subsciprtion part")


# """As we are using setup here beacuse the setup is an function which can assessed my all the other function,
# so were ever import that function the function first runs the setUp and runs the imported function"""
def test_buildresume(setUp):
    print("navigate through all forms and filling the deatils")



# Yeild and fixtures..!!!!!!!!!!!
@pytest.fixture
def setUp():
    print("Login")
    print("click on take assesment")
    print("back to dashboard")

    # """here yield is like if u want to run any programme after the main programme runs, we use yield."""

    yield
    print("click on edit projects")
    print("add all the items to profile and save")


def test_viewreport(setUp):
    print("navigate through all Reports and subsciprtion part")


def test_buildresume(setUp):
    print("navigate through all forms and filling the deatils")

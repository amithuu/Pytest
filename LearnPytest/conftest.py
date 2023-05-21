import pytest


@pytest.fixture(scope="session",autouse=True)
def tc_setUp():
    print("Login")
    print("click on take assesment")
    print("back to dashboard")
    yield
    print("click on forms and save details")
    print(" click on next or back button ")

# this is the file where we can use this method in all other files. just by adding the function name on it.

# Scope is that how many time and where and all the setup function has to run.

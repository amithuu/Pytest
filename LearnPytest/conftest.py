import pytest


@pytest.fixture(scope="session", autouse=True)
def tc_setUp(browser):
    if browser == "chrome":
        print("Login")
    elif browser == "ff":
        print("click on take assessment")
    else:
        print("back to dashboard")
    yield
    print("click on forms and save details")
    print(" click on next or back button ")


# this is the file where we can use this method in all other files. just by adding the function name on it.

# Scope is that how-many times and where and all the setup function has to run.

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getaoption("--browser")

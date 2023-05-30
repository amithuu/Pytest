import pytest


def to_setUp(browser):
    if browser == "chrome":
        print("login")
        print("using browser")

    yield
    print("log-off")


""" In the below method, which gets the parameter that we are passed in the command prompt."""
"""[ pytest --browser chrome ]"""


def pytest_addoption(parser):
    parser.addoption("--browser")


""" A method which returns the browser type chrome/ff/edge"""


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")






import pytest

"""Here the a and b are the parameter we can send for a single scenarios 
            [like for login we can send valid and invalid parameter]"""


@pytest.fixture(params=["a","b"])
def demo_fixture(request):
    print(request.param)


"""This is an another Type where we can pass argument/parameters in function
    Then it collects by function body and Calculates in a loop"""


@pytest.mark.parametrize("a, b, Sum", [(1, 2, 7), (2, 4, 6), (5, 5, 10), (5, 6, 12)])
def testAdd(a, b, Sum):
    assert a + b == sum


def testLogin(demo_fixture):
    print("login successfully")

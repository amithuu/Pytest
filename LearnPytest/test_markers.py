import pytest
def testLogin():
    print("Login Successful")

@pytest.mark.skip
def testLogoff():
    print("Logoff Successful")
@pytest.mark.xfail
def testCalculation():
    assert 2+2 == 4

@pytest.mark.sanity
def testmergetomain():
    print("successfully merged to main")
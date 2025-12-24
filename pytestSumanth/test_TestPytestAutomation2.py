import pytest

@pytest.fixture(scope="module")
def preSetupWork():
    print("browser module setup for test 1 & 2")
    return "PASS"


@pytest.fixture(scope="function")
def secondWork():
    print("function setup for test 1 & 2") #execute before test is run
    yield #pause
    print("tear down validation") #excute after test is run


@pytest.mark.smoke
def test_sample(preSetupWork,secondWork):
    print("pytest test 1")
    assert preSetupWork=="PASS"


@pytest.mark.skip
def test_sample2(preSetupWork,secondWork):
    print("pyest test 2")
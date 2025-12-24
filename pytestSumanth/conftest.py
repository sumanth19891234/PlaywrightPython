import pytest


@pytest.fixture(scope="session")
def preWork():
    print("browser session setup for test 3 & 4")
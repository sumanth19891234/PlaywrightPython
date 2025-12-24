import pytest


def test_sample(preWork):
    print("pytest test 3")

@pytest.mark.smoke
def test_sample2(preWork):
    print("pyest test 4")
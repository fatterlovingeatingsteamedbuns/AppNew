import pytest


def pytest_addoption(parser):
    parser.addoption("--data", action='store', help="data")


@pytest.fixture(scope="class", autouse=True)
def data(request):
    return request.config.getoption("--data")

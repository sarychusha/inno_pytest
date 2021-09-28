import pytest


def pytest_addoption(parser):
    """."""
    parser.addoption("--log", action="store", default="log.txt", help="Write log to file")


@pytest.fixture
def log_file_name(request):
    """Фикстура, которая передает имя файла с логами."""
    return request.config.getoption("--log")




import pytest
from selene import browser


@pytest.fixture(autouse=True)
def setting_browser():

    browser.config.window_height = 750
    browser.config.window_width = 1200
    yield
    browser.quit()

@pytest.fixture()
def skip():
    """""
    TODO: добавить передачу  искомой переменной в вывод
    """""
    return pytest.skip("Ошибка, не находит")
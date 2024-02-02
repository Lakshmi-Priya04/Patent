from selenium.webdriver import Chrome
import pytest

@pytest.fixture(scope = "module")
def launch():
     driver = Chrome()
     driver.get("https://www.wipo.int/patinformed/")
     driver.maximize_window()
     driver.implicitly_wait(10)
     yield driver
     driver.close()
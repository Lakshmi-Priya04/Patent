from selenium import webdriver
import pytest

@pytest.fixture(scope = "module")
def launch():
     driver = webdriver.Chrome()
     driver.get("https://www.wipo.int/patinformed/")
     driver.maximize_window()
     driver.implicitly_wait(10)
     yield driver
     driver.close()
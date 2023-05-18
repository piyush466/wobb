import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=option)
    return driver
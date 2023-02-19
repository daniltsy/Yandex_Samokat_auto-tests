import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    print("\nstart chrome browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()

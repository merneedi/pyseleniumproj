from selenium import webdriver
import pytest
import logging


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver #value will be stored permananetly
    #return driver

def test_open_url_verify_title(driver):
    LOGGER = logging.getLogger(__name__)
    driver.get("https://app.vwo.com")
    print(driver.title) #verification
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("This is information logs")
    LOGGER.error('This is error logs')
    LOGGER.warning('This is warning logs')
    LOGGER.critical('This is critical logs')
    assert "Login - VWO" == driver.title

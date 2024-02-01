import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.JSUtil import JSUtils


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_js_execute(driver):
    URL = "https://selectorshub.com/xpath-practice-page/"
    driver.get(URL)
    # element = driver.find_element(By.ID,"pizza")
    # js_utils = JSUtils(driver)
    # js_utils.scroll_into_view(element)
    # element.send_keys("Hello This is sanddeep")
    div= driver.find_element(By.XPATH,"//div[@class='jackPart']")
    driver.execute_script("arguments[0].scrollIntoView(true);", div)

    pizza = driver.execute_script("return document.querySelector('div.jackPart').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('input#pizza');")
    pizza.send_keys("Farmhouse")
    time.sleep(4)
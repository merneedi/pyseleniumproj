import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
from selenium.webdriver.common.alert import Alert
import time


def test_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    driver.maximize_window()

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    #checkboxes_one = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")

    # check the checkbox which is not selected
    for c in checkboxes:
        if not c.is_selected():
            c.click()
    #checkboxes_one.click()
    time.sleep(15)

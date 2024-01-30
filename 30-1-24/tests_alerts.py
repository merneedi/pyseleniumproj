import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.common.alert import Alert

def test_alerts_testing():
    #LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    #button= driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
    button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
    button.click()
    wait = WebDriverWait(driver,10)
    wait.until(EC.alert_is_present())#timeout exception
    #wait.until(EC.presence_of_element_located())#element not visible exception

    alert = driver.switch_to.alert
    alert.send_keys("don")
    alert.accept()
    #alert.dismiss()
    result = driver.find_element(By.XPATH,"//p[@id='result']")
    print(result.text)
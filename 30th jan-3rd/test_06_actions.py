import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

def test_06_actions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    URL = "https://www.makemytrip.com/"
    driver.get(URL)

    time.sleep(5)
    fromcity = driver.find_element(By.ID,"fromCity")
    #fromcity.send_keys("New Delhi")
    actions = ActionChains(driver).move_to_element(fromcity).click().send_keys("New Delhi").perform()

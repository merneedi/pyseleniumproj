# open the browser
# navigate to the url
# FInd the email webelement and put email id = 'abc@gnail.com'
# Find the password input box and enter the password - 123
# Click on the bottom - sign in

# Verify that the dashboard is loaded - Pytest
# Create a report to send to QA lead - HTML - Allure report
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import logging

def test_vwologin():
    # Selenium API - Create session
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--start-maximized")
    #
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the browser
    # Naviagate to url
    #  command - driver.get (navigate command to existing sesssion )
    driver.get("https://app.vwo.com")

    # find the email webelement
    # find the pwd input box
    # click on the button - sign in

    # How to find the elements

    # find_element_by_id = finds an element by its unique id attribute
    # find_element_by_name = finds an element by its name attribute
    # find_element_by_xpath = finds an element by using xpath expression
    # find_element_by_link_text = finds anchor element (a) by its visible text
    # find_element_by_partial_link_text = finds anchor element (a) by a partial match
    # find_element_by_tag_name = finds an element by a html tag name
    # find_element_by_class_name = finds an element by its css classname

    email_address_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.NAME, "password")

    sign_in_ele = driver.find_element(By.ID, "js-login-btn")

    # sending the data email and password and clicking on the button
    # sendkeys and click()

    email_address_ele.send_keys("93npu2yyb0@esiix.com")
    password_ele.send_keys('Wingify@123')
    sign_in_ele.click()

    time.sleep(5)
    # There is delay for 3 -4
    LOGGER = logging.getLogger(__name__)
    LOGGER.info('title is >' + driver.title)
    assert "Login - VWO" in driver.title

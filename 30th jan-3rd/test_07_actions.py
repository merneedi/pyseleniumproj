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
    URL = "https://the-internet.herokuapp.com/windows"
    driver.get(URL)

    main_window_handle = driver.current_window_handle
    print(main_window_handle)
    link = driver.find_element(By.LINK_TEXT,"Click Here")
    link.click()

    window_handles = driver.window_handles
    print(window_handles)


    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
                print("Found the text")
                break

    driver.switch_to.window(main_window_handle)


    time.sleep(10)
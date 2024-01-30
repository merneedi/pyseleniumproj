import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

def test_04_actions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    iframe = driver.find_element(By.TAG_NAME,"iframe")

    # Scroll from element with offset 0,-50
    scroll_origin = ScrollOrigin.from_element(iframe)

    ActionChains(driver).scroll_from_origin(scroll_origin,0,200).perform()


    ActionChains(driver).scroll_to_element(iframe).perform()

    time.sleep(20)
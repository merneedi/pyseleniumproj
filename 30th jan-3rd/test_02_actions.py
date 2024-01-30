import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_02_actions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    # clickable = driver.find_element(By.ID,"clickable")
    # actions = ActionChains(driver)
    # actions.click_and_hold(clickable).key_down(Keys.SHIFT).send_keys("don").key_up(Keys.SHIFT).perform()

    # click - normal and action will be performed
    # click and hold - click and hold -> click but we will not release
    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver) \
        .click_and_hold(clickable) \
        .perform()


    assert "https://awesomeqa.com/selenium/mouse_interaction.html" in driver.current_url


    time.sleep(20)
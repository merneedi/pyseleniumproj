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
    driver.maximize_window()
    driver.get("https://www.ebay.com/b/PC-Desktops-All-In-One-Computers/179/bn_661752")


    ignore_list = [ElementNotVisibleException,ElementNotSelectableException]
    wait = WebDriverWait(driver,timeout=10,poll_frequency=1,ignored_exceptions=ignore_list)
    element = EC.presence_of_element_located((By.XPATH,"//span[contains(@class,'b-pageheader text')]"))


    see_all_list = driver.find_elements(By.XPATH,"//span[contains(text(),'See All')]")
    see_all_list[0].click()
    time.sleep(10)

    driver.find_element(By.CSS_SELECTOR,"div[id*='Computer%20Technologies']input").click()

    time.sleep(10)
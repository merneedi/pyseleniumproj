import pytest
import logging
from selenium import webdriver

# Chrome -> # chrome options

# Chrome with the Extensions,window size, proxy, JS disabled

def test_login():
    chrome_options = webdriver.ChromeOptions()


    extension_path = "/Users/Hp/Downloads/adblobker1.crx"
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_extension(extension_path)

    # 1. Headless mode: Run Chrome in headlines mode(without GUI)
    chrome_options.add_argument('--headless=new')

    # with UI - slow and consume lot of resources, see the test
    # without UI - headless - fast, it will consume less resources, can't see the test



    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://app.vwo.com")



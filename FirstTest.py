from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
    driver.maximize_window

def test_message():
    messageField = driver.find_element_by_id("user-message")
    messageField.send_keys("Sample Message")
 
    showMessageButton = driver.find_element_by_css_selector("button[onclick='showInput();']")
    showMessageButton.click()
 
    messageDisplay = driver.find_element_by_css_selector("#user-message #display")
    assert "Sample Message" in messageDisplay.text

def test_teardown():
    driver.close()
    driver.quit()
    print("Test Completed")
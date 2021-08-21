import time
from selenium.common.exceptions import NoSuchElementException
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# import pyautogui
# pyautogui.PAUSE = 2.5


URL = "https://demoqa.com/"

complying_username = "Jane Doe"
complying_email = "jane.doe@gmail.com"
complying_current_address = "29 Elm Street, 88901 Las Vegas, USA"
complying_permanent_address = "1 Piazza Navona, 000123 Rome, Italy"


def demo_site_starting(driver):
    driver.implicitly_wait(0.1)
    driver.get(URL)
    driver.maximize_window()
    time.sleep(0.1)
    try:
        driver.find_element_by_xpath("//img[@title='Ad.Plus Advertising']").click()
    except:
        pass
    time.sleep(0.1)
    # driver.execute_script("document.body.style.zoom='0.5'")
    time.sleep(0.1)


def advertisement_control(driver):
    try:
        driver.find_element_by_xpath("//img[@title='Ad.Plus Advertising']").click()
    except:
        time.sleep(0.1)
        pass


def wait_then_find(driver, seconds, xpath):
    time.sleep(1)
    clickable_element = WebDriverWait(driver, seconds).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    clickable_element.click()
    time.sleep(1)


def wait_then_click(driver, seconds, xpath):
    time.sleep(1)
    clickable_element = WebDriverWait(driver, seconds).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    clickable_element.click()
    time.sleep(1)


def element_does_not_exist_by_xpath(driver, xpath):
    with pytest.raises(NoSuchElementException):
        driver.find_element_by_xpath(xpath)


def element_does_not_exist_by_link_text(driver, link_text):
    with pytest.raises(NoSuchElementException):
        driver.find_element_by_xpath(link_text)

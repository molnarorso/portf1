import time
from selenium.common.exceptions import NoSuchElementException
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


URL = "https://demoqa.com/"

complying_username = "Jane Doe"
complying_email = "janedoe@example.com"
complying_current_address = "29 Elm Street, 88901 Las Vegas, USA"
complying_permanent_address = "1 Piazza Navona, 000123 Rome, Italy"

non_complying_email_1 = 'janedoe.example.com'
non_complying_email_2 = 'janedoe@example.c'
non_complying_email_3 = 'janedoe@example.'
non_complying_email_4 = 'janedoe@.com'
non_complying_email_5 = '@example.com'
non_complying_email_6 = 'jane@doe@example.com'
non_complying_email_7 = '12@3.4'
non_complying_email_8 = '12@example.3'
non_complying_email_9 = 'janedoe@example.com.'

non_complying_emails = [
    non_complying_email_1,
    non_complying_email_2,
    non_complying_email_3,
    non_complying_email_4,
    non_complying_email_5,
    non_complying_email_6,
    non_complying_email_7,
    non_complying_email_8,
    non_complying_email_9]


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

from data_and_functions import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class TestElementsTextBox(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        demo_site_starting(self.driver)
        wait_then_click(self.driver, 20, "//div[@class='category-cards']//div[1]//div[1]//div[1]")
        time.sleep(0.1)
        self.driver.find_element_by_xpath("//span[normalize-space()='Text Box']").click()

    def teardown(self):
        time.sleep(0.1)
        self.driver.quit()

    # TC001: Completing form using complying data
    def test_completing_form(self):
        time.sleep(0.1)
        self.driver.find_element_by_xpath("//span[normalize-space()='Text Box']").click()
        self.driver.find_element_by_xpath("//input[@id='userName']").send_keys(complying_username)
        self.driver.find_element_by_xpath("//input[@id='userEmail']").send_keys(complying_email)
        self.driver.find_element_by_xpath("//textarea[@id='currentAddress']").send_keys(complying_current_address)
        self.driver.find_element_by_xpath("//textarea[@id='permanentAddress']").send_keys(complying_permanent_address)
        self.driver.find_element_by_xpath("//textarea[@id='permanentAddress']").send_keys(Keys.TAB)

        my_action = ActionChains(self.driver)
        my_action.send_keys(Keys.ENTER)
        my_action.perform()
        time.sleep(3)

        registered_name = self.driver.find_element_by_xpath("//p[@id='name']")
        registered_email = self.driver.find_element_by_xpath("//p[@id='email']")
        registered_current_address = self.driver.find_element_by_xpath("//p[@id='currentAddress']")
        registered_permanent_address = self.driver.find_element_by_xpath("//p[@id='permanentAddress']")

        assert registered_name.text == f"Name:{complying_username}"
        assert registered_email.text == f"Email:{complying_email}"
        assert registered_current_address.text == f"Current Address :{complying_current_address}"
        assert registered_permanent_address.text == f"Permananet Address :{complying_permanent_address}"

import time

from data_and_functions_for_elements_text_box import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class TestElementsTextBoxUsingWrongEmailFormats(object):
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

    # TC002: Completing form using wrong email formats
    def test_completing_form(self):
        time.sleep(0.1)
        self.driver.execute_script("document.body.style.zoom='45%'")
        time.sleep(0.1)
        for i in non_complying_emails:
            time.sleep(0.1)
            self.driver.find_element_by_xpath("//input[@id='userEmail']").clear()
            time.sleep(0.1)
            self.driver.find_element_by_xpath("//input[@id='userEmail']").send_keys(i)
            self.driver.find_element_by_xpath("//textarea[@id='permanentAddress']").send_keys(Keys.TAB)
            my_action = ActionChains(self.driver)
            my_action.send_keys(Keys.ENTER)
            my_action.perform()
            time.sleep(1)
            assert self.driver.find_element_by_xpath("//input[@class='mr-sm-2 field-error form-control']").is_enabled()

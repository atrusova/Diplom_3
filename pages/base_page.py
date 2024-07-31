from telnetlib import EC

from selenium.webdriver import ActionChains

from data import order_num
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(
            locator))
        return self.driver.find_element(*locator)

    def drag_and_drop(self, locator_element, locator_target):
        element = self.find_element_with_wait(locator_element)
        target = self.find_element_with_wait(locator_target)
        ActionChains(self.driver) \
            .drag_and_drop(element, target) \
            .perform()

    def wait_until_text_is_not(self, locator, text):
        WebDriverWait(self.driver, 30).until_not(
            expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator).text

    def wait_element_be_clickable(self, locator):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click

    def find_element_with_implicitly_wait(self):
        self.driver.implicitly_wait(10)

    def no_element_with_wait(self, locator):
        WebDriverWait(self.driver, 30).until_not(expected_conditions.visibility_of_element_located(
            locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(
            locator))
        return self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

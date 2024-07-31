from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators


class HeaderPage(BasePage):

    @allure.step('Найти заголовок Конструктор')
    def find_constructor(self):
        self.find_element_with_wait(HeaderLocators.PAGE_CONSTRUCTOR)

    @allure.step('Клик на заголовок Конструктор')
    def click_to_constructor(self):
        self.find_element_with_wait(HeaderLocators.PAGE_CONSTRUCTOR)
        self.click_to_element(HeaderLocators.PAGE_CONSTRUCTOR)

    @allure.step('Найти заголовок Собрать бургер')
    def find_header_constructor(self):
        return self.find_element_with_wait(HeaderLocators.SEARCH_MAIN_HEAD)

    @allure.step('Кликнуть на Ленту заказов')
    def click_to_order_list(self):
        self.click_to_element(HeaderLocators.ORDER_LIST)

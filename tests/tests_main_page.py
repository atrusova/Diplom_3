import time
import allure
import pytest
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.login_page import LoginPage
from pages.header_page import HeaderPage
from conftest import driver
from selenium.webdriver import ActionChains


class TestMainPage:

    @allure.title('Проверка перехода на конструктор')
    def test_switch_to_constructor_in_main_page(self, driver):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        main_page.click_order_list()
        main_page.click_constructor()

        assert header_page.find_header_constructor()

    @allure.title('Проверка перехода в список заказов')
    def test_switch_to_order_list_in_main_page(self, driver):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)
        main_page.click_order_list()

        assert order_list_page.find_header

    @allure.title('Проверка отображения всплывающего окна с деталями по клику на ингредиент')
    def test_click_to_element_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_element_in_constructor()

        assert main_page.find_header_modal_window_element_construction()

    @allure.title('Проверка закрытия модального окна с детализацией ингредиента')
    def test_close_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_element_in_constructor()
        main_page.click_to_close_element_modal_window()

        assert main_page.modal_window_is_closed()

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_check_count(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop(driver)
        assert main_page.find_bun_count_increase()

    @allure.title('Проверка офрмления заказа залогиненным пользователем')
    def test_add_ingredient_check_count(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_to_profile()
        login_page.login_user()
        main_page.drag_and_drop(driver)
        main_page.click_to_order()
        assert main_page.find_order_info_after_order()



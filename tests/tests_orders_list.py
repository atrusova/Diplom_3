import time
import allure
import pytest
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.login_page import LoginPage
from pages.header_page import HeaderPage
from pages.profile_page import ProfilePage
from pages.order_list_page import OrderListPage
from conftest import driver


class TestOrderList:

    @allure.title('Проверка оформления заказа залогиненным пользователем')
    def test_order_auth_user(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_to_profile()
        login_page.login_user()
        main_page.click_constructor()
        main_page.drag_and_drop_ingredient_to_basket()
        main_page.click_to_order()

        assert main_page.get_order_number()

    @allure.title('Проверка, если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_order_details(self, driver):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.click_order_list()
        order_list_page.click_to_order_in_list_order()

        assert order_list_page.find_opened_modal_window()

    @allure.title(f'Проверка отображения заказов пользователя из «Истории заказов» на странице «Лента заказов»')
    def test_visible_order_history_in_order_line(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        header_page = HeaderPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.click_to_profile()
        login_page.login_user()
        main_page.make_order()
        main_page.click_to_profile()
        profile_page.click_to_orders_history()
        order_num_in_profile = profile_page.find_order_number_in_history()
        header_page.click_to_order_list()
        order_list = []
        order_num_1 = order_list_page.find_last_order_number_in_order_list()
        order_num_2 = order_list_page.find_order_number_in_order_list()

        order_list.append(order_num_1)
        order_list.append(order_num_2)

        assert order_num_in_profile in order_list

    @allure.title('Проверка увеличения счётчика "Выполнено за всё время" при создании нового заказа')
    def test_check_count_for_all_time_after_new_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        header_page = HeaderPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.click_to_profile()
        login_page.login_user()
        header_page.click_to_order_list()
        num_orders_before = order_list_page.find_number_orders_for_all_time()
        header_page.click_to_constructor()
        main_page.make_order()
        header_page.click_to_order_list()
        num_order_after = order_list_page.find_number_orders_for_all_time()

        assert num_order_after > num_orders_before

    @allure.title(f'Проверка увеличения счётчика "Выполнено за сегодня" при создании нового заказа')
    def test_check_count_for_today_time_after_new_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        header_page = HeaderPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.click_to_profile()
        login_page.login_user()
        header_page.click_to_order_list()
        num_orders_before = order_list_page.find_number_orders_for_today()
        header_page.click_to_constructor()
        main_page.make_order()
        header_page.click_to_order_list()
        num_order_after = order_list_page.find_number_orders_for_today()

        assert num_order_after > num_orders_before

    @allure.title('Проверка отображения номера заказа в разделе "В работе" после оформления заказа')
    def test_check_order_number_in_count_in_progress(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        header_page = HeaderPage(driver)
        profile_page = ProfilePage(driver)
        order_list_page = OrderListPage(driver)

        main_page.click_to_profile()
        login_page.login_user()
        order_num = main_page.make_order()
        main_page.click_to_close_element_modal_window()
        header_page.click_to_order_list()
        order_number_in_list = order_list_page.find_order_number_in_progress()

        assert f'0{order_num}' == order_number_in_list



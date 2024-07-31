import time
import allure
import pytest
from data import main_email, main_pass
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from conftest import driver


class TestLoginPage:

    @allure.title(f'Проверка перехода на личный кабинет')
    def test_login_user_open_profile(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.click_to_profile()
        login_page.login_user()
        main_page.click_to_profile()
        assert profile_page.find_header_profile()

    @allure.title(f'Проверка перехода в список заказов в профиле')
    def test_open_order_history(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.click_to_profile()
        login_page.login_user()
        main_page.click_to_profile()
        profile_page.click_to_orders_history()
        assert profile_page.find_active_tab_orders_history()

    @allure.title(f'Проверка выхода из аккаунта')
    def test_logout(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        main_page.click_to_profile()
        login_page.login_user()
        main_page.click_to_profile()
        profile_page.click_to_logout()
        assert login_page.find_button_login()

    @allure.title(f'Проверка переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_switch_to_page_forgot_password(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_to_profile()
        login_page.click_to_forgot_password()
        assert login_page.find_forgot_pass_in_forgot_pass_page()

    @allure.title(f'Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_add_email_in_forgot_password_page_and_submit(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_to_profile()
        login_page.click_to_forgot_password()
        login_page.click_to_email_forgot_pass()
        login_page.add_text_to_email_forgot_pass()
        login_page.click_to_button_forgot_pass()
        assert login_page.find_password_input_in_forgot_pass_page()

    @allure.title(f'Проверка отображения пароля по клику на кнопку показать/скрыть пароль на форме восстановления пароля')
    def test_show_pass_in_forgot_password_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_to_profile()
        login_page.click_to_forgot_password()
        login_page.click_to_email_forgot_pass()
        login_page.add_text_to_email_forgot_pass()
        login_page.click_to_button_forgot_pass()
        login_page.add_text_in_password_input_in_forgot_pass_page()
        login_page.click_to_show_password()
        assert login_page.find_active_input_password()

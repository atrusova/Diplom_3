import time
import allure
import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from data import main_email, main_pass
from locators.login_page import LoginLocators
from conftest import driver


class LoginPage(BasePage):

    @allure.step('Заполнение полей на форме Входа и авторизация')
    def login_user(self):
        self.find_element_with_wait(LoginLocators.INPUT_EMAIL)
        self.click_to_element(LoginLocators.INPUT_EMAIL)
        self.add_text_to_element(LoginLocators.INPUT_EMAIL, main_email)
        self.click_to_element(LoginLocators.INPUT_PASS)
        self.add_text_to_element(LoginLocators.INPUT_PASS, main_pass)
        self.click_to_element(LoginLocators.LINK_LOG_IN)

    def find_button_login(self):
        return self.find_element_with_wait(LoginLocators.LINK_LOG_IN)

    def click_to_forgot_password(self):
        self.click_to_element(LoginLocators.LINK_FORGOT_PASSWORD)

    def click_to_email_forgot_pass(self):
        self.click_to_element(LoginLocators.INPUT_EMAIL)

    def add_text_to_email_forgot_pass(self):
        self.add_text_to_element(LoginLocators.INPUT_EMAIL, main_email)

    def click_to_button_forgot_pass(self):
        self.click_to_element(LoginLocators.BUTTON_FORGOT_PASS)

    def find_password_input_in_forgot_pass_page(self):
        return self.find_element_with_wait(LoginLocators.INPUT_PASS)

    def add_text_in_password_input_in_forgot_pass_page(self):
        self.add_text_to_element(LoginLocators.INPUT_PASS, main_pass)

    def find_forgot_pass_in_forgot_pass_page(self):
        return self.find_element_with_wait(LoginLocators.BUTTON_FORGOT_PASS)

    def click_to_show_password(self):
        self.click_to_element(LoginLocators.SHOW_PASS)

    def find_active_input_password(self):
        return self.find_element_with_wait(LoginLocators.INPUT_PASS_VISIBLE)

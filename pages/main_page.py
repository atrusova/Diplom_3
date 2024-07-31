import time

import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.header_locators import HeaderLocators
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from conftest import driver


class MainPage(BasePage):

    @allure.step("Клик на вкладку Конструктор")
    def click_constructor(self):
        self.click_to_element(HeaderLocators.PAGE_CONSTRUCTOR)

    @allure.step("Клик на вкладку Лента Заказов")
    def click_order_list(self):
        self.find_element_with_wait(HeaderLocators.ORDER_LIST)
        self.click_to_element(HeaderLocators.ORDER_LIST)

    @allure.step("Клик на булку или ингредиент в конструкторе")
    def click_to_element_in_constructor(self):
        return self.click_to_element(MainPageLocators.ELEMENT_IN_CONSTRUCTOR)

    @allure.step("Поиск заголовка в модальном окне с детализацией ингредиента")
    def find_header_modal_window_element_construction(self):
        return self.find_element_with_wait(MainPageLocators.MODAL_WINDOW_ELEMENT)

    @allure.step("Клик на крестик в модальном окне с информацией о булке или ингридиенте")
    def click_to_close_element_modal_window(self):
        self.wait_until_order_number_will_be_change()
        self.click_to_element(MainPageLocators.CLOSE_ELEMENT_MODAL_WINDOW)

    @allure.step("Найти открытое модальное окно с описанием ингридиента")
    def find_opened_modal_window_ingredient(self):
        return self.find_element_with_wait(MainPageLocators.OPENED_MODAL_WINDOW_ELEMENT_INGREDIENT)

    @allure.step("Убедимся что модальное окно закрыто, отсутствует крестик закрытия окна")
    def modal_window_is_closed(self):
        return self.no_element_with_wait(MainPageLocators.CLOSE_ELEMENT_MODAL_WINDOW)

    @allure.step("Поиск увеличенного счетчика у ингридиента")
    def find_bun_count_increase(self):
        return self.find_element_with_wait(MainPageLocators.BUN_COUNTER_INCREASE)

    @allure.step("Клик на кнопку Оформить заказ")
    def click_to_order(self):
        self.find_element_with_implicitly_wait()
        self.click_to_element(MainPageLocators.BUTTON_ORDER)

    @allure.step("Поиск заголовка о завершенном заказе")
    def find_order_info_after_order(self):
        return self.find_element_with_wait(MainPageLocators.TEXT_ORDER_INFO)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        self.find_element_with_implicitly_wait()
        return self.get_text_from_element(MainPageLocators.ORDER_NUMBER)

    @allure.step("Нажатие на Личный кабинет")
    def click_to_profile(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_PROFILE)
        self.click_to_element(MainPageLocators.BUTTON_PROFILE)

    @allure.step("Ожидание изменения номера заказа с дефолтного на настоящее")
    def wait_until_order_number_will_be_change(self):
        self.find_element_with_implicitly_wait()
        self.wait_until_text_is_not(MainPageLocators.ORDER_NUMBER, '9999')

    def wait_close_modal_be_clickable(self):
        self.wait_element_be_clickable(MainPageLocators.CLOSE_ELEMENT_MODAL_WINDOW)

    def print_order_num_modal_window(self):
        text = self.get_order_number()
        return print(f'Номер заказа из модального окна:{text}')

    def print_order_num_from_list(self):
        text = self.get_order_number()
        return print(f'Номер заказа из списка заказов:{text}')

    def drag_and_drop_ingredient_to_basket(self):
        self.drag_and_drop(MainPageLocators.BUN_ELEMENT_IN_CONSTRUCTOR, MainPageLocators.ORDER_BASKET)

    @allure.step("Оформить заказ")
    def make_order(self):
        self.drag_and_drop_ingredient_to_basket()
        self.click_to_order()
        self.wait_until_order_number_will_be_change()
        order_number = self.get_order_number()
        self.click_to_close_element_modal_window()

        return order_number






import allure
from pages.base_page import BasePage
from locators.order_list_locators import OrderListLocators


class OrderListPage(BasePage):

    @allure.step("Клик на вкладку Конструктор")
    def find_header(self):
        self.find_element_with_wait(OrderListLocators.HEADER_ORDER_LIST)

    @allure.step("Клик на заказ в списке заказов")
    def click_to_order_in_list_order(self):
        self.click_to_element(OrderListLocators.ORDER_IN_LIST_ORDER)

    @allure.step("Найти открытое модальное окно")
    def find_opened_modal_window(self):
        return self.find_element_with_wait(OrderListLocators.MODAL_WINDOW_ELEMENT_IN_ORDER_LIST)

    @allure.step("Найти количество заказов за все время")
    def find_number_orders_for_all_time(self):
        self.find_element_with_wait(OrderListLocators.ORDERS_FOR_ALL_TIME)
        return self.get_text_from_element(OrderListLocators.ORDERS_FOR_ALL_TIME)

    @allure.step("Найти количество заказов за сегодня")
    def find_number_orders_for_today(self):
        self.find_element_with_wait(OrderListLocators.ORDERS_FOR_TODAY)
        return self.get_text_from_element(OrderListLocators.ORDERS_FOR_TODAY)

    @allure.step("Найти последний номер заказа в ленте заказов")
    def find_last_order_number_in_order_list(self):
        self.find_element_with_wait(OrderListLocators.ORDER_NUMBER_IN_LIST_ORDERS)
        return self.get_text_from_element(OrderListLocators.ORDER_NUMBER_IN_LIST_ORDERS)

    @allure.step("Найти предпоследний номер заказа в ленте заказов")
    def find_order_number_in_order_list(self):
        self.find_element_with_wait(OrderListLocators.ORDER_NUMBER_IN_LIST_ORDERS_2)
        return self.get_text_from_element(OrderListLocators.ORDER_NUMBER_IN_LIST_ORDERS_2)

    @allure.step("Найти номер заказа в работе")
    def find_order_number_in_progress(self):
        self.find_element_with_wait(OrderListLocators.ORDERS_IN_PROGRESS)
        return self.get_text_from_element(OrderListLocators.ORDERS_IN_PROGRESS)

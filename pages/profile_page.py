import allure

from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators


class ProfilePage(BasePage):

    @allure.step("Найти заголовок профиля")
    def find_header_profile(self):
        return self.find_element_with_wait(ProfileLocators.HEADER_PROFILE)

    @allure.step("Нажать на Историю заказов")
    def click_to_orders_history(self):
        self.click_to_element(ProfileLocators.ORDERS_HISTORY)

    @allure.step("Найти активную вкладку история заказов")
    def find_active_tab_orders_history(self):
        return self.find_element_with_wait(ProfileLocators.ORDERS_HISTORY_ACTIVE)

    @allure.step("Нажать на Выйти")
    def click_to_logout(self):
        self.click_to_element(ProfileLocators.LOGOUT)

    @allure.step("Найти номер заказа в истории заказов в профиле пользователя")
    def find_order_number_in_history(self):
        return self.get_text_from_element(ProfileLocators.LAST_ORDER_IN_HISTORY)


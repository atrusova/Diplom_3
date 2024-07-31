from selenium.webdriver.common.by import By

class ProfileLocators:
    HEADER_PROFILE = By.XPATH, ".//*[text()= 'Профиль']"  # Вкладка Профиль в профиле
    ORDERS_HISTORY = By.XPATH, ".//a[text()= 'История заказов']"  # Вкладка история заказов в профиле
    ORDERS_HISTORY_ACTIVE = By.XPATH, "//*[contains(@class, 'Account_link_active')]"  # Активная вкладка История
    # заказов в профиле
    LOGOUT = By.XPATH, ".//button[text()= 'Выход']"  # Кнопка Выход
    ORDER_NUMBER_IN_HISTORY_ORDERS = By.XPATH, "(.//p[contains(text(), '#')])[1]"  # Последний номер заказа из истории заказов
    # в профиле пользователя"

    LAST_ORDER_IN_HISTORY = By.XPATH, "(.//div[contains(@class, 'OrderHistory_textBox')]//p[contains(@class, 'text_type_digits-default')])[last()]"

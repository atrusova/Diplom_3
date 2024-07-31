from selenium.webdriver.common.by import By


class OrderListLocators:
    HEADER_ORDER_LIST = By.XPATH, ".//h1[text()='Лента заказов']"
    ORDER_IN_LIST_ORDER = By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]"

    MODAL_WINDOW_ELEMENT_IN_ORDER_LIST = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]"

    ORDERS_FOR_ALL_TIME = By.XPATH, "(.//p[contains(@class, 'OrderFeed_number') and contains(@class, 'text_type_digits-large')])[1]" # Счетчик количества заказов за все время
    ORDERS_FOR_TODAY = By.XPATH, "(.//p[contains(@class, 'OrderFeed_number') and contains(@class, 'text_type_digits-large')])[2]" # Счетчик количества заказов за сегодня

    ORDER_NUMBER_IN_LIST_ORDERS = By.XPATH, "(.//p[contains(text(), '#')])[1]" # Последний номер заказа из Ленты заказов на главной"
    ORDER_NUMBER_IN_LIST_ORDERS_2 = By.XPATH, "(.//p[contains(text(), '#')])[2]" # Последний номер заказа из Ленты заказов на главной"

    #FIND_ORDER_IN_LIST = By.XPATH, f"//a[contains(@class, 'OrderHistory_link__1iNby')]//p[contains(@class, 'text_type_digits-default') and contains(text(), '{order_number}')]"


    ALL_ORDERS = By.XPATH, "//a[contains(@class, 'OrderHistory_link__1iNby')]"
    ORDERS_IN_PROGRESS = By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady') and contains(@class, 'OrderFeed_orderList')]/li[contains(@class, 'text_type_digits-default')]" # Номер заказа из блока В работе

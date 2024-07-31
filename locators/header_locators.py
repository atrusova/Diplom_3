from selenium.webdriver.common.by import By


class HeaderLocators:

    PAGE_CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"  # Раздел "Конструктор"
    ORDER_LIST = By.XPATH, ".//p[text()='Лента Заказов']" # Раздел "Лента заказов"
    SEARCH_MAIN_HEAD = By.XPATH, ".//h1[text()='Соберите бургер']"  # Заголовок в конструкторе на главной
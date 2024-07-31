from selenium.webdriver.common.by import By


class MainPageLocators:
    ELEMENT_IN_CONSTRUCTOR = By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]" # Булки и ингридиенты в конструкторе заказа
    BUN_ELEMENT_IN_CONSTRUCTOR = By.XPATH, ".//*[@alt = 'Флюоресцентная булка R2-D3']" # Булка для перетаскивания дарнэндроп в заказ
    PRICE_BUN_IN_BASKET = By.XPATH, ".//span[text() = '988']" # Цена булки Флюоресцентная булка R2-D3 в корзине
    BUN_COUNTER_INCREASE = By.XPATH, ".//p[contains(@class, 'counter__num') and text()='2']" # .//p[contains(@class, 'counter__num') and text()='2']
    BUTTON_ORDER = By.XPATH, ".//button[text()='Оформить заказ']" # Кнопка "Оформить заказ" на главной
    TEXT_ORDER_INFO = By.XPATH, ".//p[text()='идентификатор заказа']"
    ORDER_NUMBER = By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]" # Номер зазказа в модальном окне после оформления заказа
    ORDER_NUMBER_9999 = By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow') and text()='9999']" # Дефолтный номер зазказа в модальном окне после оформления заказа


    MODAL_WINDOW_ELEMENT_CONSTRUCTION = By.XPATH, ".//div[contains(@class, 'Modal_modal__container')]" # модальное окно ингредиента в конструкторе
    MODAL_WINDOW_ELEMENT = By.XPATH, ".//h2[text()='Детали ингредиента']" # заголовок в модальном окне ингредиента в конструкторе
    CLOSE_ELEMENT_MODAL_WINDOW = By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]"  # крестик для закрытия модального окна ингредиента в конструкторе
    TEXT_IN_MODAL_WINDOW = By.XPATH, ".//*[text()='Дождитесь готовности на орбитальной станции']"

    OPENED_MODAL_WINDOW_ELEMENT_INGREDIENT = By.XPATH, ".//*[contains(@class, 'Modal_modal_opened')]" # Открытое модальное окно об ингредиенте
    ORDER_BASKET = By.XPATH, ".//*[contains(@class, 'BurgerConstructor_basket')]" # корзина заказа

    BUTTON_PROFILE = By.XPATH, ".//*[@href = '/account']/p[text()='Личный Кабинет']"  # Кнопка "Личный кабинет"
    SEARCH_BUTTON_LOG_IN = By.XPATH, ".//button[text()='Войти']"  # Кнопка "Войти" на форме входа

    SEARCH_PROFILE = By.XPATH, ".//*[@href = '/account']/p[text()='Личный Кабинет']"  # Кнопка "Личный кабинет"

    SEARCH_LINK_REGISTRATION = By.XPATH, ".//a[@href = '/register']"  # Ссылка "Зрегистрироваться" на форме входа
    SEARCH_LINK_LOG_IN = By.XPATH, ".//a[@href = '/login']"  # Ссылка "Войти" на форме регистрации
    SEARCH_LINK_FORGOT_PASSWORD = By.XPATH, ".//a[@href = '/forgot-password']"  # Ссылка "Восстановить пароль" на форме входа

    SEARCH_INPUT_REGISTRATION_NAME = By.XPATH, ".//*[text()='Имя']/following-sibling::input"  # Поле "Имя" на форме входа
    SEARCH_INPUT_EMAIL = By.XPATH, ".//*[text()='Email']/following-sibling::input"  # Поле "Email" на форме входа
    SEARCH_INPUT_PASS = By.XPATH, ".//*[text()='Пароль']/following-sibling::input"  # Поле "Пароль" на форме входа


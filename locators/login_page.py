from selenium.webdriver.common.by import By


class LoginLocators:
    LINK_REGISTRATION = By.XPATH, ".//a[@href = '/register']"  # Ссылка "Зрегистрироваться" на странице регистрации
    LINK_LOG_IN = By.XPATH, ".//button[text()= 'Войти']"  # Ссылка "Войти" на форме входа
    LINK_FORGOT_PASSWORD = By.XPATH, ".//a[@href = '/forgot-password']"  # Ссылка "Восстановить пароль" на форме входа
    BUTTON_FORGOT_PASS = By.XPATH, ".//button[text()='Восстановить']" # Кнопка восстановить на странице восстановления пароля
    SHOW_PASS = By.XPATH, ".//div[contains(@class, 'input__icon input__icon-action')]" # Иконка "глаз" для отображения пароля
    INPUT_PASS_VISIBLE = By.XPATH, ".//div[contains(@class, 'input_status_active')]"

    INPUT_REGISTRATION_NAME = By.XPATH, ".//*[text()='Имя']/following-sibling::input"  # Поле "Имя" на форме входа
    INPUT_EMAIL = By.XPATH, ".//*[text()='Email']/following-sibling::input"  # Поле "Email" на форме входа
    INPUT_PASS = By.XPATH, ".//*[text()='Пароль']/following-sibling::input"  # Поле "Пароль" на форме входа
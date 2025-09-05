from selenium.webdriver.common.by import By

class Locators:
    # ===== ОСНОВНЫЕ ЭЛЕМЕНТЫ =====
    THE_SIGN_IN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    LOGO = (By.XPATH, "//div[contains(@class, 'logo')]")
    PERSONAL_ACCOUNT = (By.XPATH, '//a[p[text()="Личный Кабинет"]]')
    BUTTON_CHECKOUT = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(),'Выход')]")

    # ===== ФОРМА РЕГИСТРАЦИИ =====
    FIELD_EMAIL = (By.XPATH, "//input[@type='email']")
    FIELD_PASSWORD = (By.XPATH, "//input[@type='password']")
    FIELD_NAME = (By.XPATH, "//input[@name='name']")
    LOGIN_PAGE_INDICATOR = (By.XPATH, "//h2[text()='Вход']")
    FIELD_NAME_REGISTER = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
    FIELD_EMAIL_REGISTER = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    FIELD_PASSWORD_REGISTER = (By.XPATH, "//input[@type='password']")
    BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")
    REGISTER_LINK = (By.XPATH, '//a[text()="Зарегистрироваться" and @href="/register"]')
    LOGIN_LINK_REGISTER = (By.XPATH, "//a[text()='Войти' and @href='/login']")

    # ===== ФОРМА АВТОРИЗАЦИИ =====
    FIELD_EMAIL_LOGIN = (By.XPATH, "//input[@type='text' and @name='name']")
    FIELD_PASSWORD_LOGIN = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    BUTTON_ENTRANCE = (By.XPATH, "//button[text()='Войти']")
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")

    # ===== ФОРМА ВОССТАНОВЛЕНИЯ ПАРОЛЯ =====
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")
    RECOVERY_FIELD_EMAIL = (By.XPATH, "//input[@type='text']")

    # ===== КОНСТРУКТОР =====
    BREAD_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    TOPPINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
    
    # ДОБАВЛЕНО: Заголовки разделов
    BREAD_TITLE = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_TITLE = (By.XPATH, "//h2[text()='Соусы']")
    TOPPINGS_TITLE = (By.XPATH, "//h2[text()='Начинки']")
    
    # ДОБАВЛЕНО: Элементы для скролла и видимости
    BODY = (By.TAG_NAME, "body")

    # ===== ЛИЧНЫЙ КАБИНЕТ =====
    INSCRIPTION_PROFILE = (By.XPATH, "//a[contains(@href, '/account/profile')]")
    BUTTON_LOGOUTBIG = (By.XPATH, "//button[contains(text(), 'Выход')]")

    # ===== ОШИБКИ И ВАЛИДАЦИЯ =====
    ERROR_ACCOUNT_EXISTS = (By.XPATH, "//p[contains(text(), 'Такой пользователь уже существует')]")
    ERROR_PASSWORD = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
    VALIDATION_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")
    ANY_ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'error') or contains(@class, 'Error')]")
    
    # ===== ДОПОЛНИТЕЛЬНЫЕ ЛОКАТОРЫ =====
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'success')]")
    PROFILE_LINK = (By.XPATH, "//a[contains(@href, '/account')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'modal_overlay')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal_close')]")
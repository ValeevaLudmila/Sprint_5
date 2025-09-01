from selenium.webdriver.common.by import By

class Locators:
    # ===== ОСНОВНЫЕ ЭЛЕМЕНТЫ =====
    # Кнопка "Войти в аккаунт" на главной странице
    THE_SIGN_IN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    
    # Основной логотип
    LOGO = (By.XPATH, "//div[contains(@class, 'logo')]")
    
    # Кнопка "Личный Кабинет"
    PERSONAL_ACCOUNT = (By.XPATH, '//a[p[text()="Личный Кабинет"]]')
    
    # Кнопка "Оформить заказ" (появляется после авторизации)
    BUTTON_CHECKOUT = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")
    
    # Надпись "Выход"
    BUTTON_LOGOUT = (By.XPATH, './/button[contains(text(),"Выход")]')

    # ===== ФОРМА РЕГИСТРАЦИИ =====
    # Поля для регистрации
    FIELD_NAME_REGISTER = (By.XPATH, "(//input[@name='name'])[1]")  # Поле имени
    FIELD_EMAIL_REGISTER = (By.XPATH, "(//input[@name='name'])[2]")  # Поле email
    FIELD_PASSWORD_REGISTER = (By.XPATH, "//input[@name='Пароль']")  # Поле пароля
    
    # Кнопка "Зарегистрироваться"
    BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    # Ссылка "Зарегистрироваться" на главной
    REGISTER_LINK = (By.XPATH, '//a[text()="Зарегистрироваться" and @href="/register"]')
    
    # Ссылка "Войти" на странице регистрации
    LOGIN_LINK_REGISTER = (By.XPATH, "//a[text()='Войти' and @href='/login']")

    # ===== ФОРМА АВТОРИЗАЦИИ =====
    # Поля для авторизации
    FIELD_EMAIL_LOGIN = (By.XPATH, "//input[@name='name' and @type='text']")  # Поле email на странице логина
    FIELD_PASSWORD_LOGIN = (By.XPATH, "//input[@name='Пароль' and @type='password']")  # Поле пароля на странице логина
    
    # Кнопка "Войти"
    BUTTON_ENTRANCE = (By.XPATH, ".//button[contains(text(),'Войти')]")
    
    # Ссылка "Войти" на других страницах
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")

    # ===== ФОРМА ВОССТАНОВЛЕНИЯ ПАРОЛЯ =====
    # Кнопка "Восстановить пароль"
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")
    
    # Поле email для восстановления
    RECOVERY_FIELD_EMAIL = (By.XPATH, "//input[@name='name']")

    # ===== КОНСТРУКТОР =====
    # Разделы конструктора
    BREAD_SECTION = (By.XPATH, ".//span[contains(text(), 'Булки')]")
    SAUCES_SECTION = (By.XPATH, ".//span[contains(text(), 'Соусы')]")
    TOPPINGS_SECTION = (By.XPATH, ".//span[contains(text(), 'Начинки')]")
    
    # Активный раздел
    ACTIVE_SECTION = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]')
    
    # Надписи разделов
    INSCRIPTION_BREAD = (By.XPATH, "//h2[contains(text(),'Булки')]")

    # ===== ЛИЧНЫЙ КАБИНЕТ =====
    # Перейти в профиль
    INSCRIPTION_PROFILE = (By.XPATH, './/a[contains(@href, "/account/profile")]')
    
    # Кнопка "Выход" в аккаунте
    BUTTON_LOGOUTBIG = (By.XPATH, "//button[contains(@class, 'Account_button') and text()='Выход']")

    # ===== ОШИБКИ =====
    ERROR_ACCOUNT_EXISTS = (By.XPATH, ".//p[contains(text(), 'Такой пользователь уже существует')]")
    ERROR_PASSWORD = (By.XPATH, '//div[contains(@class, "input_status_error")]')
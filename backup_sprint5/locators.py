from selenium.webdriver.common.by import By

class Locators:
    # Кнопка "Войти в аккаунт" на главной странице
    THE_SIGN_IN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    
    # Основной логотип
    LOGO = (By.XPATH, "//header/nav/div")
    
    # Кнопка "Личный Кабинет"
    PERSONAL_ACCOUNT = (By.XPATH, '//a[p[text()="Личный Кабинет"]]')
    
    # Кнопка "Зарегистрироваться"
    BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    # Поля для регистрации (ИСПРАВЛЕНО)
    FIELD_NAME_REGISTER = (By.XPATH, "(//input[@name='name'])[1]")  # Первое поле name
    FIELD_EMAIL_REGISTER = (By.XPATH, "(//input[@name='name'])[2]")  # Второе поле name (email)
    FIELD_PASSWORD_REGISTER = (By.XPATH, "//input[@name='Пароль']")  # Поле пароля
    
    # Поля для авторизации
    FIELD_EMAIL = (By.XPATH, "//input[@name='name']")  # Поле email на странице логина
    FIELD_PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # Поле пароля на странице логина
    
    # Кнопка "Войти"
    BUTTON_ENTRANCE = (By.XPATH, ".//button[contains(text(),'Войти')]")

    # Булки
    INSCRIPTION_BREAD = (By.XPATH, "//h2[contains(text(),'Булки')]")
    
    # Надпись "Выход"
    BUTTON_LOGOUT = (By.XPATH, './/button[contains(text(),"Выход")]')

    # Кнопка "Выход"
    BUTTON_LOGOUTBIG = (By.XPATH, "//button[contains(@class, 'Account_button') and text()='Выход']")
    
    # Перейти в профиль
    INSCRIPTION_PROFILE = (By.XPATH, './/a[@href="/account/profile"]')
    
    # Кнопка-надпись "Войти"
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")
    
    # Кнопка "Оформить заказ"
    BUTTON_ARRANGE_ORDER = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")
    
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[@href='/']")
    
    # Разделы конструктора
    BREAD_SECTION = (By.XPATH, ".//span[contains(text(), 'Булки')]")
    SAUCES_SECTION = (By.XPATH, ".//span[contains(text(), 'Соусы')]")
    TOPPINGS_SECTION = (By.XPATH, ".//span[contains(text(), 'Начинки')]")
    
    # Активный раздел
    ACTIVE_SECTION = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]')
    
    # Сообщения об ошибках
    ERROR_ACCOUNT_EXISTS = (By.XPATH, ".//p[contains(text(), 'Такой пользователь уже существует')]")
    ERROR_PASSWORD = (By.XPATH, '//div[contains(@class, "input_status_error")]')
    
    # Кнопка "Восстановить пароль"
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")

    # Восстановить страницу
    RECOVERY_FIELD_EMAIL = (By.XPATH, "//input[@name='name']")
    
    # Надпись "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, '//a[text()="Зарегистрироваться" and @href="/register"]')

    # Кнопка "Оформить заказ" (появляется после авторизации)
    BUTTON_CHECKOUT = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    # Кнопка-надпись "Войти" на странице регистрации
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти' and @href='/login']")
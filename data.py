class Credantial:
    """Учетные данные для тестирования"""
    NAME = 'Людмила'
    EMAIL = 'Ludmila_Valeeva_28_748@yandex.ru'
    PASSWORD = '238abcd'

class StringValues:
    """Строковые значения"""
    READY_STATE_COMPLETE = "complete"
    FUNCTION_SCOPE = "function"
    AUTOUse = "autouse"
    NAME = "name"
    EMAIL = "email"
    PASSWORD = "password"

class LogMessages:
    """Сообщения для логирования"""
    INSTALLING_CHROMEDRIVER = "Installing ChromeDriver..."
    CREATING_WEBDRIVER = "Creating WebDriver instance..."
    WEBDRIVER_CONFIGURED = "WebDriver configured successfully"
    WEBDRIVER_INIT_ERROR = "WebDriver initialization error: {}"
    WEBDRIVER_SETUP_TIMEOUT = "WebDriver setup timeout: {}"
    INVALID_CONFIGURATION = "Invalid configuration: {}"
    UNEXPECTED_ERROR = "Unexpected error in driver fixture: {}"
    QUITTING_WEBDRIVER = "Quitting WebDriver..."
    WEBDRIVER_QUIT_SUCCESS = "WebDriver quit successfully"
    DRIVER_QUIT_ERROR = "Error during driver quit: {}"
    CLEANUP_REDIRECT = "Cleanup: redirected to login page"
    WEBDRIVER_CLEANUP_ERROR = "WebDriver error during cleanup: {}"
    CRITICAL_CLEANUP_ERROR = "Critical cleanup error: {}"

class FixtureDescriptions:
    """Описания фикстур"""
    GENERATE_USER_DATA = "Фикстура для генерации новых данных пользователя."
    START_FROM_MAIN = "Фикстура для начала теста с главной страницы."
    START_FROM_LOGIN = "Фикстура для начала теста со страницы логина."
    START_FROM_REGISTER = "Фикстура для начала теста со страницы регистрации."
    REGISTERED_USER = "Фикстура для регистрации нового пользователя."
    AUTHENTICATED_USER = "Фикстура для аутентифицированного пользователя."
    START_FROM_MAIN_NOT_LOGIN = "Фикстура для начала теста с главной страницы без авторизации."
    LOGIN_EXISTING_USER = "Фикстура для логина существующего тестового пользователя."
    CLEANUP_AFTER_TEST = "Безопасная очистка после теста. Не маскирует ошибки."

class ExceptionTypes:
    """Типы исключений для импорта"""
    WEBDRIVER_EXCEPTION = "WebDriverException"
    SESSION_NOT_CREATED = "SessionNotCreatedException"
    TIMEOUT_EXCEPTION = "TimeoutException"
    INVALID_SESSION = "InvalidSessionIdException"
    NO_SUCH_WINDOW = "NoSuchWindowException"
    NO_SUCH_ELEMENT = "NoSuchElementException"
    ELEMENT_CLICK_INTERCEPTED = "ElementClickInterceptedException"
    STALE_ELEMENT = "StaleElementReferenceException"

class ModulePaths:
    """Пути к модулям"""
    PARENT_DIR = ".."
    CURRENT_DIR = "."

class ChromeOptions:
    """Настройки Chrome Options"""
    # Можно добавить часто используемые опции
    DISABLE_EXTENSIONS = "disable-extensions"
    DISABLE_GPU = "disable-gpu"
    NO_SANDBOX = "no-sandbox"
    DISABLE_DEV_SHM = "disable-dev-shm-usage"

class TestData:
    # Увеличенные таймауты для стабильности
    PAGE_LOAD_TIMEOUT = 120  # 120 секунд для загрузки страниц
    EXPLICIT_WAIT = 60       # 60 секунд для явных ожиданий
    IMPLICIT_WAIT = 20       # 20 секунд для неявных ожиданий
    SCRIPT_TIMEOUT = 60      # 60 секунд для выполнения скриптов
    DEFAULT_NAME = "Людмила"
    
    # Дополнительные настройки для стабильности
    RETRY_ATTEMPTS = 3       # Количество попыток повторения операций
    RETRY_DELAY = 5          # Задержка между попытками в секундах
    
class SectionTitles:
    """Названия разделов конструктора"""
    BREAD = "Булки"
    SAUCES = "Соусы"
    TOPPINGS = "Начинки"

class ErrorMessages:
    """Сообщения об ошибках для всех тестов"""
    # Общие ошибки
    ELEMENT_NOT_FOUND = "Элемент не найден"
    ELEMENT_NOT_VISIBLE = "Элемент не виден"
    PAGE_NOT_LOADED = "Страница не загрузилась"
    TIMEOUT = "Таймаут ожидания элемента"
    URL_MISMATCH = "Ожидался URL: {}, но получен: {}"
    NAVIGATION_FAILED = "Навигация не удалась"
    BUTTON_NOT_CLICKABLE = "Кнопка не доступна для клика"
    FORM_NOT_LOADED = "Форма не загрузилась"
    NETWORK_ERROR = "Сетевая ошибка при загрузке страницы"
    BROWSER_ERROR = "Ошибка браузера"
    DRIVER_ERROR = "Ошибка инициализации драйвера"
    
    # Ошибки аутентификации
    LOGIN_FAILED = "Не удалось выполнить вход"
    SECTION_NOT_ACTIVE = "Раздел не стал активным"
    PERSONAL_ACCOUNT_NOT_FOUND = "Кнопка личного кабинета не найдена"
    LOGOUT_BUTTON_NOT_FOUND = "Кнопка выхода не найдена"
    LOGIN_BUTTON_NOT_FOUND = "Кнопка входа не найдена"
    CHECKOUT_BUTTON_NOT_FOUND = "Кнопка 'Оформить заказ' не найдена"
    RECOVERY_PAGE_NOT_LOADED = "Страница восстановления пароля не загрузилась"
    MAIN_PAGE_NOT_LOADED = "Главная страница не загрузилась после авторизации"
    LOGIN_PAGE_NOT_LOADED = "Страница логина не загрузилась"
    PROFILE_PAGE_NOT_LOADED = "Страница профиля не загрузилась"
    LOGIN_PAGE_NOT_LOADED_AFTER_REG = "Страница логина не загрузилась после регистрации"
    MAIN_PAGE_NOT_LOADED_AFTER_LOGIN = "Главная страница не загрузилась после входа"
    
    # Ошибки конструктора
    BREAD_SECTION_ERROR = "Ошибка активации раздела 'Булки'"
    SAUCES_SECTION_ERROR = "Ошибка активации раздела 'Соусы'"
    TOPPINGS_SECTION_ERROR = "Ошибка активации раздела 'Начинки'"
    
    # Ошибки навигации
    CONSTRUCTOR_TRANSITION_FAILED = "Переход через конструктор не удался"
    LOGO_TRANSITION_FAILED = "Переход через логотип не удался"
    PROFILE_TRANSITION_FAILED = "Переход в профиль не удался"
    
    # Ошибки регистрации
    REGISTRATION_FAILED = "Регистрация не удалась"
    EXISTING_ACCOUNT_ERROR = "Ошибка существующего аккаунта"
    PASSWORD_VALIDATION_ERROR = "Ошибка валидации пароля"
    NAME_REQUIRED_ERROR = "Требуется указать имя"
    PASSWORD_REQUIRED_ERROR = "Требуется указать пароль"

class SuccessMessages:
    """Сообщения об успешном выполнении"""
    LOGIN_SUCCESS = "Вход выполнен успешно"
    LOGOUT_SUCCESS = "Выход выполнен успешно"
    REGISTRATION_SUCCESS = "Регистрация завершена успешно"
    NAVIGATION_SUCCESS = "Навигация выполнена успешно"
    SECTION_ACTIVATED = "Раздел успешно активирован"
    CONSTRUCTOR_TRANSITION_SUCCESS = "Переход через конструктор выполнен успешно"
    LOGO_TRANSITION_SUCCESS = "Переход через логотип выполнен успешно" 
    PROFILE_TRANSITION_SUCCESS = "Переход в профиль выполнен успешно"
    EXISTING_ACCOUNT_DETECTED = "Обнаружен существующий аккаунт"
    VALIDATION_ERROR_CORRECT = "Ошибка валидации обработана корректно"
    PAGE_LOADED_SUCCESS = "Страница успешно загрузилась"
    ELEMENT_FOUND_SUCCESS = "Элемент успешно найден"

class ScreenshotNames:
    """Имена скриншотов для ошибок"""
    # Скриншоты конструктора
    BREAD_ERROR = "chapter_bread_error.png"
    FILLINGS_ERROR = "chapter_fillings_error.png"
    SAUCE_ERROR = "chapter_sauce_error.png"
    
    # Скриншоты аутентификации
    MAIN_PAGE_ERROR = "main_page_error.png"
    LOGIN_PAGE_ERROR = "login_page_error.png"
    REGISTRATION_ERROR = "registration_error.png"
    RECOVERY_ERROR = "recovery_error.png"
    LOGOUT_ERROR = "logout_error.png"
    CRITICAL_ERROR = "critical_error.png"
    UNKNOWN_ERROR = "unknown_error.png"
    NETWORK_ERROR = "network_error.png"
    TIMEOUT_ERROR = "timeout_error.png"
    
    # Скриншоты навигации
    CONSTRUCTOR_ERROR = "constructor_error.png"
    LOGO_ERROR = "logo_error.png"
    PROFILE_ERROR = "profile_error.png"
    
    # Скриншоты регистрации
    REGISTRATION_TEST_ERROR = "registration_test_error.png"
    EXISTING_ACCOUNT_ERROR = "existing_account_error.png"
    NO_NAME_ERROR = "no_name_error.png"
    PASSWORD_ERROR = "password_error.png"
    NO_PASSWORD_ERROR = "no_password_error.png"

# Дополнительные классы для обработки ошибок
class RetryConfig:
    """Конфигурация повторных попыток"""
    MAX_ATTEMPTS = 3
    DELAY_BETWEEN_ATTEMPTS = 2
    BACKOFF_FACTOR = 1.5

class NetworkConditions:
    """Настройки сетевых условий"""
    SLOW_NETWORK_TIMEOUT = 180
    NORMAL_NETWORK_TIMEOUT = 120
    FAST_NETWORK_TIMEOUT = 60

class TestPasswords:
    """Тестовые пароли для валидации"""
    SHORT_PASSWORD = "short"  # Короткий пароль для теста валидации
    VALID_PASSWORD = "valid_password_123"  # Валидный пароль
    EMPTY_PASSWORD = ""  # Пустой пароль

class TestNames:
    """Тестовые имена"""
    DEFAULT_TEST_NAME = "Тест"
    EMPTY_NAME = ""
    LONG_NAME = "Очень длинное имя пользователя которое превышает лимит"

class TestEmails:
    """Тестовые email адреса"""
    VALID_EMAIL_PREFIX = "test_user"  # Префикс для генерации email
    INVALID_EMAIL = "invalid-email"  # Невалидный email
    EMPTY_EMAIL = ""  # Пустой email

class AssertionMessages:
    """Сообщения для утверждений (assert)"""
    SECTION_VALIDATION = "Ожидался раздел '{}', но получен: {}"
    BREAD_SECTION_EXPECTED = ErrorMessages.SECTION_NOT_ACTIVE + " Ожидался раздел '{}', но получен: {}"
    ACTIVE_SECTION_NOT_DISPLAYED = "Активный раздел не отображается"
    SECTION_TITLE_NOT_DISPLAYED = "Заголовок раздела не отображается"

class TestDescriptions:
    """Описания тестовых действий"""
    FILLINGS_SECTION_TEST = "Тест активации раздела 'Начинки' в конструкторе."
    SAUCE_SECTION_TEST = "Тест активации раздела 'Соусы' в конструкторе"
    LOGIN_ACTION = "логинимся"

class TimeoutValues:
    """Значения таймаутов"""
    DEFAULT_TIMEOUT = 10
    SAUCE_SECTION_TIMEOUT = 10
    BREAD_SECTION_TIMEOUT = 10
    GENERAL_TIMEOUT = 15
    LONG_TIMEOUT = 20
    SHORT_TIMEOUT = 5

class Comments:
    """Текстовые комментарии для кода"""
    WAIT_FOR_SAUCES = "Дождаться видимости раздела 'Соусы' и прокрутить к нему"
    SCROLL_FOR_VISIBILITY = "Прокрутить к элементу для гарантии видимости"
    WAIT_FOR_BREAD = "Дождаться видимости раздела 'Булки' и прокрутить к нему"
    CHECK_ACTIVE_SECTION = "Проверить наличие активного раздела"
    CHECK_BREAD_TAB = "Проверить что активная вкладка соответствует разделу 'Булки'"
    CHECK_BREAD_TITLE = "Дополнительная проверка: убедиться что заголовок раздела 'Булки' виден"

class AssertionTemplates:
    """Шаблоны для утверждений"""
    SECTION_VALIDATION_TEMPLATE = "Ожидался раздел '{}', но получен: {}"

class SectionNames:
    """Названия разделов для использования в тексте"""
    SAUCES = "Соусы"
    BREAD = "Булки"
    TOPPINGS = "Начинки"

class ScriptTemplates:
    """Шаблоны JavaScript скриптов"""
    SCROLL_INTO_VIEW = "arguments[0].scrollIntoView({block: 'center'});"
    DOCUMENT_READY_STATE = "return document.readyState"

class DocumentStates:
    """Состояния документа"""
    COMPLETE = "complete"
    LOADING = "loading"
    INTERACTIVE = "interactive"
    # Добавляем метод для проверки готовности
    @staticmethod
    def is_complete(state):
        return state == DocumentStates.COMPLETE

class SleepDurations:
    """Длительности пауз"""
    SHORT_PAUSE = 1
    MEDIUM_PAUSE = 2
    LONG_PAUSE = 3
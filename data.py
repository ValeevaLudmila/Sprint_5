class Credantial:
    """Учетные данные для тестирования"""
    NAME = 'Людмила'
    EMAIL = 'Ludmila_Valeeva_28_748@yandex.ru'
    PASSWORD = '238abcd'

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
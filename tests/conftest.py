import sys
import os
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import (WebDriverException, TimeoutException, 
                                      InvalidSessionIdException, NoSuchWindowException,
                                      NoSuchElementException, ElementClickInterceptedException,
                                      StaleElementReferenceException)

# Добавляем корневую директорию в PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Теперь можно импортировать модули
from data import TestData, StringValues, LogMessages, ChromeOptions, ExceptionTypes
from locators import Locators
from curl import Urls

@pytest.fixture(scope=StringValues.FUNCTION_SCOPE)
def driver():
    """Фикстура создает и настраивает драйвер с полной конфигурацией."""
    import logging
    logger = logging.getLogger(__name__)
    
    chrome_options = Options()
    # ... опции ...
    
    driver = None
    try:
        logger.info("Installing ChromeDriver...")
        service = Service(ChromeDriverManager().install())
        
        logger.info("Creating WebDriver instance...")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Конфигурация драйвера...
        logger.info("WebDriver configured successfully")
        
        yield driver
        
    except (WebDriverException, SessionNotCreatedException) as e:
        logger.error(f"WebDriver initialization error: {e}")
        pytest.fail(f"WebDriver initialization failed: {e}")
        
    except TimeoutException as e:
        logger.error(f"WebDriver setup timeout: {e}")
        pytest.fail(f"WebDriver setup timeout: {e}")
        
    except ValueError as e:
        logger.error(f"Invalid configuration: {e}")
        pytest.fail(f"Invalid configuration: {e}")
        
    except Exception as e:
        # Только для логирования непредвиденных ошибок
        logger.critical(f"Unexpected error in driver fixture: {e}")
        # Пробрасываем выше - не маскируем критические ошибки
        raise
        
    finally:
        if driver:
            try:
                logger.info("Quitting WebDriver...")
                driver.quit()
                logger.info("WebDriver quit successfully")
            except Exception as e:
                logger.warning(f"Error during driver quit: {e}")
                # Не падаем на ошибках закрытия

@pytest.fixture
def generate_new_user_data():
    # Фикстура для генерации новых данных пользователя.
    generator = EmailPasswordGenerator()
    email, password = generator.generate()
    return {
        'name': TestData.DEFAULT_NAME,
        'email': email,
        'password': password
    }

@pytest.fixture
def start_from_main_page(driver):
    # Фикстура для начала теста с главной страницы.
    driver.get(Urls.MAIN_SITE)
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(EC.url_to_be(Urls.MAIN_SITE))
    return driver

@pytest.fixture
def start_from_login_page(driver):
    # Фикстура для начала теста со страницы логина.
    driver.get(Urls.LOGIN_SITE)
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(EC.url_to_be(Urls.LOGIN_SITE))
    return driver

@pytest.fixture
def start_from_register_page(driver):
    # Фикстура для начала теста со страницы регистрации.
    driver.get(Urls.REGISTER_SITE)
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER)
    )
    return driver

@pytest.fixture
def registered_user(driver):
    """
    Фикстура для регистрации нового пользователя.
    Гарантированно возвращает валидные учетные данные.
    """
    # Генерируем новые данные ДО попытки регистрации
    generator = EmailPasswordGenerator()
    email, password = generator.generate()
    
    # Переходим на страницу регистрации
    driver.get(Urls.REGISTER_SITE)
    
    # Ждем загрузки формы
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER)
    )
    
    # Заполняем форму регистрации
    driver.find_element(*Locators.FIELD_NAME_REGISTER).send_keys(TestData.DEFAULT_NAME)
    driver.find_element(*Locators.FIELD_EMAIL_REGISTER).send_keys(email)
    driver.find_element(*Locators.FIELD_PASSWORD_REGISTER).send_keys(password)
    driver.find_element(*Locators.BUTTON_REGISTER).click()
    
    # Ждем успешной регистрации (переход на страницу логина)
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.url_to_be(Urls.LOGIN_SITE)
    )
    
    return email, password

@pytest.fixture
def authenticated_user(driver):
    # Фикстура для аутентифицированного пользователя.
    login_user(driver, Credantial.EMAIL, Credantial.PASSWORD)
    return {
        "email": Credantial.EMAIL,
        "password": Credantial.PASSWORD
    }

@pytest.fixture
def start_from_main_not_login(driver):
    # Фикстура для начала теста с главной страницы без авторизации.
    driver.get(Urls.MAIN_SITE)
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.visibility_of_element_located(Locators.THE_SIGN_IN_TO_ACCOUNT_BUTTON)
    )
    return driver

@pytest.fixture
def login_existing_user(driver):
    # Фикстура для логина существующего тестового пользователя.
    def _login_user(email=Credantial.EMAIL, password=Credantial.PASSWORD):
        # Переходим на страницу логина
        driver.get(Urls.LOGIN_SITE)
        
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.visibility_of_element_located(Locators.FIELD_EMAIL_LOGIN),
            ErrorMessages.LOGIN_PAGE_NOT_LOADED
        )
        
        # Заполняем форму логина
        email_field = driver.find_element(*Locators.FIELD_EMAIL_LOGIN)
        email_field.clear()
        email_field.send_keys(email)
        
        password_field = driver.find_element(*Locators.FIELD_PASSWORD_LOGIN)
        password_field.clear()
        password_field.send_keys(password)
        
        # Кликаем кнопку входа
        driver.find_element(*Locators.BUTTON_ENTRANCE).click()
        
        # Ждем перехода на главную страницу
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.url_to_be(Urls.MAIN_SITE),
            ErrorMessages.MAIN_PAGE_NOT_LOADED_AFTER_LOGIN
        )
        
        return email, password
    
    return _login_user

@pytest.fixture(scope="function", autouse=True)
def cleanup_after_test(driver):
    """
    Безопасная очистка после теста. Не маскирует ошибки.
    """
    # Действия перед тестом
    logger = logging.getLogger(__name__)
    
    yield
    
    # Действия после теста
    try:
        # Простая и надежная очистка
        if driver and driver.current_url != Urls.LOGIN_SITE:
            driver.get(Urls.LOGIN_SITE)
            logger.info("Cleanup: redirected to login page")
            
    except WebDriverException as e:
        # Логируем ошибки WebDriver, но не маскируем
        logger.warning(f"WebDriver error during cleanup: {e}")
        
    except Exception as e:
        # Критические ошибки логируем и пробрасываем
        logger.error(f"Critical cleanup error: {e}")
        raise



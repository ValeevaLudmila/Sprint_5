import sys
import os
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import (
    WebDriverException,
    TimeoutException,
    InvalidSessionIdException,
    NoSuchWindowException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    SessionNotCreatedException
)

# Добавляем корневую директорию в PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Теперь можно импортировать модули
from data import (
    TestData, StringValues, LogMessages, ExceptionTypes,
    Credantial, ErrorMessages
)
from locators import Locators
from curl import Urls
from generating_logins import EmailPasswordGenerator
from helpers import login_user

logger = logging.getLogger(__name__)


@pytest.fixture(scope=StringValues.FUNCTION_SCOPE)
def driver():
    """Фикстура создает и настраивает драйвер с полной конфигурацией."""
    chrome_options = Options()
    # Базовые опции Chrome для стабильности
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    
    driver_instance = None
    try:
        logger.info(LogMessages.INSTALLING_CHROMEDRIVER)
        service = Service(ChromeDriverManager().install())
        
        logger.info(LogMessages.CREATING_WEBDRIVER)
        driver_instance = webdriver.Chrome(service=service, options=chrome_options)
        
        # Конфигурация драйвера
        driver_instance.implicitly_wait(TestData.IMPLICIT_WAIT)
        driver_instance.set_page_load_timeout(TestData.PAGE_LOAD_TIMEOUT)
        driver_instance.set_script_timeout(TestData.SCRIPT_TIMEOUT)
        
        logger.info(LogMessages.WEBDRIVER_CONFIGURED)
        yield driver_instance
        
    except (WebDriverException, SessionNotCreatedException) as e:
        error_msg = LogMessages.WEBDRIVER_INIT_ERROR.format(e)
        logger.error(error_msg)
        pytest.fail(error_msg)
        
    except TimeoutException as e:
        error_msg = LogMessages.WEBDRIVER_SETUP_TIMEOUT.format(e)
        logger.error(error_msg)
        pytest.fail(error_msg)
        
    except ValueError as e:
        error_msg = LogMessages.INVALID_CONFIGURATION.format(e)
        logger.error(error_msg)
        pytest.fail(error_msg)
        
    except Exception as e:
        error_msg = LogMessages.UNEXPECTED_ERROR.format(e)
        logger.critical(error_msg)
        raise
        
    finally:
        if driver_instance:
            try:
                logger.info(LogMessages.QUITTING_WEBDRIVER)
                driver_instance.quit()
                logger.info(LogMessages.WEBDRIVER_QUIT_SUCCESS)
            except Exception as e:
                logger.warning(LogMessages.DRIVER_QUIT_ERROR.format(e))


@pytest.fixture
def generate_new_user_data():
    """Фикстура для генерации новых данных пользователя."""
    generator = EmailPasswordGenerator()
    email, password = generator.generate()
    return {
        StringValues.NAME: TestData.DEFAULT_NAME,
        StringValues.EMAIL: email,
        StringValues.PASSWORD: password
    }


@pytest.fixture
def start_from_main_page(driver):
    """Фикстура для начала теста с главной страницы."""
    driver.get(Urls.MAIN_SITE)
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.url_to_be(Urls.MAIN_SITE)
    )
    return driver


@pytest.fixture
def start_from_login_page(driver):
    """Фикстура для начала теста со страницы логина."""
    driver.get(Urls.LOGIN_SITE)
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.url_to_be(Urls.LOGIN_SITE)
    )
    return driver


@pytest.fixture
def start_from_register_page(driver):
    """Фикстура для начала теста со страницы регистрации."""
    driver.get(Urls.REGISTER_SITE)
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER)
    )
    return driver


@pytest.fixture
def registered_user(driver):
    """Фикстура для регистрации нового пользователя."""
    generator = EmailPasswordGenerator()
    email, password = generator.generate()
    
    driver.get(Urls.REGISTER_SITE)
    
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER)
    )
    
    driver.find_element(*Locators.FIELD_NAME_REGISTER).send_keys(TestData.DEFAULT_NAME)
    driver.find_element(*Locators.FIELD_EMAIL_REGISTER).send_keys(email)
    driver.find_element(*Locators.FIELD_PASSWORD_REGISTER).send_keys(password)
    driver.find_element(*Locators.BUTTON_REGISTER).click()
    
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.url_to_be(Urls.LOGIN_SITE)
    )
    
    return email, password


@pytest.fixture
def authenticated_user(driver):
    """Фикстура для аутентифицированного пользователя."""
    login_user(driver, Credantial.EMAIL, Credantial.PASSWORD)
    return {
        StringValues.EMAIL: Credantial.EMAIL,
        StringValues.PASSWORD: Credantial.PASSWORD
    }


@pytest.fixture
def start_from_main_not_login(driver):
    """Фикстура для начала теста с главной страницы без авторизации."""
    driver.get(Urls.MAIN_SITE)
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.visibility_of_element_located(Locators.THE_SIGN_IN_TO_ACCOUNT_BUTTON)
    )
    return driver


@pytest.fixture
def login_existing_user(driver):
    """Фикстура для логина существующего тестового пользователя."""
    def _login_user(email=Credantial.EMAIL, password=Credantial.PASSWORD):
        driver.get(Urls.LOGIN_SITE)
        
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.visibility_of_element_located(Locators.FIELD_EMAIL_LOGIN),
            ErrorMessages.LOGIN_PAGE_NOT_LOADED
        )
        
        email_field = driver.find_element(*Locators.FIELD_EMAIL_LOGIN)
        email_field.clear()
        email_field.send_keys(email)
        
        password_field = driver.find_element(*Locators.FIELD_PASSWORD_LOGIN)
        password_field.clear()
        password_field.send_keys(password)
        
        driver.find_element(*Locators.BUTTON_ENTRANCE).click()
        
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.url_to_be(Urls.MAIN_SITE),
            ErrorMessages.MAIN_PAGE_NOT_LOADED_AFTER_LOGIN
        )
        
        return email, password
    
    return _login_user


@pytest.fixture(scope=StringValues.FUNCTION_SCOPE, autouse=True)
def cleanup_after_test(driver):
    """Безопасная очистка после теста."""
    yield
    
    try:
        if driver and driver.current_url != Urls.LOGIN_SITE:
            driver.get(Urls.LOGIN_SITE)
            logger.info(LogMessages.CLEANUP_REDIRECT)
            
    except WebDriverException as e:
        logger.warning(LogMessages.WEBDRIVER_CLEANUP_ERROR.format(e))
        
    except Exception as e:
        logger.error(LogMessages.CRITICAL_CLEANUP_ERROR.format(e))
        raise
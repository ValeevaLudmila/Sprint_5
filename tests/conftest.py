import sys
import os
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (TimeoutException, InvalidSessionIdException, 
                                      NoSuchWindowException, NoSuchElementException,
                                      ElementClickInterceptedException, StaleElementReferenceException,
                                      WebDriverException)
from selenium.webdriver.common.by import By

# Добавляем корневую директорию в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators import Locators
from data import Credantial, TestData
from generating_logins import EmailPasswordGenerator
from curl import Urls
from helpers import login_user

# Настройка логирования
logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def driver():
    """Фикстура создает и настраивает драйвер с полной конфигурацией."""
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Добавьте для стабильности сети
    chrome_options.add_argument("--disable-features=VizDisplayCompositor")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Убираем опознавательные признаки автоматизации
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        driver.implicitly_wait(TestData.IMPLICIT_WAIT)
        driver.set_page_load_timeout(TestData.PAGE_LOAD_TIMEOUT)
        driver.set_script_timeout(TestData.SCRIPT_TIMEOUT)
        
        yield driver
        
    except WebDriverException as e:
        logger.error("Ошибка инициализации WebDriver: %s", e)
        pytest.fail(f"Не удалось инициализировать WebDriver: {e}")
    finally:
        try:
            if 'driver' in locals() and driver:
                driver.quit()
        except (InvalidSessionIdException, NoSuchWindowException, WebDriverException):
            pass
@pytest.fixture
def generate_new_user_data():
    """Фикстура для генерации новых данных пользователя."""
    generator = EmailPasswordGenerator()
    email, password = generator.generate()
    return {
        'name': TestData.DEFAULT_NAME,
        'email': email,
        'password': password
    }

@pytest.fixture
def start_from_main_page(driver):
    """Фикстура для начала теста с главной страницы."""
    driver.get(Urls.MAIN_SITE)
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(EC.url_to_be(Urls.MAIN_SITE))
    return driver

@pytest.fixture
def start_from_login_page(driver):
    """Фикстура для начала теста со страницы логина."""
    driver.get(Urls.LOGIN_SITE)
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(EC.url_to_be(Urls.LOGIN_SITE))
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
    driver.get(Urls.REGISTER_SITE)
    
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER)
    )
    
    # Генерируем новые данные
    generator = EmailPasswordGenerator()
    email, password = generator.generate()
    
    # Заполняем форму регистрации
    driver.find_element(*Locators.FIELD_NAME_REGISTER).send_keys(TestData.DEFAULT_NAME)
    driver.find_element(*Locators.FIELD_EMAIL_REGISTER).send_keys(email)
    driver.find_element(*Locators.FIELD_PASSWORD_REGISTER).send_keys(password)
    driver.find_element(*Locators.BUTTON_REGISTER).click()
    
    # Обрабатываем результат регистрации
    try:
        # Ждем перехода на страницу логина (успешная регистрация)
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(EC.url_to_be(Urls.LOGIN_SITE))
        return email, password
    except TimeoutException:
        # Если остались на странице регистрации, проверяем наличие ошибки
        try:
            driver.find_element(*Locators.ERROR_ACCOUNT_EXISTS)
            # Пользователь уже существует, используем тестовые данные
            return Credantial.EMAIL, Credantial.PASSWORD
        except NoSuchElementException:
            # Другая ошибка регистрации
            raise

@pytest.fixture
def authenticated_user(driver):
    """Фикстура для аутентифицированного пользователя."""
    login_user(driver, Credantial.EMAIL, Credantial.PASSWORD)
    return {
        "email": Credantial.EMAIL,
        "password": Credantial.PASSWORD
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
    """Автоматическая очистка после каждого теста."""
    yield
    
    # После каждого теста пытаемся выйти из системы
    try:
        # Переходим в личный кабинет если мы на авторизованной странице
        if "/account" not in driver.current_url and driver.current_url != Urls.LOGIN_SITE:
            driver.get(Urls.MAIN_SITE)
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
            ).click()
            
            # Ждем загрузки профиля и выходим
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(Locators.BUTTON_LOGOUT)
            ).click()
            
            # Ждем перехода на страницу логина
            WebDriverWait(driver, 5).until(
                EC.url_to_be(Urls.LOGIN_SITE)
            )
    except (TimeoutException, NoSuchElementException, WebDriverException):
        # Игнорируем ошибки при cleanup
        pass




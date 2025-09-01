import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, InvalidSessionIdException, NoSuchWindowException
from selenium.webdriver.common.by import By
from curl import *
from locators import Locators
from data import Credantial
from generating_logins import EmailPasswordGenerator

@pytest.fixture(scope="function")
def driver():
    # Фикстура создает и закрывает драйвер после каждого теста
    from selenium.webdriver.chrome.options import Options
    
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    
    try:
        driver.quit()
    except (InvalidSessionIdException, NoSuchWindowException):
        pass

@pytest.fixture
def generate_new_user_data():
    # Фикстура для генерации новых данных пользователя
    generator = EmailPasswordGenerator()
    email, password = generator.generate()
    return {
        'name': 'Людмила',
        'email': email,
        'password': password
    }

@pytest.fixture
def start_from_main_page(driver):
    try:
        driver.get(main_site)
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
        return driver
    except Exception as e:
        print(f"Ошибка: {e}")
        driver.save_screenshot("main_page_error.png")
        raise

@pytest.fixture
def register_new_account(driver):
    try:
        # Переходим на страницу регистрации
        driver.get(register_site)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER)
        )
        
        name = Credantial.name
        email = Credantial.email
        password = Credantial.password
        
        print(f"Регистрируем пользователя: email={email}, password={password}")
        
        # Заполняем поля
        name_field = driver.find_element(*Locators.FIELD_NAME_REGISTER)
        name_field.send_keys(name)
        print("Заполнено поле Имя")
        
        email_field = driver.find_element(*Locators.FIELD_EMAIL_REGISTER)
        email_field.send_keys(email)
        print("Заполнено поле Email")
        
        password_field = driver.find_element(*Locators.FIELD_PASSWORD_REGISTER)
        password_field.send_keys(password)
        print("Заполнено поле Пароль")
        
        register_button = driver.find_element(*Locators.BUTTON_REGISTER)
        register_button.click()
        
        
        try:
            # Если регистрация успешна - ждем перехода на страницу логина
            WebDriverWait(driver, 5).until(
                EC.url_to_be(login_site)
            )
            print("Регистрация успешна, перешли на страницу логина")
            
            # Авторизуемся
            email_field = driver.find_element(*Locators.FIELD_EMAIL_LOGIN)
            email_field.send_keys(email)
            
            password_field = driver.find_element(*Locators.FIELD_PASSWORD_LOGIN)
            password_field.send_keys(password)
            
            driver.find_element(*Locators.BUTTON_ENTRANCE).click()
            
            # Ждем перехода на главную страницу после авторизации
            WebDriverWait(driver, 10).until(
                EC.url_to_be(main_site)
            )
            print("Успешная авторизация после регистрации")
            
        except TimeoutException:
            # Если остались на странице регистрации - проверяем ошибку
            try:
                error_element = driver.find_element(*Locators.ERROR_ACCOUNT_EXISTS)
                print("Пользователь уже существует, нажимаем 'Войти'")
                
                # Нажимаем кнопку "Войти" на странице регистрации
                login_link = driver.find_element(*Locators.LOGIN_LINK_REGISTER)
                login_link.click()
                
                # Ждем загрузки страницы логина
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(Locators.FIELD_EMAIL_LOGIN)
                )
                print("Перешли на страницу логина")
                
                # Авторизуемся
                email_field = driver.find_element(*Locators.FIELD_EMAIL_LOGIN)
                email_field.send_keys(email)
                
                password_field = driver.find_element(*Locators.FIELD_PASSWORD_LOGIN)
                password_field.send_keys(password)
                
                driver.find_element(*Locators.BUTTON_ENTRANCE).click()
                
                # Ждем перехода на главную страницу
                WebDriverWait(driver, 10).until(
                    EC.url_to_be(main_site)
                )
                print("Успешная авторизация существующего пользователя")
                
            except Exception as inner_e:
                print(f"Неизвестная ошибка при регистрации: {inner_e}")
                driver.save_screenshot("registration_unknown_error.png")
                raise
        
        return email, password
        
    except Exception as e:
        print(f"Ошибка при регистрации: {e}")
        driver.save_screenshot("registration_error.png")
        raise

@pytest.fixture
def login_existing_user(driver):
    # Фикстура для авторизации существующего пользователя
    def _login(email, password):
        try:
            driver.get(login_site)
            WebDriverWait(driver, 10).until(
                EC.url_to_be(login_site)
            )
            
            driver.find_element(*Locators.BUTTON_ENTRANCE).click()
            
            # Ждем перехода на главную страницу
            WebDriverWait(driver, 10).until(
                EC.url_to_be(main_site)
            )
            
            print(f"Успешная авторизация пользователя: {email}")
            
        except Exception as e:
            print(f"Ошибка при авторизации: {e}")
            driver.save_screenshot("login_error.png")
            raise
    
    return _login

@pytest.fixture
def start_from_main_not_login(driver):
    # Фикстура для начала теста с главной страницы без авторизации
    try:
        driver.get(main_site)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.THE_SIGN_IN_TO_ACCOUNT_BUTTON)
        )
        return driver
    except Exception as e:
        print(f"Ошибка: {e}")
        driver.save_screenshot("main_page_error.png")
        raise

@pytest.fixture
def start_from_login_page(driver):
    """Фикстура для начала теста со страницы логина"""
    try:
        driver.get(login_site)
        WebDriverWait(driver, 10).until(
            EC.url_to_be(login_site)
        )
        return driver
    except Exception as e:
        print(f"Ошибка: {e}")
        driver.save_screenshot("login_page_error.png")
        raise
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, InvalidSessionIdException, NoSuchWindowException
from selenium.webdriver.common.by import By
from curl import *
from locators import Locators
from data import Credantial

@pytest.fixture
def driver():
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
def start_from_main_page(driver):
    try:
        driver.get(main_site)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.THE_SIGN_IN_TO_ACCOUNT_BUTTON))
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
        
        # Ждем загрузки страницы регистрации
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER)
        )
        
        # Используем данные из Credantial
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
        
        # Нажимаем кнопку регистрации
        register_button = driver.find_element(*Locators.BUTTON_REGISTER)
        register_button.click()
        
        # Ждем либо успешной регистрации, либо ошибки
        try:
            # Если регистрация успешна - ждем перехода
            WebDriverWait(driver, 5).until(
                lambda driver: login_site in driver.current_url or main_site in driver.current_url
            )
            print("Регистрация успешна")
            
        except TimeoutException:
            # Если остались на странице регистрации - проверяем ошибку
            try:
                error_element = driver.find_element(*Locators.ERROR_ACCOUNT_EXISTS)
                print("Пользователь уже существует, нажимаем 'Войти'")
                
                # Нажимаем кнопку "Войти" на странице регистрации
                login_link = driver.find_element(*Locators.LOGIN_LINK)
                login_link.click()
                
                # Ждем загрузки страницы логина
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(Locators.FIELD_EMAIL)
                )
                print("Перешли на страницу логина")
                
            except:
                print("Неизвестная ошибка при регистрации")
                driver.save_screenshot("registration_unknown_error.png")
                raise
        
        # ВСЕГДА переходим на главную страницу после регистрации/авторизации
        if driver.current_url != main_site:
            driver.get(main_site)
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.THE_SIGN_IN_TO_ACCOUNT_BUTTON)
            )
            print("Перешли на главную страницу")
        
        return email, password
        
    except Exception as e:
        print(f"Ошибка при регистрации: {e}")
        driver.save_screenshot("registration_error.png")
        raise

@pytest.fixture
def login_existing_user(driver):
    """Фикстура для авторизации существующего пользователя"""
    def _login(email, password):
        try:
            # Переходим на страницу логина
            driver.get(login_site)
            
            # Ждем загрузки страницы логина
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.FIELD_EMAIL)
            )
            
            # Заполняем форму
            email_field = driver.find_element(*Locators.FIELD_EMAIL)
            email_field.send_keys(email)
            
            password_field = driver.find_element(*Locators.FIELD_PASSWORD)
            password_field.send_keys(password)
            
            # Нажимаем кнопку входа
            driver.find_element(*Locators.BUTTON_ENTRANCE).click()
            
            # Ждем перехода на главную страницу
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"))
            )
            
            print(f"Успешная авторизация пользователя: {email}")
            
        except Exception as e:
            print(f"Ошибка при авторизации: {e}")
            driver.save_screenshot("login_error.png")
            raise
    
    return _login
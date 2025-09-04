import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from locators import Locators
from curl import Urls
from generating_logins import EmailPasswordGenerator
from data import Credantial, ErrorMessages, SuccessMessages, ScreenshotNames, TestNames, TestPasswords, StringValues

class TestRegistration:
    # Тесты функциональности регистрации
    
    def test_successful_registration(self, driver, generate_new_user_data):
        # Тест успешной регистрации нового аккаунта
        user_data = generate_new_user_data
        
        # 1. Переходим на страницу регистрации
        driver.get(Urls.REGISTER_SITE)
        
        # 2. Ждем загрузки формы регистрации
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER),
            ErrorMessages.FORM_NOT_LOADED
        )
        
        # 3. Заполняем поле Имя
        name_field = driver.find_element(*Locators.FIELD_NAME_REGISTER)
        name_field.clear()
        name_field.send_keys(user_data['name'])
        
        # 4. Заполняем поле Email
        email_field = driver.find_element(*Locators.FIELD_EMAIL_REGISTER)
        email_field.clear()
        email_field.send_keys(user_data['email'])
        
        # 5. Заполняем поле Пароль
        password_field = driver.find_element(*Locators.FIELD_PASSWORD_REGISTER)
        password_field.clear()
        password_field.send_keys(user_data['password'])
        
        # 6. Кликаем кнопку Зарегистрироваться
        register_button = driver.find_element(*Locators.BUTTON_REGISTER)
        register_button.click()
        
        # 7. Ждем перехода на страницу логина (после успешной регистрации)
        WebDriverWait(driver, 20).until(
            EC.url_to_be(Urls.LOGIN_SITE),
            ErrorMessages.LOGIN_PAGE_NOT_LOADED_AFTER_REG
        )
        
        # 8. Авторизуемся с только что созданными данными
        email_field = driver.find_element(*Locators.FIELD_EMAIL_LOGIN)
        email_field.clear()
        email_field.send_keys(user_data['email'])
        
        password_field = driver.find_element(*Locators.FIELD_PASSWORD_LOGIN)
        password_field.clear()
        password_field.send_keys(user_data['password'])
        
        driver.find_element(*Locators.BUTTON_ENTRANCE).click()
        
        # 9. Ждем перехода на главную страницу после авторизации
        WebDriverWait(driver, 20).until(
            EC.url_to_be(Urls.MAIN_SITE),
            ErrorMessages.MAIN_PAGE_NOT_LOADED_AFTER_LOGIN
        )
        
        # 10. Проверяем что пользователь авторизован (кнопка "Оформить заказ")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.BUTTON_CHECKOUT),
            ErrorMessages.CHECKOUT_BUTTON_NOT_FOUND
        )
        
        # 11. Проверяем URL
        assert driver.current_url == Urls.MAIN_SITE, ErrorMessages.REGISTRATION_FAILED

    def test_existing_account_registration(self, driver):
        # Тест попытки регистрации существующего аккаунта
        # 1. Переходим на страницу регистрации
        driver.get(Urls.REGISTER_SITE)
        
        # 2. Ждем загрузки формы регистрации
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER),
            ErrorMessages.FORM_NOT_LOADED
        )
        
        # 3. Заполняем форму данными существующего пользователя
        driver.find_element(*Locators.FIELD_NAME_REGISTER).send_keys(Credantial.NAME)
        driver.find_element(*Locators.FIELD_EMAIL_REGISTER).send_keys(Credantial.EMAIL)
        driver.find_element(*Locators.FIELD_PASSWORD_REGISTER).send_keys(Credantial.PASSWORD)
        
        # 4. Нажимаем кнопку Зарегистрироваться
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        
        # 5. Ждем сообщение об ошибке
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ERROR_ACCOUNT_EXISTS),
            ErrorMessages.EXISTING_ACCOUNT_ERROR
        )
        
        # 6. Проверяем что остались на странице регистрации
        assert Urls.REGISTER_SITE in driver.current_url, ErrorMessages.EXISTING_ACCOUNT_ERROR

    def test_registration_without_name(self, driver):
        # Тест регистрации без имени
        # 1. Переходим на страницу регистрации
        driver.get(Urls.REGISTER_SITE)
        
        # 2. Ждем загрузки формы регистрации
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER),
            ErrorMessages.FORM_NOT_LOADED
        )
        
        # 3. Генерируем email и password
        generator = EmailPasswordGenerator()
        email, password = generator.generate()
        
        # 4. Заполняем только email и password (имя пропускаем)
        driver.find_element(*Locators.FIELD_EMAIL_REGISTER).send_keys(email)
        driver.find_element(*Locators.FIELD_PASSWORD_REGISTER).send_keys(password)
        
        # 5. Нажимаем кнопку Зарегистрироваться
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        
        # 6. Проверяем что остались на странице регистрации
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.REGISTER_SITE),
            ErrorMessages.NAME_REQUIRED_ERROR
        )
        assert driver.current_url == Urls.REGISTER_SITE, ErrorMessages.NAME_REQUIRED_ERROR

    def test_password_validation_error(self, driver):
        # Тест ошибки при коротком пароле
        # 1. Переходим на страницу регистрации
        driver.get(Urls.REGISTER_SITE)
        
        # 2. Ждем загрузки формы регистрации
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER),
            ErrorMessages.FORM_NOT_LOADED
        )
        
        # 3. Генерируем email
        generator = EmailPasswordGenerator()
        email, _ = generator.generate()
        
        # 4. Заполняем форму
        driver.find_element(*Locators.FIELD_NAME_REGISTER).send_keys(TestNames.DEFAULT_TEST_NAME)
        driver.find_element(*Locators.FIELD_EMAIL_REGISTER).send_keys(email)
        driver.find_element(*Locators.FIELD_PASSWORD_REGISTER).send_keys(TestPasswords.SHORT_PASSWORD)
        
        # 5. Нажимаем кнопку Зарегистрироваться
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        
        # 6. Ждем ошибку пароля
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ERROR_PASSWORD),
            ErrorMessages.PASSWORD_VALIDATION_ERROR
        )
        
        # 7. Проверяем что остались на странице регистрации
        assert Urls.REGISTER_SITE in driver.current_url, ErrorMessages.PASSWORD_VALIDATION_ERROR

    def test_registration_without_password(self, driver):
        # Тест регистрации без пароля
        # 1. Переходим на страницу регистрации
        driver.get(Urls.REGISTER_SITE)
        
        # 2. Ждем загрузки формы регистрации
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER),
            ErrorMessages.FORM_NOT_LOADED
        )
        
        # 3. Генерируем email
        generator = EmailPasswordGenerator()
        email, _ = generator.generate()
        
        # 4. Заполняем только имя и email
        driver.find_element(*Locators.FIELD_NAME_REGISTER).send_keys(TestNames.DEFAULT_TEST_NAME)
        driver.find_element(*Locators.FIELD_EMAIL_REGISTER).send_keys(email)
        
        # 5. Нажимаем кнопку Зарегистрироваться
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        
        # 6. Проверяем что остались на странице регистрации
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.REGISTER_SITE),
            ErrorMessages.PASSWORD_REQUIRED_ERROR
        )
        assert driver.current_url == Urls.REGISTER_SITE, ErrorMessages.PASSWORD_REQUIRED_ERROR
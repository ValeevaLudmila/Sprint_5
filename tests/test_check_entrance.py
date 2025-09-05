import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import TestData, ErrorMessages, SuccessMessages, ScriptTemplates, DocumentStates, StringValues
from curl import Urls
from helpers import login_user

class TestAuthentication:
    
    def test_entrance_by_main_button(self, start_from_main_page):
        # Тест входа через главную кнопку
        # Переходим на главную страницу
        driver = start_from_main_page
    
        # Ждем полной загрузки страницы
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            lambda d: d.execute_script(ScriptTemplates.DOCUMENT_READY_STATE) 
            == DocumentStates.COMPLETE
        )
    
        login_button = WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.element_to_be_clickable(Locators.THE_SIGN_IN_TO_ACCOUNT_BUTTON),
            ErrorMessages.BUTTON_NOT_CLICKABLE
        )
        login_button.click()
    
        # Проверяем переход на страницу логина
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.url_to_be(Urls.LOGIN_SITE),
            ErrorMessages.LOGIN_PAGE_NOT_LOADED
        )
    
        # Проверяем, что форма логина отображается
        email_field = WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.visibility_of_element_located(Locators.FIELD_EMAIL_LOGIN),
            ErrorMessages.ELEMENT_NOT_VISIBLE
        )
    
        assert driver.current_url == Urls.LOGIN_SITE, ErrorMessages.URL_MISMATCH.format(
            Urls.LOGIN_SITE, driver.current_url
        )
        assert email_field.is_displayed(), ErrorMessages.ELEMENT_NOT_VISIBLE

    def test_password_recovery_page_access(self, start_from_main_page):
        # Тест доступа к странице восстановления пароля.
        driver = start_from_main_page

        # Переходим на страницу восстановления пароля
        driver.get(Urls.FORGOT_PASSWORD_SITE)
        
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.url_to_be(Urls.FORGOT_PASSWORD_SITE),
            ErrorMessages.RECOVERY_PAGE_NOT_LOADED
        )

        assert driver.current_url == Urls.FORGOT_PASSWORD_SITE, ErrorMessages.URL_MISMATCH.format(
            Urls.FORGOT_PASSWORD_SITE, driver.current_url
        )

    def test_entrance_from_recovery_page(self, start_from_main_page, registered_user):
        # Тест входа в систему со страницы восстановления пароля.
        driver = start_from_main_page
        email, password = registered_user
        
        # Переходим на страницу восстановления пароля
        driver.get(Urls.FORGOT_PASSWORD_SITE)
        
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.url_to_be(Urls.FORGOT_PASSWORD_SITE),
            ErrorMessages.RECOVERY_PAGE_NOT_LOADED
        )

        # Находим и кликаем кнопку "Войти" на странице восстановления
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON),
            ErrorMessages.LOGIN_BUTTON_NOT_FOUND
        ).click()

        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.url_to_be(Urls.LOGIN_SITE),
            ErrorMessages.LOGIN_PAGE_NOT_LOADED
        )

        # Заполняем форму авторизации
        email_field = driver.find_element(*Locators.FIELD_EMAIL_LOGIN)
        email_field.send_keys(email)

        password_field = driver.find_element(*Locators.FIELD_PASSWORD_LOGIN)
        password_field.send_keys(password)

        driver.find_element(*Locators.BUTTON_ENTRANCE).click()

        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.url_to_be(Urls.MAIN_SITE),
            ErrorMessages.MAIN_PAGE_NOT_LOADED
        )
        
        assert driver.current_url == Urls.MAIN_SITE, ErrorMessages.URL_MISMATCH.format(
            Urls.MAIN_SITE, driver.current_url
        )

    def test_user_logout(self, start_from_main_page, registered_user):
        # Тест выхода пользователя из системы.
        driver = start_from_main_page
        email, password = registered_user
    
        # Логинимся сначала
        login_user(driver, email, password)
    
        # Переходим в личный кабинет
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
        ).click()

        # Ждем загрузки профиля
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.url_contains(Urls.ACCOUNT_SITE)
        )

        # Выходим
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.element_to_be_clickable(Locators.BUTTON_LOGOUT)
        ).click()

        # После выхода должны быть на странице логина
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.url_to_be(Urls.LOGIN_SITE)
        )

        assert driver.current_url == Urls.LOGIN_SITE
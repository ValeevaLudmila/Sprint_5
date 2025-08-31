from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credantial

# test_check_entrance.py
class TestBigMainButton:
    def test_check_entrance_by_big_button(self, start_from_main_page, register_new_account, login_existing_user):
        driver = start_from_main_page
        email, password = register_new_account
        
        try:
            print(f"Авторизуемся как: email={email}, password={password}")
            
            # Если остались на странице регистрации - выполняем авторизацию
            if "register" in driver.current_url:
                login_existing_user(email, password)
            else:
                # Ждем кнопку "Войти в аккаунт" и кликаем
                WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable(Locators.THE_SIGN_IN_TO_ACCOUNT_BUTTON)
                ).click()

                # Ждем появления полей формы логина
                WebDriverWait(driver, 15).until(
                    EC.visibility_of_element_located(Locators.FIELD_EMAIL)
                )
                
                # Заполняем форму
                email_field = driver.find_element(*Locators.FIELD_EMAIL)
                email_field.send_keys(email)

                password_field = driver.find_element(*Locators.FIELD_PASSWORD)
                password_field.send_keys(password)

                driver.find_element(*Locators.BUTTON_ENTRANCE).click()

                # Ожидание перехода на главную страницу
                WebDriverWait(driver, 15).until(
                    EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"))
                )
            
            # Проверяем что мы на основной странице сайта
            assert driver.current_url == main_site, f"Ожидался {main_site}, но получили {driver.current_url}"
            print("Успешная авторизация!")
            
        except Exception as e:
            print(f"Ошибка в тесте: {e}")
            print(f"Текущий URL при ошибке: {driver.current_url}")
            driver.save_screenshot("big_button_error.png")
            raise

class TestCheckRegister:
    def test_login_password_recovery(self, start_from_main_page):
        driver = start_from_main_page

        try:
            # Переходим на страницу восстановления пароля
            driver.get(forgot_password_site)
            
            # Ждем загрузки страницы восстановления
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]"))
            )

            # Проверяем что мы на странице восстановления пароля
            assert "forgot-password" in driver.current_url, f"Ожидалась страница восстановления, но URL: {driver.current_url}"
            print("Тест восстановления пароля пройден успешно!")
            
        except Exception as e:
            driver.save_screenshot("recovery_error.png")
            raise e


class TestCheckEntranceFromRecoveryPage:
    def test_button_inscription_login(self, start_from_main_page, register_new_account):
        driver = start_from_main_page
        email, password = register_new_account  # Используем зарегистрированного пользователя

        try:
            # Если мы на странице регистрации, переходим на главную
            if "register" in driver.current_url:
                driver.get(main_site)
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(Locators.THE_SIGN_IN_TO_ACCOUNT_BUTTON)
                )
                print("Перешли на главную страницу после регистрации")
            
            print(f"Начальный URL: {driver.current_url}")
            print(f"Используем пользователя: email={email}")
            
            # 1. Переходим на страницу логина через кнопку "Войти в аккаунт"
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.THE_SIGN_IN_TO_ACCOUNT_BUTTON)
            ).click()
            print("Клик на 'Войти в аккаунт'")

            # 2. Ждем загрузки страницы логина
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(Locators.FIELD_EMAIL)
            )
            print("Страница логина загружена")

            # 3. Переходим на страницу восстановления пароля
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/forgot-password']"))
            ).click()
            print("Клик на 'Восстановить пароль'")

            # 4. Ждем загрузки страницы восстановления
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]"))
            )
            print("Страница восстановления загружена")

            # 5. Находим и кликаем кнопку "Войти" на странице восстановления
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
            ).click()
            print("Клик на 'Войти' со страницы восстановления")

            # 6. Ждем появления полей формы авторизации
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(Locators.FIELD_EMAIL)
            )
            print("Форма авторизации загружена")

            # 7. Заполняем форму авторизации
            email_field = driver.find_element(*Locators.FIELD_EMAIL)
            email_field.send_keys(email)
            print("Заполнено поле Email")

            password_field = driver.find_element(*Locators.FIELD_PASSWORD)
            password_field.send_keys(password)
            print("Заполнено поле Пароль")

            driver.find_element(*Locators.BUTTON_ENTRANCE).click()
            print("Клик на кнопку Войти")

            # 8. Ожидание перехода на главную страницу
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"))
            )

            # 9. Проверяем что мы на основной странице сайта
            assert driver.current_url == main_site, f"Ожидался {main_site}, но получили {driver.current_url}"
            print("Тест завершен успешно!")

        except Exception as e:
            print(f"Ошибка в тесте: {e}")
            print(f"Текущий URL при ошибке: {driver.current_url}")
            driver.save_screenshot("recovery_login_error.png")
            raise e

def test_check_loging_out(start_from_main_page, register_new_account):
    driver = start_from_main_page
    email, password = register_new_account  # Используем зарегистрированного пользователя

    try:
        print(f"Начальный URL: {driver.current_url}")
        print(f"Используем пользователя: email={email}")
        
        # 1. Переходим на страницу логина
        driver.get(login_site)
        
        # 2. Ждем загрузки страницы логина
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.FIELD_EMAIL)
        )
        print("Страница логина загружена")

        # 3. Заполняем форму авторизации
        email_field = driver.find_element(*Locators.FIELD_EMAIL)
        email_field.send_keys(email)
        print("Заполнено поле Email")

        password_field = driver.find_element(*Locators.FIELD_PASSWORD)
        password_field.send_keys(password)
        print("Заполнено поле Пароль")

        driver.find_element(*Locators.BUTTON_ENTRANCE).click()
        print("Клик на кнопку Войти")

        # 4. Ждем перехода на главную страницу
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"))
        )
        print("Успешный переход на главную страницу")

        # 5. Кликаем "Личный кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
        ).click()
        print("Клик на 'Личный кабинет'")

        # 6. Ждем загрузки страницы профиля
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/account/profile')]"))
        )
        print("Страница профиля загружена")

        # 7. Кликаем "Выход"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Выход')]"))
        ).click()
        print("Клик на 'Выход'")

        # 8. Ждем перехода на страницу логина
        WebDriverWait(driver, 15).until(
            EC.url_to_be(login_site)
        )
        print("Успешный переход на страницу логина после выхода")

        # 9. Проверяем что мы на странице логина
        assert driver.current_url == login_site, f"Ожидался URL: {login_site}, но получен: {driver.current_url}"
        print("Тест выхода из аккаунта завершен успешно!")

    except Exception as e:
        print(f"Ошибка в тесте: {e}")
        print(f"Текущий URL при ошибке: {driver.current_url}")
        driver.save_screenshot("logout_error.png")
        raise
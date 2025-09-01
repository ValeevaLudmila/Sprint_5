from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credantial

class TestBigMainButton:
    def test_check_entrance_by_big_button(self, start_from_main_page, register_new_account):
        driver = start_from_main_page
        email, password = register_new_account
        
        try:
            print(f"Проверяем авторизацию для: email={email}")
            
            assert driver.current_url == main_site, f"Ожидался {main_site}, но получили {driver.current_url}"
            
            # Проверяем что кнопка "Оформить заказ" видна (признак успешной авторизации)
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.BUTTON_CHECKOUT)
            )
            print("Кнопка 'Оформить заказ' найдена - вход успешен!")
            
            print("Успешная авторизация через главную кнопку!")
            
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
            WebDriverWait(driver, 25).until(
                EC.url_to_be(forgot_password_site)
            )

            # Проверяем что мы на странице восстановления пароля
            assert driver.current_url == forgot_password_site, f"Ожидалась {forgot_password_site}, но URL: {driver.current_url}"
            print("Тест восстановления пароля пройден успешно!")
            
        except Exception as e:
            driver.save_screenshot("recovery_error.png")
            raise e

class TestCheckEntranceFromRecoveryPage:
    def test_button_inscription_login(self, start_from_main_page, register_new_account):
        driver = start_from_main_page
        email, password = register_new_account

        try:
            print(f"Начальный URL: {driver.current_url}")
            print(f"Используем пользователя: email={email}")
            
            # Выходим из аккаунта, чтобы протестировать вход через восстановление
            # Переходим в личный кабинет
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
            ).click()
            
            # Ждем загрузки страницы профиля
            WebDriverWait(driver, 25).until(
                EC.url_contains("/account")
            )
            
            # Выходим из аккаунта
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Выход')]"))
            ).click()
            
            # Ждем перехода на страницу логина
            WebDriverWait(driver, 25).until(
                EC.url_to_be(login_site)
            )
            
            # 1. Переходим на страницу восстановления пароля напрямую
            driver.get(forgot_password_site)
            
            # 2. Ждем загрузки страницы восстановления
            WebDriverWait(driver, 25).until(
                EC.url_to_be(forgot_password_site)
            )
            print("Страница восстановления загружена")

            # 3. Находим и кликаем кнопку "Войти" на странице восстановления
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
            ).click()
            print("Клик на 'Войти' со страницы восстановления")

            # 4. Ждем перехода на страницу логина
            WebDriverWait(driver, 15).until(
                EC.url_to_be(login_site)
            )
            print("Перешли на страницу логина")

            # 5. Заполняем форму авторизации
            email_field = driver.find_element(*Locators.FIELD_EMAIL_LOGIN)
            email_field.send_keys(email)
            print("Заполнено поле Email")

            password_field = driver.find_element(*Locators.FIELD_PASSWORD_LOGIN)
            password_field.send_keys(password)
            print("Заполнено поле Пароль")

            driver.find_element(*Locators.BUTTON_ENTRANCE).click()
            print("Клик на кнопку Войти")

            # 6. Ожидание перехода на главную страницу
            WebDriverWait(driver, 25).until(
                EC.url_to_be(main_site)
            )
            
            # Дополнительная проверка успешного входа
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.BUTTON_CHECKOUT)
            )
            print("Кнопка 'Оформить заказ' найдена - вход успешен!")

            # 7. Проверяем что мы на основной странице сайта
            assert driver.current_url == main_site, f"Ожидался {main_site}, но получили {driver.current_url}"
            print("Тест входа через страницу восстановления завершен успешно!")

        except Exception as e:
            print(f"Ошибка в тесте: {e}")
            print(f"Текущий URL при ошибке: {driver.current_url}")
            driver.save_screenshot("recovery_login_error.png")
            raise e

def test_check_loging_out(start_from_main_page, register_new_account):
    driver = start_from_main_page
    email, password = register_new_account

    try:
        print(f"Начальный URL: {driver.current_url}")
        print(f"Используем пользователя: email={email}")
        
        assert driver.current_url == main_site, f"Ожидался {main_site}, но получили {driver.current_url}"
        
        # Проверяем что кнопка "Оформить заказ" видна
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUTTON_CHECKOUT)
        )
        print("Кнопка 'Оформить заказ' найдена - вход успешен!")
        
        # 1. Кликаем "Личный кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
        ).click()
        print("Клик на 'Личный кабинет'")

        # 2. Ждем загрузки страницы профиля
        WebDriverWait(driver, 25).until(
            EC.url_contains("/account")
        )
        print("Страница профиля загружена")

        # 3. Кликаем "Выход"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Выход')]"))
        ).click()
        print("Клик на 'Выход'")

        # 4. Ждем перехода на страницу логина
        WebDriverWait(driver, 25).until(
            EC.url_to_be(login_site)
        )
        print("Успешный переход на страницу логина после выхода")

        # 5. Проверяем что мы на странице логина
        assert driver.current_url == login_site, f"Ожидалась {login_site}, но получен: {driver.current_url}"
        print("Тест выхода из аккаунта завершен успешно!")

    except Exception as e:
        print(f"Ошибка в тесте: {e}")
        print(f"Текущий URL при ошибке: {driver.current_url}")
        driver.save_screenshot("logout_error.png")
        raise
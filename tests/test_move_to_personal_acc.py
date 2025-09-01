import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locators
from curl import *

class TestTransitionByConstructor:
    def test_check_transition_by_constructor(self, start_from_main_page, register_new_account):
        driver = start_from_main_page
        email, password = register_new_account
        
        try:
            # Убедимся что мы на главной странице и авторизованы
            WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.BUTTON_CHECKOUT)
            )

            # Нажать на кнопку "Личный кабинет"
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
            ).click()

            # Ждем загрузки страницы профиля
            WebDriverWait(driver, 10).until(
                EC.url_contains("/account")
            )

            # Кликаем по кнопке "Конструктор"
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
            ).click()

            # Ждем переход на главную страницу
            WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

            # Проверяем что мы на основной странице
            assert driver.current_url == main_site
            print("Тест перехода через конструктор выполнен успешно!")

        except Exception as e:
            print(f"Ошибка в тесте: {e}")
            driver.save_screenshot("constructor_error.png")
            raise


class TestTransitionByLogo:
    def test_transition_by_logo(self, start_from_main_page, register_new_account):
        driver = start_from_main_page
        email, password = register_new_account
        
        try:
            # Убедимся что мы на главной странице и авторизованы
            WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.BUTTON_CHECKOUT)
            )

            # Нажать на кнопку "Личный кабинет"
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
            ).click()

            # Ждем загрузки страницы профиля
            WebDriverWait(driver, 15).until(
                EC.url_contains("/account")
            )

            # Кликаем по логотипу (исправленный локатор)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.LOGO)
            ).click()

            # Ждем перехода на главную страницу
            WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

            # Проверяем что мы на основной странице
            assert driver.current_url == main_site
            print("Тест перехода через логотип выполнен успешно!")

        except Exception as e:
            print(f"Ошибка в тесте: {e}")
            driver.save_screenshot("logo_error.png")
            raise


class TestCheckPageProfile:
    def test_transition_before_profile(self, start_from_main_page, register_new_account):
        driver = start_from_main_page
        email, password = register_new_account
        
        try:
            # Убедимся что мы на главной странице и авторизованы
            WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.BUTTON_CHECKOUT)
            )

            # Нажать на кнопку "Личный кабинет"
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
            ).click()

            # Ждем переход на страницу профиля
            WebDriverWait(driver, 10).until(
                EC.url_to_be(profile_site)
            )

            # Проверить что мы на странице профиля
            assert driver.current_url == profile_site
            print("Тест перехода в профиль выполнен успешно!")

        except Exception as e:
            print(f"Ошибка в тесте: {e}")
            driver.save_screenshot("profile_error.png")
            raise
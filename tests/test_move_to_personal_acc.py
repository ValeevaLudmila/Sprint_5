import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from locators import Locators
from curl import *
from data import ErrorMessages

class TestPersonalAccountNavigation:
    """Тесты навигации личного кабинета"""
    
    def test_constructor_transition(self, start_from_main_page, register_new_account):
        """
        Тест перехода на главную страницу через кнопку 'Конструктор'
        """
        driver = start_from_main_page
        email, password = register_new_account
        
        # Убедимся что мы на главной странице и авторизованы
        WebDriverWait(driver, 10).until(
            EC.url_to_be(main_site),
            ErrorMessages.MAIN_PAGE_NOT_LOADED
        )
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUTTON_CHECKOUT),
            ErrorMessages.ELEMENT_NOT_VISIBLE
        )

        # Нажать на кнопку "Личный кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT),
            ErrorMessages.BUTTON_NOT_CLICKABLE
        ).click()

        # Ждем загрузки страницы профиля
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account"),
            ErrorMessages.PROFILE_PAGE_NOT_LOADED
        )

        # Кликаем по кнопке "Конструктор"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON),
            ErrorMessages.BUTTON_NOT_CLICKABLE
        ).click()

        # Ждем переход на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_to_be(main_site),
            ErrorMessages.MAIN_PAGE_NOT_LOADED
        )

        # Проверяем что мы на основной странице
        assert driver.current_url == main_site, ErrorMessages.CONSTRUCTOR_TRANSITION_FAILED

    def test_logo_transition(self, start_from_main_page, register_new_account):
        """
        Тест перехода на главную страницу через логотип
        """
        driver = start_from_main_page
        email, password = register_new_account
        
        # Убедимся что мы на главной странице и авторизованы
        WebDriverWait(driver, 10).until(
            EC.url_to_be(main_site),
            ErrorMessages.MAIN_PAGE_NOT_LOADED
        )
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUTTON_CHECKOUT),
            ErrorMessages.ELEMENT_NOT_VISIBLE
        )

        # Нажать на кнопку "Личный кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT),
            ErrorMessages.BUTTON_NOT_CLICKABLE
        ).click()

        # Ждем загрузки страницы профиля
        WebDriverWait(driver, 15).until(
            EC.url_contains("/account"),
            ErrorMessages.PROFILE_PAGE_NOT_LOADED
        )

        # Кликаем по логотипу
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGO),
            ErrorMessages.BUTTON_NOT_CLICKABLE
        ).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_to_be(main_site),
            ErrorMessages.MAIN_PAGE_NOT_LOADED
        )

        # Проверяем что мы на основной странице
        assert driver.current_url == main_site, ErrorMessages.LOGO_TRANSITION_FAILED

    def test_profile_transition(self, start_from_main_page, register_new_account):
        """
        Тест перехода в личный кабинет
        """
        driver = start_from_main_page
        email, password = register_new_account
        
        # Убедимся что мы на главной странице и авторизованы
        WebDriverWait(driver, 10).until(
            EC.url_to_be(main_site),
            ErrorMessages.MAIN_PAGE_NOT_LOADED
        )
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUTTON_CHECKOUT),
            ErrorMessages.ELEMENT_NOT_VISIBLE
        )

        # Нажать на кнопку "Личный кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT),
            ErrorMessages.BUTTON_NOT_CLICKABLE
        ).click()

        # Ждем переход на страницу профиля
        WebDriverWait(driver, 10).until(
            EC.url_to_be(profile_site),
            ErrorMessages.PROFILE_PAGE_NOT_LOADED
        )

        # Проверить что мы на странице профиля
        assert driver.current_url == profile_site, ErrorMessages.PROFILE_TRANSITION_FAILED
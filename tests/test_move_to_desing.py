from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Credantial, SectionTitles, ErrorMessages, ScreenshotNames

class TestConstructorNavigation:
    """Тесты навигации по разделам конструктора"""
    
    def test_bread_section_activation(self, start_from_main_page, register_new_account):
        """
        Тест активации раздела 'Булки' в конструкторе
        """
        driver = start_from_main_page
        # driver.maximize_window()  ← УДАЛЕНО!

        # Сначала регистрируем/логинимся
        email, password = register_new_account

        # Нажать на раздел "Соусы"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCES_SECTION),
            ErrorMessages.ELEMENT_NOT_FOUND
        ).click()

        # Нажать на раздел "Булки"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BREAD_SECTION),
            ErrorMessages.ELEMENT_NOT_FOUND
        ).click()

        # Проверить наличие активного раздела
        active_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION),
            ErrorMessages.SECTION_NOT_ACTIVE
        )
        assert active_element.is_displayed(), ErrorMessages.SECTION_NOT_ACTIVE

        # Проверить что активная вкладка соответствует разделу "Булки"
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION),
            ErrorMessages.ELEMENT_NOT_FOUND
        )
        assert SectionTitles.BREAD in active_tab.text, \
            f"Ожидался раздел '{SectionTitles.BREAD}', но получен: {active_tab.text}"

    def test_fillings_section_activation(self, start_from_main_page, register_new_account):
        """
        Тест активации раздела 'Начинки' в конструкторе
        """
        driver = start_from_main_page
        # driver.maximize_window()  ← УДАЛЕНО!

        # Сначала регистрируем/логинимся
        email, password = register_new_account

        # Нажать на раздел "Начинки"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.TOPPINGS_SECTION),
            ErrorMessages.ELEMENT_NOT_FOUND
        ).click()

        # Проверить наличие активного раздела
        active_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION),
            ErrorMessages.SECTION_NOT_ACTIVE
        )
        assert active_element.is_displayed(), ErrorMessages.SECTION_NOT_ACTIVE

        # Проверить что активная вкладка соответствует разделу "Начинки"
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION),
            ErrorMessages.ELEMENT_NOT_FOUND
        )
        assert SectionTitles.TOPPINGS in active_tab.text, \
            f"Ожидался раздел '{SectionTitles.TOPPINGS}', но получен: {active_tab.text}"

    def test_sauce_section_activation(self, start_from_main_page, register_new_account):
        """
        Тест активации раздела 'Соусы' в конструкторе
        """
        driver = start_from_main_page
        # driver.maximize_window()  ← УДАЛЕНО!

        # Сначала регистрируем/логинимся
        email, password = register_new_account

        # Нажать на раздел "Соусы"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCES_SECTION),
            ErrorMessages.ELEMENT_NOT_FOUND
        ).click()

        # Проверить наличие активного раздела
        active_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION),
            ErrorMessages.SECTION_NOT_ACTIVE
        )
        assert active_element.is_displayed(), ErrorMessages.SECTION_NOT_ACTIVE

        # Проверить что активная вкладка соответствует разделу "Соусы"
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION),
            ErrorMessages.ELEMENT_NOT_FOUND
        )
        assert SectionTitles.SAUCES in active_tab.text, \
            f"Ожидался раздел '{SectionTitles.SAUCES}', но получен: {active_tab.text}"
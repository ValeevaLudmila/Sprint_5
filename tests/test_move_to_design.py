from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from curl import Urls
from locators import Locators
from data import Credantial, SectionTitles, ErrorMessages, ScreenshotNames, TestData

class TestConstructorNavigation:
    
    def test_bread_section_activation(self, start_from_main_page, authenticated_user):
        driver = start_from_main_page
        email, password = authenticated_user

        # Явное ожидание загрузки страницы
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.presence_of_element_located((By.TAG_NAME, "body")),
            ErrorMessages.PAGE_NOT_LOADED
        )

        # Дождаться видимости раздела "Соусы" и прокрутить к нему
        sauces_section = WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.visibility_of_element_located(Locators.SAUCES_SECTION),
            ErrorMessages.ELEMENT_NOT_VISIBLE
        )
    
        # Прокрутить к элементу для гарантии видимости
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sauces_section)
    
        # Явное ожидание кликабельности и клик
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.element_to_be_clickable(Locators.SAUCES_SECTION),
            ErrorMessages.BUTTON_NOT_CLICKABLE
        ).click()

        # Краткая пауза для анимации
        import time
        time.sleep(1)

        # Дождаться видимости раздела "Булки" и прокрутить к нему
        bread_section = WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.visibility_of_element_located(Locators.BREAD_SECTION),
            ErrorMessages.ELEMENT_NOT_VISIBLE
        )
    
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", bread_section)
    
        # Явное ожидание кликабельности и клик
        WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.element_to_be_clickable(Locators.BREAD_SECTION),
            ErrorMessages.BUTTON_NOT_CLICKABLE
        ).click()

        # Пауза для применения изменений
        time.sleep(1)

        # Проверить наличие активного раздела
        active_element = WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION),
            ErrorMessages.SECTION_NOT_ACTIVE
        )
    
        assert active_element.is_displayed(), ErrorMessages.SECTION_NOT_ACTIVE

    # Проверить что активная вкладка соответствует разделу "Булки"
        active_tab = WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION),
            ErrorMessages.ELEMENT_NOT_FOUND
        )
    
        assert SectionTitles.BREAD in active_tab.text, \
            ErrorMessages.SECTION_NOT_ACTIVE + f" Ожидался раздел '{SectionTitles.BREAD}', но получен: {active_tab.text}"

        # Дополнительная проверка: убедиться что заголовок раздела "Булки" виден
        bread_title = WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']")),
            ErrorMessages.SECTION_NOT_ACTIVE
        )
    
        assert bread_title.is_displayed(), ErrorMessages.SECTION_NOT_ACTIVE    

    def test_fillings_section_activation(self, start_from_main_page, authenticated_user):
        """Тест активации раздела 'Начинки' в конструкторе."""
        driver = start_from_main_page
        email, password = authenticated_user

        # Ждем загрузки и кликаем на раздел "Начинки"
        toppings_section = WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.element_to_be_clickable(Locators.TOPPINGS_SECTION),
            ErrorMessages.BUTTON_NOT_CLICKABLE
        )
        toppings_section.click()

        # Проверяем активацию раздела
        active_tab = WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION),
            ErrorMessages.SECTION_NOT_ACTIVE
        )
    
        # Проверяем заголовок раздела
        toppings_title = WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Начинки']")),
            ErrorMessages.SECTION_NOT_ACTIVE
        )
    
        # Основные проверки
        assert SectionTitles.TOPPINGS in active_tab.text, \
            f"Ожидался раздел '{SectionTitles.TOPPINGS}', но получен: {active_tab.text}"
        assert toppings_title.is_displayed()

    def test_sauce_section_activation(self, start_from_main_page, authenticated_user):
        """Тест активации раздела 'Соусы' в конструкторе"""
        driver = start_from_main_page
        # driver.maximize_window()  ← УДАЛЕНО!

        # Сначала регистрируем/логинимся
        email, password = authenticated_user

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
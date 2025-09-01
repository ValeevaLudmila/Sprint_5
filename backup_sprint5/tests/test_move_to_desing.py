from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestCheckChapterBread:
    def test_check_chapter_bread(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        try:
            # Нажать на раздел "Соусы"
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.SAUCES_SECTION)
            ).click()

            # Нажать на раздел "Булки"
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.BREAD_SECTION)
            ).click()

            # Проверить наличие активного раздела
            active_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(Locators.ACTIVE_SECTION)
            )
            assert active_element.is_displayed()

            # Проверить что активная вкладка соответствует разделу "Булки"
            active_tab = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.ACTIVE_SECTION)
            )
            assert "Булки" in active_tab.text

        except Exception as e:
            driver.save_screenshot("chapter_bread_error.png")
            raise e


class TestCheckChapterFillings:
    def test_check_chapter_fillings(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        try:
            # Нажать на раздел "Начинки"
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.TOPPINGS_SECTION)
            ).click()

            # Проверить наличие активного раздела
            active_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(Locators.ACTIVE_SECTION)
            )
            assert active_element.is_displayed()

            # Проверить что активная вкладка соответствует разделу "Начинки"
            active_tab = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.ACTIVE_SECTION)
            )
            assert "Начинки" in active_tab.text

        except Exception as e:
            driver.save_screenshot("chapter_fillings_error.png")
            raise e


class TestCheckChapterSauce:
    def test_check_chapter_sauce(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        try:
            # Нажать на раздел "Соусы"
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.SAUCES_SECTION)
            ).click()

            # Проверить наличие активного раздела
            active_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(Locators.ACTIVE_SECTION)
            )
            assert active_element.is_displayed()

            # Проверить что активная вкладка соответствует разделу "Соусы"
            active_tab = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.ACTIVE_SECTION)
            )
            assert "Соусы" in active_tab.text

        except Exception as e:
            driver.save_screenshot("chapter_sauce_error.png")
            raise e
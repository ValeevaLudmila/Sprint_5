import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import register_site
from generating_logins import EmailPasswordGenerator

@pytest.fixture
def register_new_account(driver):
    try:
        driver.get(register_site)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FIELD_NAME))

        generator = EmailPasswordGenerator()
        email, password = generator.generate()

        driver.find_element(*Locators.FIELD_NAME).send_keys("Людмила")
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTER).click()

        return driver, email, password
    except Exception as e:
        print(f"Ошибка: {e}")
        driver.save_screenshot("register_error.png")
        raise
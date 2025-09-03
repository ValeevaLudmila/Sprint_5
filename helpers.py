from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import Locators
from curl import Urls
from data import TestData

def login_user(driver, email: str, password: str):
    """Выполняет авторизацию пользователя."""
    driver.get(Urls.LOGIN_SITE)
    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.url_to_be(Urls.LOGIN_SITE)
    )

    # Заполняем поля
    email_field = driver.find_element(*Locators.FIELD_EMAIL_LOGIN)
    email_field.send_keys(email)
    
    password_field = driver.find_element(*Locators.FIELD_PASSWORD_LOGIN)
    password_field.send_keys(password)

    driver.find_element(*Locators.BUTTON_ENTRANCE).click()

    WebDriverWait(driver, TestData.EXPLICIT_WAIT).until(
        EC.url_to_be(Urls.MAIN_SITE)
    )
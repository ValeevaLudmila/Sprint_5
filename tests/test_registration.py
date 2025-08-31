import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import main_site, register_site
from generating_logins import EmailPasswordGenerator


class TestCheckNewRegister:
    def test_registration(self, driver, generate_new_user_data):
        """Тест успешной регистрации нового аккаунта"""
        user_data = generate_new_user_data
        
        try:
            print(f"Начинаем регистрацию пользователя: {user_data}")
            
            # 1. Переходим на страницу регистрации
            driver.get(register_site)
            print("Перешли на страницу регистрации")
            
            # 2. Ждем загрузки формы регистрации
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(Locators.FIELD_NAME)
            )
            print("Форма регистрации загружена")
            
            # 3. Заполняем поле Имя
            name_field = driver.find_element(*Locators.FIELD_NAME)
            name_field.clear()
            name_field.send_keys(user_data['name'])
            print("Заполнено поле Имя")
            
            # 4. Заполняем поле Email
            email_field = driver.find_element(*Locators.FIELD_EMAIL)
            email_field.clear()
            email_field.send_keys(user_data['email'])
            print("Заполнено поле Email")
            
            # 5. Заполняем поле Пароль
            password_field = driver.find_element(*Locators.FIELD_PASSWORD)
            password_field.clear()
            password_field.send_keys(user_data['password'])
            print("Заполнено поле Пароль")
            
            # 6. Кликаем кнопку Зарегистрироваться
            register_button = driver.find_element(*Locators.BUTTON_REGISTER)
            register_button.click()
            print("Нажата кнопка Зарегистрироваться")
            
            # 7. Ждем перехода на главную страницу
            WebDriverWait(driver, 20).until(
                EC.url_to_be(main_site)
            )
            print(f"Успешный переход на главную страницу: {driver.current_url}")
            
            # 8. Проверяем что пользователь авторизован
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(Locators.BUTTON_CHECKOUT)
            )
            print("Пользователь успешно авторизован")
            
            # 9. Проверяем URL
            assert driver.current_url == main_site
            print("Тест регистрации завершен успешно!")
            
        except Exception as e:
            print(f"Ошибка в тесте: {e}")
            print(f"Текущий URL: {driver.current_url}")
            driver.save_screenshot("registration_test_error.png")
            raise

@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingCreationExistingAccount:
    def test_existing_account(self, start_from_main_not_login):  # Добавлен параметр фикстуры
        driver = start_from_main_not_login

        # Жмем кнопку "Зарегистрироваться"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

        # Ждем загрузки формы регистрации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FIELD_NAME))

        # Ищем поле "Имя" и заполняем его
        driver.find_element(*Locators.FIELD_NAME).send_keys(Credantial.name)

        # Ищем поле "email" и заполняем его
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credantial.email)

        # Ищем поле "Пароль" и заполняем его
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credantial.password)

        # Нажимаем "Зарегистрироваться"
        driver.find_element(*Locators.BUTTON_REGISTER).click()

        # Ждем ошибку регистрации
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_ACCOUNT_EXISTS))


@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckRegisterNoName:
    def test_registration_no_name(self, start_from_main_not_login):  # Добавлен параметр фикстуры
        driver = start_from_main_not_login

        # Нажимаем по надписи "Зарегистрироваться"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

        # Ждем загрузки формы регистрации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FIELD_NAME))

        # Генерация email и password
        generator = EmailPasswordGenerator()
        email, password = generator.generate()

        # Ищем поле "email" и заполняем его (поле имени пропускаем)
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(email)

        # Ищем поле "Пароль" и заполняем его
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(password)

        # Жмем на кнопку "Зарегистрироваться"
        driver.find_element(*Locators.BUTTON_REGISTER).click()

        # Проверяем что остались на странице регистрации (из-за ошибки)
        WebDriverWait(driver, 10).until(EC.url_to_be(register_site))
        assert driver.current_url == register_site


@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingErrorPassword:
    def test_error_password(self, start_from_main_not_login):  # Добавлен параметр фикстуры
        driver = start_from_main_not_login

        # Жмем кнопку "Зарегистрироваться"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

        # Ждем загрузки формы регистрации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FIELD_NAME))

        # Найди поле "Имя" и заполни его
        driver.find_element(*Locators.FIELD_NAME).send_keys(Credantial.name)

        # Найди поле "email" и заполни его
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credantial.email)

        # Ищем поле "Пароль" и заполняем его слишком коротким паролем
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys("short")  # Короткий пароль

        # Жмем на кнопку "Зарегистрироваться"
        driver.find_element(*Locators.BUTTON_REGISTER).click()

        # Ждем ошибку пароля
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_PASSWORD))


@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingNoPassword:
    def test_no_password(self, start_from_main_not_login):  # Добавлен параметр фикстуры и переименован класс
        driver = start_from_main_not_login
        email = 'Ludmila_Valeeva_28_748@yandex.ru'

        # Жмем кнопку "Зарегистрироваться"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

        # Ждем загрузки формы регистрации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FIELD_NAME))

        # Найди поле "Имя" и заполни его
        driver.find_element(*Locators.FIELD_NAME).send_keys(Credantial.name)

        # Найди поле "email" и заполни его
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(email)

        # Пароль не заполняем (оставляем пустым)

        # Жмем на кнопку "Зарегистрироваться"
        driver.find_element(*Locators.BUTTON_REGISTER).click()

        # Проверяем что остались на странице регистрации (из-за ошибки)
        WebDriverWait(driver, 10).until(EC.url_to_be(register_site))
        assert driver.current_url == register_site

        driver.quit()
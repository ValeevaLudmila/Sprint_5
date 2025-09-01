import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import main_site, register_site, login_site  # Добавьте login_site
from generating_logins import EmailPasswordGenerator
from data import Credantial


class TestCheckNewRegister:
    def test_registration(self, driver, generate_new_user_data):
        # Тест успешной регистрации нового аккаунта
        user_data = generate_new_user_data
        
        try:
            print(f"Начинаем регистрацию пользователя: {user_data}")
            
            # 1. Переходим на страницу регистрации
            driver.get(register_site)
            print("Перешли на страницу регистрации")
            
            # 2. Ждем загрузки формы регистрации
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER)
            )
            print("Форма регистрации загружена")
            
            # 3. Заполняем поле Имя
            name_field = driver.find_element(*Locators.FIELD_NAME_REGISTER)
            name_field.clear()
            name_field.send_keys(user_data['name'])
            print("Заполнено поле Имя")
            
            # 4. Заполняем поле Email
            email_field = driver.find_element(*Locators.FIELD_EMAIL_REGISTER)
            email_field.clear()
            email_field.send_keys(user_data['email'])
            print("Заполнено поле Email")
            
            # 5. Заполняем поле Пароль
            password_field = driver.find_element(*Locators.FIELD_PASSWORD_REGISTER)
            password_field.clear()
            password_field.send_keys(user_data['password'])
            print("Заполнено поле Пароль")
            
            # 6. Кликаем кнопку Зарегистрироваться
            register_button = driver.find_element(*Locators.BUTTON_REGISTER)
            register_button.click()
            print("Нажата кнопка Зарегистрироваться")
            
            # 7. Ждем перехода на страницу логина (после успешной регистрации)
            WebDriverWait(driver, 20).until(
                EC.url_to_be(login_site)
            )
            print(f"Успешный переход на страницу логина: {driver.current_url}")
            
            # 8. Авторизуемся с только что созданными данными
            email_field = driver.find_element(*Locators.FIELD_EMAIL_LOGIN)
            email_field.clear()
            email_field.send_keys(user_data['email'])
            
            password_field = driver.find_element(*Locators.FIELD_PASSWORD_LOGIN)
            password_field.clear()
            password_field.send_keys(user_data['password'])
            
            driver.find_element(*Locators.BUTTON_ENTRANCE).click()
            print("Нажата кнопка Войти после регистрации")
            
            # 9. Ждем перехода на главную страницу после авторизации
            WebDriverWait(driver, 20).until(
                EC.url_to_be(main_site)
            )
            print(f"Успешный переход на главную страницу: {driver.current_url}")
            
            # 10. Проверяем что пользователь авторизован (кнопка "Оформить заказ")
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(Locators.BUTTON_CHECKOUT)
            )
            print("Пользователь успешно авторизован")
            
            # 11. Проверяем URL
            assert driver.current_url == main_site
            print("Тест регистрации завершен успешно!")
            
        except Exception as e:
            print(f"Ошибка в тесте: {e}")
            print(f"Текущий URL: {driver.current_url}")
            driver.save_screenshot("registration_test_error.png")
            raise


class TestCheckingCreationExistingAccount:
    def test_existing_account(self, driver):
        # Тест попытки регистрации существующего аккаунта
        try:
            # 1. Переходим на страницу регистрации
            driver.get(register_site)
            print("Перешли на страницу регистрации")
            
            # 2. Ждем загрузки формы регистрации
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER)
            )
            print("Форма регистрации загружена")
            
            # 3. Заполняем форму данными существующего пользователя
            driver.find_element(*Locators.FIELD_NAME_REGISTER).send_keys(Credantial.name)
            driver.find_element(*Locators.FIELD_EMAIL_REGISTER).send_keys(Credantial.email)
            driver.find_element(*Locators.FIELD_PASSWORD_REGISTER).send_keys(Credantial.password)
            print("Заполнены поля формы")
            
            # 4. Нажимаем кнопку Зарегистрироваться
            driver.find_element(*Locators.BUTTON_REGISTER).click()
            print("Нажата кнопка Зарегистрироваться")
            
            # 5. Ждем сообщение об ошибке
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.ERROR_ACCOUNT_EXISTS)
            )
            print("Получено сообщение об ошибке: пользователь уже существует")
            
            # 6. Проверяем что остались на странице регистрации
            assert register_site in driver.current_url
            print("Тест существующего аккаунта завершен успешно!")
            
        except Exception as e:
            print(f"Ошибка в тесте: {e}")
            print(f"Текущий URL: {driver.current_url}")
            driver.save_screenshot("existing_account_error.png")
            raise


class TestCheckRegisterNoName:
    def test_registration_no_name(self, driver):
        # Тест регистрации без имени
        try:
            # 1. Переходим на страницу регистрации
            driver.get(register_site)
            print("Перешли на страницу регистрации")
            
            # 2. Ждем загрузки формы регистрации
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER)
            )
            print("Форма регистрации загружена")
            
            # 3. Генерируем email и password
            generator = EmailPasswordGenerator()
            email, password = generator.generate()
            
            # 4. Заполняем только email и password (имя пропускаем)
            driver.find_element(*Locators.FIELD_EMAIL_REGISTER).send_keys(email)  # ИСПРАВЛЕНО
            driver.find_element(*Locators.FIELD_PASSWORD_REGISTER).send_keys(password)
            print("Заполнены email и password (имя пропущено)")
            
            # 5. Нажимаем кнопку Зарегистрироваться
            driver.find_element(*Locators.BUTTON_REGISTER).click()
            print("Нажата кнопка Зарегистрироваться")
            
            # 6. Проверяем что остались на странице регистрации
            WebDriverWait(driver, 10).until(
                EC.url_to_be(register_site)
            )
            assert driver.current_url == register_site
            print("Тест регистрации без имени завершен успешно!")
            
        except Exception as e:
            print(f"Ошибка в тесте: {e}")
            print(f"Текущий URL: {driver.current_url}")
            driver.save_screenshot("no_name_error.png")
            raise


class TestCheckingErrorPassword:
    def test_error_password(self, driver):
        # Тест ошибки при коротком пароле
        try:
            # 1. Переходим на страницу регистрации
            driver.get(register_site)
            print("Перешли на страницу регистрации")
            
            # 2. Ждем загрузки формы регистрации
            WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER)  # ИСПРАВЛЕНО
        )
            print("Форма регистрации загружена")
            
            # 3. Генерируем email
            generator = EmailPasswordGenerator()
            email, _ = generator.generate()
            
            # 4. Заполняем форму
            driver.find_element(*Locators.FIELD_NAME_REGISTER).send_keys("Тест")  # ИСПРАВЛЕНО
            driver.find_element(*Locators.FIELD_EMAIL_REGISTER).send_keys(email)  # ИСПРАВЛЕНО
            driver.find_element(*Locators.FIELD_PASSWORD_REGISTER).send_keys("short")  # Короткий пароль
            print("Заполнена форма с коротким паролем")
            
            # 5. Нажимаем кнопку Зарегистрироваться
            driver.find_element(*Locators.BUTTON_REGISTER).click()
            print("Нажата кнопка Зарегистрироваться")
            
            # 6. Ждем ошибку пароля
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.ERROR_PASSWORD)
            )
            print("Получена ошибка пароля")
            
            # 7. Проверяем что остались на странице регистрации
            assert register_site in driver.current_url
            print("Тест ошибки пароля завершен успешно!")
            
        except Exception as e:
            print(f"Ошибка в тесте: {e}")
            print(f"Текущий URL: {driver.current_url}")
            driver.save_screenshot("password_error.png")
            raise


class TestCheckingNoPassword:
    def test_no_password(self, driver):
        # Тест регистрации без пароля
        try:
            # 1. Переходим на страницу регистрации
            driver.get(register_site)
            print("Перешли на страницу регистрации")
            
            # 2. Ждем загрузки формы регистрации
            WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.FIELD_NAME_REGISTER)  # ИСПРАВЛЕНО
        )
            print("Форма регистрации загружена")
            
            # 3. Генерируем email
            generator = EmailPasswordGenerator()
            email, _ = generator.generate()
            
            # 4. Заполняем только имя и email
            driver.find_element(*Locators.FIELD_NAME_REGISTER).send_keys("Тест")  # ИСПРАВЛЕНО
            driver.find_element(*Locators.FIELD_EMAIL_REGISTER).send_keys(email)
            print("Заполнены имя и email (пароль пропущен)")
            
            # 5. Нажимаем кнопку Зарегистрироваться
            driver.find_element(*Locators.BUTTON_REGISTER).click()
            print("Нажата кнопка Зарегистрироваться")
            
            # 6. Проверяем что остались на странице регистрации
            WebDriverWait(driver, 10).until(
                EC.url_to_be(register_site)
            )
            assert driver.current_url == register_site
            print("Тест регистрации без пароля завершен успешно!")
            
        except Exception as e:
            print(f"Ошибка в тесте: {e}")
            print(f"Текущий URL: {driver.current_url}")
            driver.save_screenshot("no_password_error.png")
            raise

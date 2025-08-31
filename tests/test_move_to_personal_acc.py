import ...

class TestTransitionByConstructor:
    def test_check_transition_by_constructor(self, start_from_main_page):
        driver = start_from_main_page
        
        # Ждем переход на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        # Нажать на кнопку "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        # Ждем загрузки надписи "конструктор"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.the_constructor_button))

        # Кликаем по кнопке "конструктор"
        driver.find_element(*Locators.the_constructor_button).click()

        # Ждем переход на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        # Проверяем что мы на основной странице
        assert driver.current_url == main_site


class TestTransitionByLogo:
    def test_transition_by_logo(self, start_from_login_page):
        driver = start_from_login_page


        # Ждем загрузки надписи "профиль"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_personal_area))

        # Нажать на кнопку "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        # Ждем загрузки надписи "профиль"
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.INSCRIPTION_PROFILE))

        # Кликаем по "logo"
        driver.find_element(*Locators.logo).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        # Проверяем что мы на основной странице
        assert driver.current_url == (main_site)


class TestCheckPageProfile:
    def test_transition_before_profile(self, start_from_login_page):
        driver = start_from_login_page

        # Ждем загрузки "булок"
        WebDriverWait(driver, 10).until(EC.visibility_of_elenent_located(Locators.inscription_bread))

        # Нажать на кнопку "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        # Ждем переход на страницу профиля
        WebDriverWait(driver, 10).until(EC.url_to_be(profile_site))

        # Проверить что мы на странице профиля
        assert driver.current_url == (profile_site)

        driver.quit()
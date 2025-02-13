import allure

from page_objects.main_page import MainPage
from page_objects.password_recovery_page import PasswdRecoveryPage


class TestPasswdRecoveryPage:
    @allure.title('Проверка редиректа на страницу восстановления пароля')
    def test_navigate_to_recovery_passwd_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_login_in_main()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.navigate_to_recovery_passwd_page()
        assert recovery_page.check_displaying_of_input_email()

    @allure.title('Проверка перехода к восстановлению пароля при вводе валидного email и нажатии кнопки "Восстановить"')
    def test_click_recovery_button_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_login_in_main()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.navigate_to_recovery_passwd_page()
        recovery_page.send_email()
        recovery_page.click_on_recovery_button()
        assert recovery_page.check_displaying_of_input_password()

    @allure.title('Проверка отображения пароля в поле ввода после клика на иконку глаза')
    def test_click_on_eye_icon_makes_passwd_visible_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_login_in_main()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.navigate_to_recovery_passwd_page()
        recovery_page.send_email()
        recovery_page.click_on_recovery_button()
        recovery_page.send_password()
        recovery_page.click_on_eye_icon()
        assert recovery_page.check_displaying_password_value()

    @allure.title('Проверка скрытия пароля в поле ввода после двух кликов на иконку глаза')
    def test_double_click_on_eye_icon_makes_passwd_invisible_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_login_in_main()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.navigate_to_recovery_passwd_page()
        recovery_page.send_email()
        recovery_page.click_on_recovery_button()
        recovery_page.send_password()
        recovery_page.click_on_eye_icon()
        recovery_page.click_on_eye_icon()
        assert recovery_page.check_not_displaying_password_value()

    @allure.title('Проверка активности поля Пароль после клика на иконку глаза')
    def test_click_on_eye_icon_makes_passwd_field_active(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_login_in_main()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.navigate_to_recovery_passwd_page()
        recovery_page.send_email()
        recovery_page.click_on_recovery_button()
        recovery_page.send_password()
        recovery_page.click_on_eye_icon()
        assert recovery_page.check_displaying_active_border()
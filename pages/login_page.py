from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на корректный url адрес
        assert "login" in browser.current_url, "URL doesn't contain 'login'"

    def should_be_login_form(self):
        # Проверка, что есть форма логина
        assert self.is_element_present(*MainPageLoсators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register form is not present"

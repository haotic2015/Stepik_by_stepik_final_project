from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage): 
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
#
#
#
#
#    def go_to_login_page(self):
#        login_link = browser.find_element_by_css_selector("#login_link")
#        login_link.click()
#        link = self.browser(*MainPageLocators.LOGIN_LINK)
#        link.click()
#
#    def should_be_login_link():
#        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not present"
#         
#    def go_to_login_page():
#        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#        login_link.click()
    

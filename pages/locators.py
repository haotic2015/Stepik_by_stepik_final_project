from selenium.webdriver.common.by import By
from selenium import webdriver

class MainPageLocators():
    LOGIN_LINK  = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.NAME, "login_submit")
    REGISTER_FORM = (By.NAME, "registration_submit")
    EMAIL =  (By.CSS_SELECTOR, "#id_registration-email")
    PWD1 =  (By.CSS_SELECTOR, "#id_registration-password1")
    PWD2 =  (By.CSS_SELECTOR, "#id_registration-password2")
    SBMT_BUTTON =  (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_FROM_ALERT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    BASKET_VALUE_FROM_ALERT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_TO_BASKET_PAGE = (By.CSS_SELECTOR, "span a.btn:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_TITLE = (By.XPATH, "//div[@id='content_inner']/p")

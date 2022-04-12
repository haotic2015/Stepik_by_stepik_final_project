from selenium.webdriver.common.by import By
from selenium import webdriver

class MainPageLocators():
    LOGIN_LINK  = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.NAME, "login_submit")
    REGISTER_FORM = (By.NAME, "registration_submit")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_FROM_ALERT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    BASKET_VALUE_FROM_ALERT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")

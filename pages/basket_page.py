from selenium import webdriver
from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "В корзине что-то лежит, но вообще-то не должно"
    
    def basket_contains_empty_title(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TITLE), "Почему-то нет строки, что корзина пуста"
    

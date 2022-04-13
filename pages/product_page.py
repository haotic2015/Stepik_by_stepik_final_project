from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()

    def price_of_added_product_should_be_the_same_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Товар не имеет цены"
        assert self.is_element_present(*ProductPageLocators.BASKET_VALUE_FROM_ALERT_ADDED_TO_BASKET), "Товар не добавлен в корзину"
        product_price_el = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_value_el = self.browser.find_element(*ProductPageLocators.BASKET_VALUE_FROM_ALERT_ADDED_TO_BASKET).text
        assert basket_value_el in product_price_el, "Цена товара не соответствует сумме товаров в корзине"

    def basket_should_contain_added_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Название товара не найдено"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_FROM_ALERT_ADDED_TO_BASKET), "Добавленный товар не найден"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text # Ищем название товара
        product_name_from_alert_added_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_ALERT_ADDED_TO_BASKET).text # Берём название товара из информационного сообшения
        assert product_name == product_name_from_alert_added_to_basket, "Товар, добавленный в корзину, не соответствует желаемому." # Сравниваем названия исходного и добавленного товаров

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение об успехе присутствует, но вообще-то быть его не должно"
        
    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение об успехе не пропало, а вообще-то ему бы следовало исчезнуть"
       
   

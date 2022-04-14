from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) # Передаём в объект нужные параметры
    page.open() # Открыть ссылку
    page.add_product_to_basket() # Добавить товар в корзину
    page.solve_quiz_and_get_code() # Решаем задачку из алёрта и получаем код
    page.price_of_added_product_should_be_the_same_in_basket() # Проверяем наличие товара в корзине
    page.basket_should_contain_added_product() # Проверяем, что имя добавленного товара совпадает с описанием товара


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"        
        email = str(time.time()) + "@fakemail.org"
        password = "leT$m8$G0_"
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.should_be_login_link()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
 
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        #self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, self.link) # Передаём в объект нужные параметры
        product_page.open() # Открыть ссылку
        product_page.add_product_to_basket() # Добавить товар в корзину
        product_page.solve_quiz_and_get_code() # Решаем задачку из алёрта и получаем код
        product_page.price_of_added_product_should_be_the_same_in_basket() # Проверяем наличие товара в корзине
        product_page.basket_should_contain_added_product() # Проверяем, что имя добавленного товара совпадает с описанием товара

    @pytest.mark.xfail(reason="Усё в порядке: так и была задумано")
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser): 
        #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"        
        product_page = ProductPage(browser, self.link) # Передаём в объект нужные параметры
        product_page.open() # Открываем страницу товара 
        product_page.add_product_to_basket() # Добавляем товар в корзину 
        product_page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.xfail(reason="Усё в порядке: так и была задумано")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) # Передаём в объект нужные параметры
    page.open() # Открываем страницу товара 
    page.add_product_to_basket() # Добавляем товар в корзину 
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

def test_guest_cant_see_success_message(browser): 
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) # Передаём в объект нужные параметры
    page.open() # Открыть ссылку
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

 
@pytest.mark.xfail(reason="Усё в порядке: так и была задумано")
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) # Передаём в объект нужные параметры
    page.open() # Открываем страницу товара 
    page.add_product_to_basket() # Добавляем товар в корзину 
    page.success_message_is_disappeared() # Проверяем, что нет сообщения об успехе с помощью is_disappeared

@pytest.mark.login_guest    
class TestLoginFromMainPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
    
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) # Передаём в объект нужные параметры
    page.open() # Гость открывает страницу товара
    page.go_to_basket_page() # Переходит в корзину по кнопке в шапке
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty() # Ожидаем, что в корзине нет товаров
    basket_page.basket_contains_empty_title() # Ожидаем, что есть текст о том что корзина пуста 

    

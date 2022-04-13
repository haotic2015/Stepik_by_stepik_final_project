from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link) # Передать в объект нужные параметры
    page.open() # Открыть ссылку
    page.go_to_login_page() # Найти локатор элемента и кликнуть по нему
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) # Передаём в объект нужные параметры
    page.open() # Гость открывает страницу товара
    page.go_to_basket_page() # Переходит в корзину по кнопке в шапке 
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty() # Ожидаем, что в корзине нет товаров
    basket_page.basket_contains_empty_title() # Ожидаем, что есть текст о том что корзина пуста


from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time
import pytest


#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#def test_guest_can_add_product_to_basket(browser, link):
#    page = ProductPage(browser, link) # Передаём в объект нужные параметры
#    page.open() # Открыть ссылку
#    page.add_product_to_basket() # Добавить товар в корзину
#    page.solve_quiz_and_get_code() # Решаем задачку из алёрта и получаем код
#    page.price_of_added_product_should_be_the_same_in_basket() # Проверяем наличие товара в корзине
#    page.basket_should_contain_added_product() # Проверяем, что имя добавленного товара совпадает с описанием товара
#    
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

@pytest.mark.xfail(reason="Усё в порядке: так и была задумано")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link) # Передаём в объект нужные параметры
    page.open() # Открываем страницу товара 
    page.add_product_to_basket() # Добавляем товар в корзину 
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

 

def test_guest_cant_see_success_message(browser): 
    page = ProductPage(browser, link) # Передаём в объект нужные параметры
    page.open() # Открыть ссылку
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

 
@pytest.mark.xfail(reason="Усё в порядке: так и была задумано")
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link) # Передаём в объект нужные параметры
    page.open() # Открываем страницу товара 
    page.add_product_to_basket() # Добавляем товар в корзину 
    page.success_message_is_disappeared() # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

    

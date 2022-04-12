from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
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
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link) # Передать в объект нужные параметры
    page.open() # Открыть ссылку
    page.add_product_to_basket() # Добавить товар в корзину
    page.solve_quiz_and_get_code() # Решаем задачку из алёрта и получаем код
    page.price_of_added_product_should_be_the_same_in_basket() # Проверяем наличие товара в корзине
    page.basket_should_contain_added_product() # Проверяем, что имя добавленного товара совпадает с описанием товара
    
    #@pytest.mark.parametrize('link', ["okay_link",pytest.param("bugged_link", marks=pytest.mark.xfail), okay_link"])                                  

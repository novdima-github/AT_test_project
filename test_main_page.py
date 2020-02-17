import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.main_page import MainPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
         # реализация теста
         url = "http://selenium1py.pythonanywhere.com/"
         page = MainPage(browser, url,timeout=10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
         page.open()  # открываем страницу
         page.go_to_login_page()
         login_page = LoginPage(browser, browser.current_url)
         login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # реализация теста
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, url, timeout=10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_login_link()

@pytest.mark.skip
def test_guest_check_login_form_register_form(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, url, timeout=10)
    page.open()  # открываем страницу
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, url, timeout=10)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_basket_page()
    page.test_product_basket_is_empty()







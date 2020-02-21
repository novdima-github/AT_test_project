from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASS = (By.NAME, "registration-password1")
    REGISTRATION_PASS_CONFIRM = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class PageObjectLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_VIEW_BUTTON = (By.LINK_TEXT, "View basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    #BASKET_EMPTY = (By.XPATH, "//p[contains(text())]")
    BASKET_EMPTY = (By.ID, "content_inner")




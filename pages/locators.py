from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > .price_color")
    ADDING_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    ADDING_TO_BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages > div.alert-info strong")
    SUCCESS_MESSAGES_ADDING = (By.CSS_SELECTOR, "#messages .alert-success")

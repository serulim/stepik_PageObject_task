from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_name = ''
    product_price = ''

    def add_to_basket(self):
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_add_button()

        product_add_to_cart = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        product_add_to_cart.click()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price of product not found"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_add_button(self):
        assert self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button 'Add to basket' is not presented"

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES_ADDING), "Success message not found"
        assert self.is_element_present(*ProductPageLocators.ADDING_TO_BASKET_PRODUCT_NAME), "Adding name of product not found"
        assert self.is_element_present(*ProductPageLocators.ADDING_TO_BASKET_PRODUCT_PRICE), "Adding price of product not found"
        assert self.product_name == self.browser.find_element(*ProductPageLocators.ADDING_TO_BASKET_PRODUCT_NAME).text, "Wrong name product added to basket"
        assert self.product_price == self.browser.find_element(*ProductPageLocators.ADDING_TO_BASKET_PRODUCT_PRICE).text, "Wrong price product added to basket"


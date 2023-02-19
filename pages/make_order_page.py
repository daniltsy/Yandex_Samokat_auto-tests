from pages.base_page import BasePage
from pages.locators import OrderPageLocators


class OrderPage(BasePage):
    def should_be_name_surname_adress_metro_phone(self):
        self.go_to_order_page()
        self.is_element_present(*OrderPageLocators.ORDER_NAME)
        self.is_element_present(*OrderPageLocators.ORDER_SURNAME)
        self.is_element_present(*OrderPageLocators.ORDER_ADRESS)
        self.is_element_present(*OrderPageLocators.ORDER_METRO)
        self.is_element_present(*OrderPageLocators.ORDER_PHONE)




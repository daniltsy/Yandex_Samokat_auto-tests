from pages.base_page import BasePage
from pages.locators import OrderPageLocators


class OrderPage(BasePage):
    def support_for_should_be_all_fields_required(self, *locator):
        element = self.element_to_action(*locator)
        element.click()
        self.browser.execute_script("arguments[0].blur();", element)

    def should_be_name_surname_adress_metro_phone(self):
        self.go_to_order_page()
        self.is_element_present(*OrderPageLocators.ORDER_NAME)
        self.is_element_present(*OrderPageLocators.ORDER_SURNAME)
        self.is_element_present(*OrderPageLocators.ORDER_ADRESS)
        self.is_element_present(*OrderPageLocators.ORDER_METRO)
        self.is_element_present(*OrderPageLocators.ORDER_PHONE)

    def should_be_all_fields_required(self):
        self.go_to_order_page()
        self.support_for_should_be_all_fields_required(*OrderPageLocators.ORDER_NAME)
        assert self.is_element_present(*OrderPageLocators.ORDER_NAME_ERROR), 'Нет сообщения об ошибке поля "Имя"'
        self.support_for_should_be_all_fields_required(*OrderPageLocators.ORDER_SURNAME)
        assert self.is_element_present(*OrderPageLocators.ORDER_SURNAME_ERROR), 'Нет сообщения об ошибке поля "Фамилия"'
        self.support_for_should_be_all_fields_required(*OrderPageLocators.ORDER_ADRESS)
        assert self.is_element_present(*OrderPageLocators.ORDER_ADRESS_ERROR), 'Нет сообщения об ошибке поля "Адрес"'
        self.support_for_should_be_all_fields_required(*OrderPageLocators.ORDER_PHONE)
        assert self.is_element_present(*OrderPageLocators.ORDER_PHONE_ERROR), 'Нет сообщения об ошибке поля "Телефон"'





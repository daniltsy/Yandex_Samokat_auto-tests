from pages.locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_order_page(self):
        order_button = self.browser.find_element(*MainPageLocators.ORDER_BUTTON)
        order_button.click()
        assert 'order' in self.browser.current_url, ' "order" не является частью url'

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def element_to_action(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return 'Такого элемента нет на странице'
        return element

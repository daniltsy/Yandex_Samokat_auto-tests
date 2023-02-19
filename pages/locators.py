from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON = (By.CSS_SELECTOR, '.Header_Nav__AGCXC .Button_Button__ra12g')


class OrderPageLocators:
    ORDER_NAME = (By.CSS_SELECTOR, '[placeholder = "* Имя"]')
    ORDER_SURNAME = (By.CSS_SELECTOR, '[placeholder = "* Фамилия"]')
    ORDER_ADRESS = (By.CSS_SELECTOR, '[placeholder = "* Адрес: куда привезти заказ"]')
    ORDER_METRO = (By.CSS_SELECTOR, '.select-search__input')
    ORDER_PHONE = (By.CSS_SELECTOR, '[placeholder ="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.CSS_SELECTOR, '.Button_Middle__1CSJM')
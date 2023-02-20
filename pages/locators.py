from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON = (By.CSS_SELECTOR, '.Header_Nav__AGCXC .Button_Button__ra12g')


class OrderPageLocators:
    ORDER_NAME = (By.CSS_SELECTOR, '[placeholder = "* Имя"]')
    ORDER_NAME_ERROR = (By.CSS_SELECTOR, '[placeholder = "* Имя"]~.Input_Visible___syz6')
    ORDER_SURNAME = (By.CSS_SELECTOR, '[placeholder = "* Фамилия"]')
    ORDER_SURNAME_ERROR = (By.CSS_SELECTOR, '[placeholder = "* Фамилия"]~.Input_Visible___syz6')
    ORDER_ADRESS = (By.CSS_SELECTOR, '[placeholder = "* Адрес: куда привезти заказ"]')
    ORDER_ADRESS_ERROR = (By.CSS_SELECTOR, '[placeholder = "* Адрес: куда привезти заказ"]~.Input_Visible___syz6')
    ORDER_METRO = (By.CSS_SELECTOR, '.select-search__input')
    ORDER_PHONE = (By.CSS_SELECTOR, '[placeholder ="* Телефон: на него позвонит курьер"]')
    ORDER_PHONE_ERROR = '[placeholder ="* Телефон: на него позвонит курьер"]~.Input_Visible___syz6'
    NEXT_BUTTON = (By.CSS_SELECTOR, '.Button_Middle__1CSJM')

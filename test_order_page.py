from pages.make_order_page import OrderPage
import pytest

link = 'https://0b077e8c-d8b2-43ee-90ef-f2d792cbf6d3.serverhub.praktikum-services.ru/'


class TestFirstOrderPage:

    def test_user_can_see_name_surname_adress_metro_phone(self, browser):
        page = OrderPage(browser, link)
        page.open()
        page.go_to_order_page()
        page.should_be_name_surname_adress_metro_phone()

    @pytest.mark.xfail  # Баг при прохождении теста на моменте с Адресом, не вылезает красное сообщение об ошибке
    def test_user_can_see_errors_if_all_required_fields_are_not_filled(self, browser):
        page = OrderPage(browser, link)
        page.open()
        page.go_to_order_page()
        page.should_be_all_fields_required()


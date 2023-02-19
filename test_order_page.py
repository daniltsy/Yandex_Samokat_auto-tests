from pages.make_order_page import OrderPage

link = 'https://e53585a4-064b-423d-b39a-e5f908c682be.serverhub.praktikum-services.ru/'


class TestFirstOrderPage:

    def test_user_can_see_name_surname_adress_metro_phone(self, browser):
        page = OrderPage(browser, link)
        page.open()
        page.go_to_order_page()
        page.should_be_name_surname_adress_metro_phone()




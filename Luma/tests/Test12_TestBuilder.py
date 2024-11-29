import pytest

from pages.test_builder.test_builder import TestBuilder


@pytest.mark.usefixtures("driver")
class Test12TestBuilder:

    def test_01_core_flow_1(self):

        TestBuilder(self.driver, self.url)\
            .l_login("User1@gmail.com", "qwerty12345")\
            .r_search_product("Strike Endurance boy")\
            .r_count_products(9)\
            .r_search_product("Strike boy") \
            .r_count_products(1) \
            .r_search_product("shoe") \
            .r_count_products(3)

    def test_02_core_flow_2(self):

        TestBuilder(self.driver, self.url)\
            .p_navigate_to_product("https://magento.softwaretestingboard.com/sol-active-short.html")\
            .p_verify_name("Sol Active Short")\
            .p_verify_price("32.00")\
            .p_enter_qty(18)\
            .p_select_size("34")\
            .p_select_color("blue")\
            .p_add_to_cart()\
            .p_verify_title_quantity(18) \
            .p_navigate_to_product("https://magento.softwaretestingboard.com/cassius-sparring-tank.html") \
            .p_verify_name("Cassius Sparring Tank") \
            .p_verify_price("18.00") \
            .p_enter_qty(25) \
            .p_select_size("L") \
            .p_select_color("blue") \
            .p_add_to_cart() \
            .p_verify_title_quantity(43)\
            .c_navigate_to_cart()\
            .c_verify_product_info("Sol Active Short", "34", "blue", "32.00", "18", "576.00")\
            .c_verify_product_info("Cassius Sparring Tank", "L", "blue", "18.00", "25", "450.00")\
            .c_proceed_to_checkout()


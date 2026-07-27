from playwright.sync_api import Page

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage

def test_product_sort(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    inventory_page = login_page.login_standard_user()
    assert inventory_page.get_title().text_content() == "Products"
    inventory_page.sort_dropdown.select_option("za")
    assert inventory_page.sort_dropdown.input_value() == "za"
from playwright.sync_api import Page

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
 

def test_login_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    assert "standard_user" in login_page.get_login_credentials().inner_html()
    assert "secret_sauce" in login_page.get_login_password().inner_html()

def test_login_successfull(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    inventory_page = login_page.login_standard_user()
    assert inventory_page.get_title().text_content() == "Products"


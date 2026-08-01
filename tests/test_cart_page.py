import pytest
from playwright.sync_api import Page
from pages.LoginPage import LoginPage


def test_cart_page_load(page: Page):
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()

    cart_page = inventory_page.go_to_cart()

    # Verify title and checkout button are visible
    assert cart_page.get_page_title().text_content() == "Your Cart"
    assert cart_page.checkout_button.is_visible()


def test_add_item_to_cart(page: Page):
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    inventory_page.add_item_to_cart("sauce-labs-backpack")

    cart_page = inventory_page.go_to_cart()

    # assert the item count went up
    assert cart_page.get_item_count() == 1
    # assert the item name is correct
    assert "Sauce Labs Backpack" in cart_page.get_item_name()
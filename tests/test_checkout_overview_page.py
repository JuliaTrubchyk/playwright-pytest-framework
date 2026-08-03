
import pytest
from playwright.sync_api import Page
from pages.LoginPage import LoginPage


def test_all_information(page: Page):
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    inventory_page.add_item_to_cart("sauce-labs-backpack")

    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.go_to_checkout()

    checkout_overview_page = checkout_page.submit_checkout_information("Tom", "Smith", "94539")

    assert checkout_overview_page.summary_info.is_visible()

def test_verify_thank_you_message(page: Page):
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    inventory_page.add_item_to_cart("sauce-labs-backpack")

    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.go_to_checkout()

    checkout_overview_page = checkout_page.submit_checkout_information("Tom", "Smith", "94539")
    checkout_complete_page = checkout_overview_page.finish_checkout()

    assert checkout_complete_page.get_complete_message().text_content() == "Thank you for your order!"

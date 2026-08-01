
import pytest
from playwright.sync_api import Page
from pages.LoginPage import LoginPage


def test_fill_out_page_is_visible(page: Page):
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    inventory_page.add_item_to_cart("sauce-labs-backpack")

    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.go_to_checkout()

    # Verify title and continue button are visible
    assert checkout_page.get_page_title().text_content() == "Checkout: Your Information"
    assert checkout_page.continue_button.is_visible()


def test_checkout_fields_accept_valid_information(page: Page):
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    inventory_page.add_item_to_cart("sauce-labs-backpack")

    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.go_to_checkout()

    checkout_page.fill_checkout_information("Tom", "Smith", "94539")

    assert checkout_page.get_first_name_field().input_value() == "Tom"
    assert checkout_page.get_last_name_field().input_value() == "Smith"
    assert checkout_page.get_postal_code_field().input_value() == "94539"


@pytest.mark.parametrize(
    "first_name, last_name, postal_code",
    [
        ("Tom", "Smith", "94539"),
        ("John", "O'Connor", "10001"),
        ("Anna", "Smith-Jones", "94539"),
    ]
)
def test_continue_button_navigates_to_checkout_overview(page: Page, first_name, last_name, postal_code):
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    inventory_page.add_item_to_cart("sauce-labs-backpack")

    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.go_to_checkout()

    checkout_overview_page = checkout_page.submit_checkout_information(first_name, last_name, postal_code)
    assert checkout_overview_page.get_page_title().text_content() == "Checkout: Overview"


def test_verify_thank_you_message(page: Page):
    # Click Finish
    # Assert the Message
    pass
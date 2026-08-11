
import pytest
from pages.InventoryPage import InventoryPage
from pages.CheckoutPage import CheckoutPage
from pages.CheckoutOverviewPage import CheckoutOverviewPage


def test_all_information(inventory_page: InventoryPage):

    inventory_page.add_item_to_cart("sauce-labs-backpack")

    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.go_to_checkout()

    checkout_overview_page = checkout_page.submit_checkout_information("Tom", "Smith", "94539")

    assert checkout_overview_page.summary_info.is_visible()

def test_all_information(completed_order: CheckoutOverviewPage):
    assert completed_order.summary_info.is_visible()

def test_verify_thank_you_message(inventory_page: InventoryPage):

    inventory_page.add_item_to_cart("sauce-labs-backpack")

    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.go_to_checkout()

    checkout_overview_page = checkout_page.submit_checkout_information("Tom", "Smith", "94539")
    checkout_complete_page = checkout_overview_page.finish_checkout()

    assert checkout_complete_page.get_complete_message().text_content() == "Thank you for your order!"

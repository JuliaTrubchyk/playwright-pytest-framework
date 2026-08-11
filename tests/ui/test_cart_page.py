import pytest

from pages.InventoryPage import InventoryPage


def test_cart_page_load(inventory_page: InventoryPage):
    cart_page = inventory_page.go_to_cart()

    # Verify title and checkout button are visible
    assert cart_page.get_page_title().text_content() == "Your Cart"
    assert cart_page.checkout_button.is_visible()


def test_add_item_to_cart(inventory_page: InventoryPage):
    inventory_page.add_item_to_cart("sauce-labs-backpack")

    cart_page = inventory_page.go_to_cart()

    # assert the item count went up
    assert cart_page.get_item_count() == 1
    # assert the item name is correct
    assert "Sauce Labs Backpack" in cart_page.get_item_name()

# example using fixture
def test_added_item_appears_in_cart(cart_with):
    cart_page = cart_with("sauce-labs-backpack")
    assert cart_page.get_item_count() == 1
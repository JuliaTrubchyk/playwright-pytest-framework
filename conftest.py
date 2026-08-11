import pytest
from playwright.sync_api import Page
from pages.CheckoutOverviewPage import CheckoutOverviewPage
from pages.CheckoutPage import CheckoutPage
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture for the login page"""
    login_page = LoginPage(page)
    login_page.open()
    return login_page

@pytest.fixture
def inventory_page(login_page: LoginPage) -> InventoryPage:
    return login_page.login_standard_user()

@pytest.fixture
def checkout_page(inventory_page: InventoryPage) -> CheckoutPage:
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    return inventory_page.go_to_cart().go_to_checkout()

@pytest.fixture
def completed_order(checkout_page: CheckoutPage) -> CheckoutOverviewPage:
        return checkout_page.submit_checkout_information(
        "Tom", "Smith", "94539")

@pytest.fixture
def cart_with(inventory_page: InventoryPage):
    def _cart_with(*item_ids: str):
        for item_id in item_ids:
            inventory_page.add_item_to_cart(item_id)

        return inventory_page.go_to_cart()

    return _cart_with
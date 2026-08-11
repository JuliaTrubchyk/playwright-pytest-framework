import os
import pytest
from dotenv import load_dotenv

from playwright.sync_api import Page
from pages.CheckoutOverviewPage import CheckoutOverviewPage
from pages.CheckoutPage import CheckoutPage
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage

load_dotenv()
USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")
BASE_URL = os.getenv("BASE_URL")

AUTH_STATE_PATH = "playwright/.auth/state.json"


@pytest.fixture(scope="session")
def auth_state(browser):

    # Create the path
    os.makedirs(os.path.dirname(AUTH_STATE_PATH), exist_ok=True)

    context = browser.new_context(base_url=BASE_URL)
    login_page = LoginPage(context.new_page())
    login_page.open()
    login_page.login_user(USERNAME, PASSWORD)
    context.storage_state(path="AUTH_STATE_PATH")
    context.close()

    return AUTH_STATE_PATH


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture for the login page"""
    login_page = LoginPage(page)
    login_page.open()
    return login_page

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return new_context(storage_state=auth_state).new_page()

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
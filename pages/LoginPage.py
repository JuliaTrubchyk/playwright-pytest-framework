
from playwright.sync_api import Page
from pages.InventoryPage import InventoryPage


class LoginPage:
    def __init__(self, page: Page) -> None:
    # Locators
        self.page = page
        self.username_field = page.get_by_role("textbox", name="Username")
        self.password_field = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.login_credentials = page.locator("[data-test=\"login-credentials\"]")
        self.login_password = page.locator("[data-test=\"login-password\"]")
        self.error_message = page.locator("[data-test=\"error\"]")

    def open(self):
        self.page.goto("/")

    def login_standard_user(self)  -> InventoryPage():
        self.username_field.fill("standard_user")
        self.password_field.fill("secret_sauce")
        self.login_button.click()
        return InventoryPage(self.page)

    def login_user(self, username: str, password: str)  -> InventoryPage():
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
        return InventoryPage(self.page)

    def get_login_credentials(self):
        return self.login_credentials

    def get_login_password(self):
        return self.login_password

    def get_error_message(self):
        return self.error_message



    # Getters
    def get_login_credentials(self):
        return self.login_credentials

    def get_login_password(self):
        return self.login_password

    def get_error_message(self):
        return self.error_message
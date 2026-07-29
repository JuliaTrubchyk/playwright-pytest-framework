
from playwright.sync_api import Page
from pages.InventoryPage import InventoryPage


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
    
    # Locators
        self.username_field = page.get_by_role("textbox", name="Username")
        self.password_field = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.login_credentials = page.locator("[data-test=\"login-credentials\"]")
        self.login_password = page.locator("[data-test=\"login-password\"]")

    # Validation
        self.error_message = page.locator("[data-test=\"error\"]")

    def open(self):
        self.page.goto("/")

    def submit_login(self, username: str, password: str) -> None:
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def login_user(self, username: str, password: str) -> InventoryPage:
        self.submit_login(username, password)
        return InventoryPage(self.page)

    def login_standard_user(self) -> InventoryPage:
        return self.login_user("standard_user", "secret_sauce")

    # def login_standard_user(self)  -> InventoryPage:
    #     self.username_field.fill("standard_user")
    #     self.password_field.fill("secret_sauce")
    #     self.login_button.click()
    #     return InventoryPage(self.page)

    # def login_user(self, username: str, password: str)  -> InventoryPage:
    #     self.username_field.fill(username)
    #     self.password_field.fill(password)
    #     self.login_button.click()
    #     return InventoryPage(self.page)

    # Getters
    def get_login_credentials(self):
        return self.login_credentials

    def get_login_password(self):
        return self.login_password

    def get_error_message(self):
        return self.error_message
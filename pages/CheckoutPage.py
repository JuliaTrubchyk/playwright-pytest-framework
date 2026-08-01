
from playwright.sync_api import Page
from pages.CheckoutOverviewPage import CheckoutOverviewPage


class CheckoutPage:
    def __init__(self, page:Page) -> None:
        self.page = page
    #Locators
        self.page_title = page.locator("[data-test=\"title\"]")

        self.first_name_field = page.locator("[data-test=\"firstName\"]")
        self.last_name_field = page.locator("[data-test=\"lastName\"]")
        self.postal_code_field = page.locator("[data-test=\"postalCode\"]")

        self.cancel_button = page.locator("[data-test=\"cancel\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")

        self.error_message = page.locator("[data-test=\"error\"]")

    # Methods
    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code_field.fill(postal_code)

    def submit_checkout_information(self, first_name: str, last_name: str, postal_code: str) -> CheckoutOverviewPage:
        self.fill_checkout_information(first_name, last_name, postal_code)
        self.click_continue()
        return CheckoutOverviewPage(self.page)

    def click_cancel(self) -> None:
        self.cancel_button.click()

    def click_continue(self) -> None:
        self.continue_button.click()

    # Getters
    def get_page_title(self):
        return self.page_title

    def get_first_name_field(self):
        return self.first_name_field

    def get_last_name_field(self):
        return self.last_name_field

    def get_postal_code_field(self):
        return self.postal_code_field
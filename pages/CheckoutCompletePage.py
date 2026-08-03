
from playwright.sync_api import Page


class CheckoutCompletePage:
    def __init__(self, page:Page) -> None:
        self.page = page
    #Locators
        self.page_title = page.locator("[data-test=\"title\"]")
        self.complete_message = page.locator("[data-test=\"complete-header\"]")
        self.back_home_button = page.locator("[data-test=\"back-to-products\"]")

    # Getters
    def get_complete_message(self):
        return self.complete_message

from playwright.sync_api import Page


class CheckoutOverviewPage:
    def __init__(self, page:Page) -> None:
        self.page = page
    #Locators
        self.page_title = page.locator("[data-test=\"title\"]")

    # Getters
    def get_page_title(self):
        return self.page_title
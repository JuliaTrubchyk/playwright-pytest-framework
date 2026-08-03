
from playwright.sync_api import Page
from pages.CheckoutCompletePage import CheckoutCompletePage


class CheckoutOverviewPage:
    def __init__(self, page:Page) -> None:
        self.page = page
    #Locators
        self.page_title = page.locator("[data-test=\"title\"]")
        self.summary_info = page.locator(".summary_info")
        self.finish_button = page.locator("[data-test=\"finish\"]")


    # Methods
    def finish_checkout(self) -> CheckoutCompletePage:
        self.click_finish()
        return CheckoutCompletePage(self.page)


    def click_finish(self) -> None:
        self.finish_button.click()


    # Getters
    def get_page_title(self):
        return self.page_title
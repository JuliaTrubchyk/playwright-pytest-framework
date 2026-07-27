from playwright.sync_api import Locator, Page


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')

    def get_title(self):
        return self.title

    def print_locator(self):
        print(sort_dropdown.count())
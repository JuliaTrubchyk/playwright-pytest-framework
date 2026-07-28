from playwright.sync_api import Page, expect


def test_positive_login(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_locked_out_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill("locked_out_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    warning = page.get_by_role("heading", name="Epic sadface: Sorry, this user has been locked out.")
    expect(warning).to_be_visible()

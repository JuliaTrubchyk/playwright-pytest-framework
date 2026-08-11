from playwright.sync_api import Page, expect

def test_e2e_swag_labs(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    add_to_cart_buttons = page.get_by_role("button", name="Add to cart")
    add_to_cart_buttons.first.click()
    page.locator(".shopping_cart_link").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    page.get_by_role("button", name="checkout").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    page.get_by_placeholder("First Name").fill("John")
    page.get_by_placeholder("Last Name").fill("Smith")
    page.get_by_placeholder("Zip/Postal Code").fill("12345")
    page.get_by_role("button", name="continue").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    page.get_by_role("button", name="finish").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    expect(page.get_by_role("heading", name="Thank you for your order!")).to_be_visible()
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.parametrize(
    "first,last,email",
    [
        ("John", "Smith", "jsmith@gmail.com"),
        ("Mike", "Johnson", "mjohnson@gmail.com"),
    ],
)
def test_demoqa(page: Page, first, last, email) -> None:
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill(first)

    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill(last)

    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill(email)

    page.get_by_role("radio", name="Male", exact=True).check()


    page.get_by_role("textbox", name="Mobile Number").click()
    page.get_by_role("textbox", name="Mobile Number").fill("9174367799")

    page.get_by_text("Sports").click()
    assert page.get_by_role("checkbox", name="Sports").is_visible()

    page.locator("#uploadPicture").set_input_files("test_data/test_image.png")

    page.get_by_role("textbox", name="Current Address").click()
    page.get_by_role("textbox", name="Current Address").fill("123 Main St")

    page.get_by_role("button", name="Submit").click()

    actual_text = page.get_by_text("Thanks for submitting the form").text_content()
    expected_text = "Thanks for submitting the form"
    assert expected_text in actual_text
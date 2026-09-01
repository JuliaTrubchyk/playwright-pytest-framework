# Test Case1: Click Action
from playwright.sync_api import Page
import pytest

def test_click_action(page: Page) -> None:
    add_element_button = page.get_by_role("button", name="Add Element")
    delete_buttons = page.get_by_role("button", name="Delete")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    add_element_button.click()
    add_element_button.click()
    
    delete_buttons.first.click()
    assert delete_buttons.count() == 1


def test_fill_and_press(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/login")
    username_input = page.get_by_label("Username")
    password_input = page.get_by_label("Password")
    login_button = page.get_by_role("button", name="Login")

    username_input.fill("tomsmith")
    username_input.press("Tab")
    password_input.fill("SuperSecretPassword!")
    login_button.click()
    actual_text = page.get_by_role("heading", name="Welcome to the Secure Area.").text_content()
    expected_text = "Welcome to the Secure Area. When you are done click logout below."
    assert expected_text in actual_text


def test_checkboxes(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox1 = page.get_by_role("checkbox").first
    checkbox2 = page.get_by_role("checkbox").last
    checkbox1.check()
    checkbox2.uncheck()

    assert checkbox1.is_checked()
    assert not checkbox2.is_checked()


def test_dropdown(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option("Option 1")
    dropdown.select_option("Option 2")

def test_hovers(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/hovers")
    image = page.locator(".figure").first
    image.hover()


def test_upload(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/upload")
    page.locator("#file-upload").set_input_files("test_data/resume.txt")
    page.locator("#file-submit").click()


def test_drag_and_drop(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    a = page.locator("#column-a")
    b = page.locator("#column-b")
    a.drag_to(b)


def test_context_window(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/context_menu")

    dialog_message = ""

    def handle_dialog(dialog):
        nonlocal dialog_message
        dialog_message = dialog.message
        dialog.accept()

    page.once("dialog", handle_dialog)

    page.locator("#hot-spot").click(button="right")

    assert dialog_message == "You selected a context menu"

# @pytest.mark.parametrize(
#     "link",
#     [
#         "random_data_18.txt",
#         "sample-upload.txt"
#     ],
# )
# def test_file_download(page: Page, link: str) -> None:
#     page.goto("https://the-internet.herokuapp.com/download")

#     with page.expect_download() as download_info:
#         page.get_by_role("link", name=link, exact=True).click()

#     download = download_info.value

#     assert download.suggested_filename == link

def test_upload_then_download_roundtrip(page: Page, tmp_path) -> None:
    """/download lists whatever strangers upload, so hardcoded filenames rot.
    Fix: OWN the data — upload a uniquely named file, then download that exact file.
    (tmp_path is a pytest built-in fixture: a fresh temp folder per test.)"""
    file_name = f"pliskin-{uuid.uuid4().hex[:8]}.txt"
    local_file = tmp_path / file_name
    local_file.write_text("uploaded by the pliskin_june11 test suite")
 
    # Arrange: put our own file on the server
    page.goto("https://the-internet.herokuapp.com/upload")
    page.locator("#file-upload").set_input_files(local_file)
    page.locator("#file-submit").click()
    expect(page.locator("#uploaded-files")).to_have_text(file_name)
 
    # Act + assert: it must now appear on /download, under the name WE chose
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_info:
        page.get_by_role("link", name=file_name, exact=True).click()
    assert download_info.value.suggested_filename == file_name
 

def test_hidden_ad(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/entry_ad")

    modal = page.locator("#modal")
    modal.wait_for(state="visible")

    page.get_by_text("Close", exact=True).click()

    modal.wait_for(state="hidden")
    assert not modal.is_visible()

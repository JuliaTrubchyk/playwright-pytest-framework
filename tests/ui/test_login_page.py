import pytest

from pages.LoginPage import LoginPage
 


def test_login_credentials_are_displayed(login_page: LoginPage):
    assert "standard_user" in login_page.get_login_credentials().inner_html()
    assert "secret_sauce" in login_page.get_login_password().inner_html()

def test_standard_user_login(login_page: LoginPage):
    inventory_page = login_page.login_standard_user()
    assert inventory_page.get_title().text_content() == "Products"

# Positive Login
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "problem_user",
        "performance_glitch_user",
        "visual_user",
    ],
)
def test_valid_users_login(login_page: LoginPage, username):
    invetory_page = login_page.login_user(username, "secret_sauce")
    # Only has access to Invetory stuff
    assert invetory_page.get_title().text_content() == "Products"


# Negative Login
@pytest.mark.parametrize(
    "username, error",
    [
        ("locked_out_user", "Epic sadface: Sorry, this user has been locked out."),
        ("not_a_user", "Epic sadface: Username and password do not match any user in this service"),
    ],
)
def test_invalid_login_fails(login_page: LoginPage, username, error):
    login_page.submit_login(username, "secret_sauce")

    actual_error = login_page.get_error_message().text_content()
    #    expected  vs  actual
    assert error in actual_error

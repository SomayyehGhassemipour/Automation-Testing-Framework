from application.ui.github_ui import GithubUI

def test_negative_login():
    """
    Summary: Negative Test for Login 
    steps:
        1. Navigate to login page
        2. Enter wrong creds
        3. Click login/signin button

    Expected result:
        Error saying "...." appeared
    """

    # initial GithubUI 
    github_ui = GithubUI()

    # navigate to it
    github_ui.login_page.navigate_to()

    # Enter wrong credential 
    github_ui.try_login("your_username", "your_password")

    # Expected result
    assert github_ui.login_page.check_wrong_creds_message()

    # clean up
    github_ui.close()
    
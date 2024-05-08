from playwright.sync_api import Page, Locator, expect
from base_dialog import BaseDialog

class SignInDialog(BaseDialog):
    """
    SignInDialog class that inherits from the BaseDialog class.
    It provides methods to interact with the sign in dialog.
    """
    def __init__(self, page: Page) -> None:
        """
        Initializes a new instance of the SignInDialog class.

        :param page: The Playwright page object.
        """
        super().__init__(page, '[data-testid="form-login"]')
        self._user_name_tb: Locator = self._page.locator('[name="username"]')
        self._password_tb: Locator = self._page.locator('[name="password"]')
        self._forgot_password_link: Locator = self._page.locator('[data-testid="forgot-password-login"]')
        self._remember_me_chbx: Locator = self._page.locator('[data-testid="remember-me-login"]')
        self._start_playing_btn: Locator = self._page.locator('[data-testid="start-playing-login"]')

    def sign_in(self, username: str, password: str, remember_me: bool = False) -> None:
        """
        Signs in with the provided username and password.

        :param username: The username.
        :param password: The password.
        :param remember_me: Whether to remember the user.
        """
        self._page.on('dialog', lambda dialog: dialog.dismiss())
        self._user_name_tb.fill(username)
        self._password_tb.fill(password)

        if remember_me:
            self._remember_me_chbx.check()

        self._start_playing_btn.click()
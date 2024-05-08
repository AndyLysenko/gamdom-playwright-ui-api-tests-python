from playwright.sync_api import Page, Locator, expect

class BaseDialog:
    """
    BaseDialog class that provides common methods for all dialog classes.
    """
    def __init__(self, page: Page, dialog_validate_locator_string: str) -> None:
        """
        Initializes a new instance of the BaseDialog class.

        :param page: The Playwright page object.
        :param dialog_validate_locator_string: The locator used to validate the dialog.
        """
        self._page: Page = page
        self._dialog_validate_locator_string: str = dialog_validate_locator_string

    def wait_to_be_open(self) -> None:
        """
        Waits for the dialog to be open.
        """
        locator: Locator = self._page.locator(self._dialog_validate_locator_string)
        expect(locator).to_be_visible(timeout=10000)

    def verify_not_displayed(self) -> None:
        """
        Verifies that the dialog is not displayed.
        """
        locator: Locator = self._page.locator(self._dialog_validate_locator_string)
        expect(locator).not_to_be_visible()
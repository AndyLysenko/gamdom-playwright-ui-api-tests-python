from typing import Optional
from playwright.sync_api import Page, Locator, expect
from constants import BASE_URL

class BasePage:
    """
    BasePage class that provides common methods for all page classes.
    """
    def __init__(self, page: Page, url: Optional[str] = None, page_validate_locator: Optional[str] = None) -> None:
        """
        Initializes a new instance of the BasePage class.

        :param page: The Playwright page object.
        :param url: The URL of the page. Defaults to None.
        :param page_validate_locator: The locator used to validate the page. Defaults to None.
        """
        self._page: Page = page
        self._page_validate_locator_string: Optional[str] = page_validate_locator
        self._url: Optional[str] = f"{BASE_URL}{url}" if url is not None else None

    def navigate(self) -> None:
        """
        Navigates to the page's URL.
        """
        if self._url is not None:
            self._page.goto(self._url)
        else:
            raise ValueError('Cannot navigate to the page. No URL provided.')

    def verify_page_is_open(self) -> None:
        """
        Verifies that the page is open by checking the URL and visibility of a locator.
        """
        if self._url is None and self._page_validate_locator_string is None:
            raise ValueError('Cannot verify the page is open. No URL or page validation locator provided')
        
        if self._url is not None:
            self._page.wait_for_url(self._url)

        if self._page_validate_locator_string is not None:
            locator: Locator = self._page.locator(self._page_validate_locator_string)
            expect(locator).to_be_visible()
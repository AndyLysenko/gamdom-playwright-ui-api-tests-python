from playwright.sync_api import Page, Locator
from base_page import BasePage

class HomePage(BasePage):
    """
    HomePage class that inherits from the BasePage class.
    It provides methods to interact with the home page.
    """
    def __init__(self, page: Page) -> None:
        """
        Initializes HomePage with the page object.

        :param page: The page object.
        """
        super().__init__(page, '/', '[data-testid="signup-nav"]')
        self._sign_up_btn: Locator = self._page.locator('[data-testid="signup-nav"]')
        self._sign_in_btn: Locator = self._page.locator('[data-testid="signin-nav"]')
        self._search_tb: Locator = self._page.locator('input[placeholder*="Search"]')
        self._open_chat_icon: Locator = self._page.locator('i.icon-Chat')
        self._close_chat_icon: Locator = self._page.locator('button > i.icon-remove21').first

    def click_sign_up(self) -> None:
        """
        Clicks the sign up button.
        """
        self._sign_up_btn.click()

    def click_sign_in(self) -> None:
        """
        Clicks the sign in button.
        """
        self._sign_in_btn.click()

    def search_and_open_game(self, name: str) -> None:
        """
        Searches for a game and opens it.

        :param name: The name of the game.
        """
        self._search_tb.fill(name)
        self._search_tb.click()

        game_list_item: Locator = self._page.locator(f'li:has-text("{name}")').first
        game_list_item.click()

    def open_chat(self) -> None:
        """
        Clicks the open chat icon to open the chat.
        """
        self._open_chat_icon.click()

    def close_chat(self) -> None:
        """
        Clicks the close chat icon to close the chat.
        """
        self._close_chat_icon.click()
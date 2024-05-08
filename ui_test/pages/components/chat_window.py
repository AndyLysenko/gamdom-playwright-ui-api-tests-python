from playwright.sync_api import Page, Locator
from base_page import BasePage

class ChatWindow(BasePage):
    """
    ChatWindow class that inherits from the BasePage class.
    It provides methods to interact with the chat window.
    """
    def __init__(self, page: Page) -> None:
        """
        Initializes a new instance of the ChatWindow class.

        :param page: The Playwright page object.
        """
        super().__init__(page, None, '#chat-messages')
        self._input_tb: Locator = self._page.locator('.chat_inputbox')
        self._emoji_btn: Locator = self._page.locator('button[aria-label="emoji"]')
        self._send_message_btn: Locator = self._page.locator('button[aria-label="send-message"]')

    def is_input_active(self) -> bool:
        """
        Checks if the input is active.

        :return: True if the input is active, False otherwise.
        """
        return self._input_tb.get_attribute('contenteditable') == 'true'

    def send_message(self, message: str) -> None:
        """
        Sends a message.

        :param message: The message to send.
        """
        self._input_tb.fill(message)
        self._send_message_btn.click()
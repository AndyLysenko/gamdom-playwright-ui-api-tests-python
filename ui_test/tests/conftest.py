from pages.components.chat_window import ChatWindow
from pages.home_page import HomePage
from playwright.sync_api import Page
import pytest

@pytest.fixture(scope='function')
def home_page(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.verify_page_is_open()
    yield home_page
    pass

@pytest.fixture(scope='function')
def chat_window(page: HomePage):
    yield ChatWindow(page)
    pass
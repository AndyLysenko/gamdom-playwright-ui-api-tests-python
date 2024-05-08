from pages.components.chat_window import ChatWindow
from pages.home_page import HomePage

def test_chat_unauthorised_user_cant_send_message(home_page: HomePage, chat_window: ChatWindow):
    home_page.open_chat()
    chat_window.verify_page_is_open()

    assert not chat_window.is_input_active()
from typing import Optional, Callable
from urllib.parse import urlparse, parse_qs
from playwright.sync_api import Page, Locator, expect
from base_page import BasePage
from model.game import Game
from functools import partial

class GamePage(BasePage):
    """
    GamePage class that inherits from the BasePage class.
    It provides methods to interact with the game page.
    """
    def __init__(self, page: Page, game: Game) -> None:
        """
        Initializes a new instance of the GamePage class.

        :param page: The Playwright page object.
        :param game: The Game object containing game details.
        """
        super().__init__(page, url=game.url)
        self._game: Game = game
        self._game_name_lbl: Locator = self._page.locator('h1').first
        self._provider_lbl: Locator = self._game_name_lbl.locator('+ a >> p')
        self._canvas_frame_retrieval_method: Optional[Callable] = partial(self._page.locator('iframe.eg__iframe').first.get_attribute, 'src')

    def verify_name_and_provider(self) -> None:
        """
        Verifies the game name and provider.
        """

        expect(self._game_name_lbl).to_have_text(self._game.name)
        expect(self._provider_lbl).to_have_text(self._game.provider)

    def verify_game_id_and_src(self) -> None:
        """
        Verifies the game ID and source.
        """
        src: Optional[str] = self._canvas_frame_retrieval_method()

        # Extract the base URL
        url_object = urlparse(src)
        base_url: str = url_object.scheme + "://" + url_object.netloc
        assert base_url == self._game.game_provider_url

        # Extract the game id
        query_params = parse_qs(url_object.query)
        game_id: Optional[str] = query_params.get('gameid')[0] if 'gameid' in query_params else None
        assert game_id == self._game.id
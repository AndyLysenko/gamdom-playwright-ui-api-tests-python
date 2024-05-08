import pytest
from playwright.sync_api import Page
from helpers.test_data_helper import load_games
from pages.game_page import GamePage
from pages.home_page import HomePage
from model.game import Game
from typing import List

test_games: List[Game] = load_games()

@pytest.mark.parametrize("game", test_games)
def test_search_and_open_game(game: Game, page: Page, home_page: HomePage) -> None:
    home_page.search_and_open_game(game.name)

    game_page = GamePage(page, game)
    game_page.verify_page_is_open()
    game_page.verify_name_and_provider()
    game_page.verify_game_id_and_src()
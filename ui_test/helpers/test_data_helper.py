import json
import os
from typing import TypeVar, List, Optional
from model.game import Game

T = TypeVar('T')

def load_data(file_path: str) -> List[T]:
    absolute_file_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(absolute_file_path, 'r') as f:
        data = json.load(f)
    return data

_games_cache: Optional[List[Game]] = None

def load_games() -> List[Game]:
    global _games_cache
    if _games_cache is None:
        games_data = load_data('../data/games.json')
        _games_cache = [Game(**game) for game in games_data]
    return _games_cache

def get_game(name: str) -> Game:
    games = load_games()
    return next((game for game in games if game.name == name), None)
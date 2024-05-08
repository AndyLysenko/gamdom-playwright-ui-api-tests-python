from dataclasses import dataclass

@dataclass
class Game:
    """
    Game class that represents a game entity.
    """
    id: str
    name: str
    provider: str
    url: str
    game_provider_url: str
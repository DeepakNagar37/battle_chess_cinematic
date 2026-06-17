from ursina import Ursina, window
from src.game_manager import GameManager

app = Ursina()
window.title = "Battle Chess Cinematic"

game_manager = GameManager()

app.run()

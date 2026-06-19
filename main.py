from ursina import Ursina, window, mouse
from src.game_manager import GameManager
from src.camera_controller import CameraController

app = Ursina()
window.title = "Battle Chess Cinematic"

game_manager = GameManager()
camera_controller = CameraController()

def update():
    camera_controller.update()

def input(key):
    if key == 'scroll up':
        camera_controller.zoom(1)
    elif key == 'scroll down':
        camera_controller.zoom(-1)

app.run()

from ursina import Entity, color

class Board:
    def __init__(self):
        print("Board initialized")
        Entity(model='cube', color=color.white, position=(0, 0, 0), scale=(1, 0.2, 1))

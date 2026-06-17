from ursina import Entity, color

class Board:
    def __init__(self):
        print("Board initialized")
        for row in range(8):
            for col in range(8):
                tile_color = color.white if (row + col) % 2 == 0 else color.gray
                x = col - 3.5
                z = row - 3.5
                Entity(model='cube', color=tile_color, position=(x, 0, z), scale=(1, 0.2, 1))

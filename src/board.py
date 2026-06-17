from ursina import Entity, color

class Board:
    def __init__(self, game_manager):
        print("Board initialized")
        self.game_manager = game_manager
        self.tiles = []
        
        for row in range(8):
            for col in range(8):
                tile_color = color.white if (row + col) % 2 == 0 else color.gray
                x = col - 3.5
                z = row - 3.5
                tile = Entity(
                    model='cube',
                    color=tile_color,
                    position=(x, 0, z),
                    scale=(1, 0.2, 1),
                    collider='box'
                )
                tile.board_position = (col, row)
                tile.board = self
                self.tiles.append(tile)
    
    def on_click(self, tile):
        self.game_manager.tile_clicked(tile.board_position)

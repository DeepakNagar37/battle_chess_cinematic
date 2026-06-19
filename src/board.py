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
                tile.original_color = tile_color
                tile.board = self
                self.tiles.append(tile)
    
    def get_tile_at(self, board_position):
        for tile in self.tiles:
            if tile.board_position == board_position:
                return tile
        return None
    
    def highlight_tiles(self, positions):
        for position in positions:
            tile = self.get_tile_at(position)
            if tile:
                tile.color = color.green
    
    def clear_highlights(self):
        for tile in self.tiles:
            tile.color = tile.original_color
    
    def on_click(self, tile):
        self.game_manager.tile_clicked(tile.board_position)

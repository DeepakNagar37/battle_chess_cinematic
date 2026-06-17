from ursina import Entity, color

class Piece:
    def __init__(self, piece_type, color_name, board_position):
        self.piece_type = piece_type
        self.color = color_name
        self.board_position = board_position
        print(f"{color_name} {piece_type} created at {board_position}")
        
        x = board_position[0] - 3.5
        z = board_position[1] - 3.5
        piece_color = color.white if color_name == "white" else color.black
        self.entity = Entity(model='sphere', color=piece_color, position=(x, 0.5, z), scale=0.5)

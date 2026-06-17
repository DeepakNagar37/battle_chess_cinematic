class Piece:
    def __init__(self, piece_type, color, board_position):
        self.piece_type = piece_type
        self.color = color
        self.board_position = board_position
        print(f"{color} {piece_type} created at {board_position}")

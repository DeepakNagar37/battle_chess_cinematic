class ChessLogic:
    def __init__(self):
        print("ChessLogic initialized")
        self.piece_setup = [
            # White pieces
            {"piece_type": "rook", "color": "white", "board_position": (0, 0)},
            {"piece_type": "knight", "color": "white", "board_position": (1, 0)},
            {"piece_type": "bishop", "color": "white", "board_position": (2, 0)},
            {"piece_type": "queen", "color": "white", "board_position": (3, 0)},
            {"piece_type": "king", "color": "white", "board_position": (4, 0)},
            {"piece_type": "bishop", "color": "white", "board_position": (5, 0)},
            {"piece_type": "knight", "color": "white", "board_position": (6, 0)},
            {"piece_type": "rook", "color": "white", "board_position": (7, 0)},
            {"piece_type": "pawn", "color": "white", "board_position": (0, 1)},
            {"piece_type": "pawn", "color": "white", "board_position": (1, 1)},
            {"piece_type": "pawn", "color": "white", "board_position": (2, 1)},
            {"piece_type": "pawn", "color": "white", "board_position": (3, 1)},
            {"piece_type": "pawn", "color": "white", "board_position": (4, 1)},
            {"piece_type": "pawn", "color": "white", "board_position": (5, 1)},
            {"piece_type": "pawn", "color": "white", "board_position": (6, 1)},
            {"piece_type": "pawn", "color": "white", "board_position": (7, 1)},
            # Black pieces
            {"piece_type": "rook", "color": "black", "board_position": (0, 7)},
            {"piece_type": "knight", "color": "black", "board_position": (1, 7)},
            {"piece_type": "bishop", "color": "black", "board_position": (2, 7)},
            {"piece_type": "queen", "color": "black", "board_position": (3, 7)},
            {"piece_type": "king", "color": "black", "board_position": (4, 7)},
            {"piece_type": "bishop", "color": "black", "board_position": (5, 7)},
            {"piece_type": "knight", "color": "black", "board_position": (6, 7)},
            {"piece_type": "rook", "color": "black", "board_position": (7, 7)},
            {"piece_type": "pawn", "color": "black", "board_position": (0, 6)},
            {"piece_type": "pawn", "color": "black", "board_position": (1, 6)},
            {"piece_type": "pawn", "color": "black", "board_position": (2, 6)},
            {"piece_type": "pawn", "color": "black", "board_position": (3, 6)},
            {"piece_type": "pawn", "color": "black", "board_position": (4, 6)},
            {"piece_type": "pawn", "color": "black", "board_position": (5, 6)},
            {"piece_type": "pawn", "color": "black", "board_position": (6, 6)},
            {"piece_type": "pawn", "color": "black", "board_position": (7, 6)},
        ]

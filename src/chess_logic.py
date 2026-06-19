class ChessLogic:
    def __init__(self):
        print("ChessLogic initialized")
        self.current_turn = "white"
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
    
    def switch_turn(self):
        self.current_turn = "black" if self.current_turn == "white" else "white"
        print(f"Turn switched to {self.current_turn}")
    
    def is_legal_move(self, piece, target_position, game_manager):
        if piece.piece_type == "pawn":
            return self._is_legal_pawn_move(piece, target_position, game_manager)
        # Other pieces have no rules yet, allow any move
        return True
    
    def _is_legal_pawn_move(self, piece, target_position, game_manager):
        col, row = piece.board_position
        target_col, target_row = target_position
        
        # Direction depends on color
        direction = 1 if piece.color == "white" else -1
        starting_row = 1 if piece.color == "white" else 6
        
        col_diff = target_col - col
        row_diff = target_row - row
        
        target_piece = game_manager.get_piece_at(target_position)
        
        # Move one square forward
        if col_diff == 0 and row_diff == direction:
            return target_piece is None
        
        # Move two squares forward from starting position
        if col_diff == 0 and row_diff == 2 * direction and row == starting_row:
            one_ahead = (col, row + direction)
            return target_piece is None and game_manager.get_piece_at(one_ahead) is None
        
        # Diagonal capture
        if abs(col_diff) == 1 and row_diff == direction:
            return target_piece is not None and target_piece.color != piece.color
        
        return False

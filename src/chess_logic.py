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
        elif piece.piece_type == "knight":
            return self._is_legal_knight_move(piece, target_position, game_manager)
        elif piece.piece_type == "bishop":
            return self._is_legal_bishop_move(piece, target_position, game_manager)
        elif piece.piece_type == "rook":
            return self._is_legal_rook_move(piece, target_position, game_manager)
        elif piece.piece_type == "queen":
            return self._is_legal_queen_move(piece, target_position, game_manager)
        elif piece.piece_type == "king":
            return self._is_legal_king_move(piece, target_position, game_manager)
        return False
    
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

    def _is_legal_knight_move(self, piece, target_position, game_manager):
        col, row = piece.board_position
        target_col, target_row = target_position
        
        col_diff = abs(target_col - col)
        row_diff = abs(target_row - row)
        
        # Knight moves in L-shape: 2 in one direction, 1 in the other
        if not ((col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2)):
            return False
        
        target_piece = game_manager.get_piece_at(target_position)
        return target_piece is None or target_piece.color != piece.color
    
    def _is_legal_bishop_move(self, piece, target_position, game_manager):
        col, row = piece.board_position
        target_col, target_row = target_position
        
        col_diff = abs(target_col - col)
        row_diff = abs(target_row - row)
        
        # Bishop moves diagonally
        if col_diff != row_diff or col_diff == 0:
            return False
        
        # Check path is clear
        if not self._is_path_clear(piece.board_position, target_position, game_manager):
            return False
        
        target_piece = game_manager.get_piece_at(target_position)
        return target_piece is None or target_piece.color != piece.color
    
    def _is_legal_rook_move(self, piece, target_position, game_manager):
        col, row = piece.board_position
        target_col, target_row = target_position
        
        # Rook moves horizontally or vertically
        if col != target_col and row != target_row:
            return False
        
        # Check path is clear
        if not self._is_path_clear(piece.board_position, target_position, game_manager):
            return False
        
        target_piece = game_manager.get_piece_at(target_position)
        return target_piece is None or target_piece.color != piece.color
    
    def _is_legal_queen_move(self, piece, target_position, game_manager):
        # Queen moves like rook or bishop
        return (self._is_legal_rook_move(piece, target_position, game_manager) or 
                self._is_legal_bishop_move(piece, target_position, game_manager))
    
    def _is_legal_king_move(self, piece, target_position, game_manager):
        col, row = piece.board_position
        target_col, target_row = target_position
        
        col_diff = abs(target_col - col)
        row_diff = abs(target_row - row)
        
        # King moves one square in any direction
        if col_diff > 1 or row_diff > 1:
            return False
        
        if col_diff == 0 and row_diff == 0:
            return False
        
        target_piece = game_manager.get_piece_at(target_position)
        return target_piece is None or target_piece.color != piece.color
    
    def _is_path_clear(self, start_position, end_position, game_manager):
        col, row = start_position
        target_col, target_row = end_position
        
        col_step = 0 if col == target_col else (1 if target_col > col else -1)
        row_step = 0 if row == target_row else (1 if target_row > row else -1)
        
        current_col = col + col_step
        current_row = row + row_step
        
        while (current_col, current_row) != (target_col, target_row):
            if game_manager.get_piece_at((current_col, current_row)) is not None:
                return False
            current_col += col_step
            current_row += row_step
        
        return True

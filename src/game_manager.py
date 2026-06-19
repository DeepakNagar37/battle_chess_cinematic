from src.board import Board
from src.pieces import Piece
from src.chess_logic import ChessLogic
from src.environment import BattlefieldEnvironment
from src.ui_manager import UIManager

class GameManager:
    def __init__(self):
        print("GameManager initialized")
        self.environment = BattlefieldEnvironment()
        self.board = Board(self)
        self.chess_logic = ChessLogic()
        self.ui_manager = UIManager()
        self.selected_piece = None
        
        # Spawn all pieces from chess logic data
        self.pieces = []
        for piece_data in self.chess_logic.piece_setup:
            piece = Piece(
                piece_data["piece_type"],
                piece_data["color"],
                piece_data["board_position"],
                self
            )
            self.pieces.append(piece)
        
        # Initialize UI with current turn
        self.ui_manager.update_turn_label(self.chess_logic.current_turn)
    
    def get_piece_at(self, board_position):
        for piece in self.pieces:
            if piece.board_position == board_position:
                return piece
        return None
    
    def select_piece(self, piece):
        # Only allow selecting pieces of the current player's color
        if piece.color != self.chess_logic.current_turn:
            print(f"Cannot select {piece.color} piece - it's {self.chess_logic.current_turn}'s turn")
            return
        
        # Clear previous highlights
        self.board.clear_highlights()
        
        # If clicking the already selected piece, deselect it
        if self.selected_piece == piece:
            self.selected_piece.set_selected(False)
            self.selected_piece = None
            print(f"Deselected {piece.color} {piece.piece_type}")
        else:
            # Deselect previous piece if any
            if self.selected_piece:
                self.selected_piece.set_selected(False)
            
            # Select new piece
            self.selected_piece = piece
            piece.set_selected(True)
            print(f"Selected {piece.color} {piece.piece_type} at {piece.board_position}")
            
            # Highlight legal moves that don't leave king in check
            legal_moves = self.chess_logic.get_safe_legal_moves(piece, self)
            self.board.highlight_tiles(legal_moves)
    
    def tile_clicked(self, board_position):
        if not self.selected_piece:
            return
        
        # Check if move is legal and safe
        if not self.chess_logic.is_legal_move(self.selected_piece, board_position, self):
            print(f"Illegal move for {self.selected_piece.color} {self.selected_piece.piece_type}")
            return
        
        # Check if move would leave king in check
        if self.chess_logic.would_move_cause_check(self.selected_piece, board_position, self):
            print(f"Cannot move - would leave {self.selected_piece.color} king in check")
            return
        
        # Check if there's a piece at the target position
        target_piece = self.get_piece_at(board_position)
        
        if target_piece:
            # Cannot move onto friendly piece
            if target_piece.color == self.selected_piece.color:
                print(f"Cannot move onto friendly {target_piece.piece_type}")
                return
            
            # Capture with animation
            attacker = self.selected_piece
            self.selected_piece.set_selected(False)
            self.selected_piece = None
            
            def finish_capture():
                self.pieces.remove(target_piece)
                attacker.move_to(board_position)
                self.board.clear_highlights()
                self.chess_logic.switch_turn()
                self.ui_manager.update_turn_label(self.chess_logic.current_turn)
                self._check_for_check()
            
            attacker.play_capture_animation(target_piece, finish_capture)
        else:
            # Normal move
            self.selected_piece.move_to(board_position)
            self.selected_piece.set_selected(False)
            self.selected_piece = None
            self.board.clear_highlights()
            self.chess_logic.switch_turn()
            self.ui_manager.update_turn_label(self.chess_logic.current_turn)
            self._check_for_check()
    
    def _check_for_check(self):
        # Check if either king is in check
        white_in_check = self.chess_logic.is_king_in_check("white", self)
        black_in_check = self.chess_logic.is_king_in_check("black", self)
        self.ui_manager.update_check_warning(white_in_check, black_in_check)

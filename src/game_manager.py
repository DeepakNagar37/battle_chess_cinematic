from src.board import Board
from src.pieces import Piece
from src.chess_logic import ChessLogic

class GameManager:
    def __init__(self):
        print("GameManager initialized")
        self.board = Board(self)
        self.chess_logic = ChessLogic()
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
    
    def tile_clicked(self, board_position):
        if not self.selected_piece:
            return
        
        # Check if there's a piece at the target position
        target_piece = self.get_piece_at(board_position)
        
        if target_piece:
            # Cannot move onto friendly piece
            if target_piece.color == self.selected_piece.color:
                print(f"Cannot move onto friendly {target_piece.piece_type}")
                return
            
            # Capture enemy piece
            print(f"Capturing {target_piece.color} {target_piece.piece_type}")
            target_piece.remove()
            self.pieces.remove(target_piece)
        
        # Move the selected piece
        self.selected_piece.move_to(board_position)
        self.selected_piece.set_selected(False)
        self.selected_piece = None
        self.chess_logic.switch_turn()

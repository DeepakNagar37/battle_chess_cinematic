from src.board import Board

from src.board import Board
from src.pieces import Piece
from src.chess_logic import ChessLogic

class GameManager:
    def __init__(self):
        print("GameManager initialized")
        self.board = Board()
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
    
    def select_piece(self, piece):
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
        self.board = Board()

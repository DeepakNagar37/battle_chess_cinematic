from src.board import Board

from src.board import Board
from src.pieces import Piece
from src.chess_logic import ChessLogic

class GameManager:
    def __init__(self):
        print("GameManager initialized")
        self.board = Board()
        self.chess_logic = ChessLogic()
        
        # Spawn all pieces from chess logic data
        self.pieces = []
        for piece_data in self.chess_logic.piece_setup:
            piece = Piece(
                piece_data["piece_type"],
                piece_data["color"],
                piece_data["board_position"]
            )
            self.pieces.append(piece)
        self.board = Board()

from src.board import Board

from src.board import Board
from src.pieces import Piece
from src.chess_logic import ChessLogic

class GameManager:
    def __init__(self):
        print("GameManager initialized")
        self.board = Board()
        self.chess_logic = ChessLogic()
        
        # Spawn test piece from chess logic data
        test_data = self.chess_logic.piece_setup[0]
        self.test_piece = Piece(
            test_data["piece_type"],
            test_data["color"],
            test_data["board_position"]
        )
        self.board = Board()

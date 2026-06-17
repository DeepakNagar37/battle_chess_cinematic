from src.board import Board

from src.board import Board
from src.pieces import Piece
from src.chess_logic import ChessLogic

class GameManager:
    def __init__(self):
        print("GameManager initialized")
        self.board = Board()
        self.chess_logic = ChessLogic()
        self.test_piece = Piece("pawn", "white", (3, 3))
        self.board = Board()

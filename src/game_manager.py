from src.board import Board

from src.board import Board
from src.pieces import Piece

class GameManager:
    def __init__(self):
        print("GameManager initialized")
        self.board = Board()
        self.test_piece = Piece("pawn", "white", (3, 3))
        self.board = Board()

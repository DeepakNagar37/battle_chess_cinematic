from ursina import Entity, color, invoke, destroy

class Piece:
    def __init__(self, piece_type, color_name, board_position, game_manager):
        self.piece_type = piece_type
        self.color = color_name
        self.board_position = board_position
        self.game_manager = game_manager
        self.selected = False
        self.is_animating = False
        print(f"{color_name} {piece_type} created at {board_position}")
        
        # Convert board position (row, col) to world position
        col, row = board_position
        x = col - 3.5
        z = row - 3.5
        
        piece_color = color.white if color_name == "white" else color.black
        self.entity = Entity(
            model='sphere',
            color=piece_color,
            position=(x, 0.5, z),
            scale=0.5,
            collider='sphere'
        )
        self.entity.piece = self
        self.base_y = 0.5
    
    def on_click(self):
        if not self.is_animating:
            self.game_manager.select_piece(self)
    
    def set_selected(self, is_selected):
        self.selected = is_selected
        if is_selected:
            self.entity.position = (self.entity.x, self.base_y + 0.3, self.entity.z)
        else:
            self.entity.position = (self.entity.x, self.base_y, self.entity.z)
    
    def move_to(self, new_board_position):
        self.board_position = new_board_position
        col, row = new_board_position
        x = col - 3.5
        z = row - 3.5
        self.entity.position = (x, self.base_y, z)
        print(f"{self.color} {self.piece_type} moved to {new_board_position}")
    
    def play_capture_animation(self, target_piece, callback):
        self.is_animating = True
        print(f"{self.color} {self.piece_type} attacking {target_piece.color} {target_piece.piece_type}")
        
        # Quick scale pulse animation
        original_scale = self.entity.scale
        self.entity.animate_scale(original_scale * 1.3, duration=0.15)
        
        # After pulse, return to normal and remove target
        def finish_capture():
            self.entity.animate_scale(original_scale, duration=0.1)
            target_piece.remove()
            self.is_animating = False
            callback()
        
        invoke(finish_capture, delay=0.15)
    
    def remove(self):
        print(f"{self.color} {self.piece_type} captured")
        if self.entity:
            self.entity.animate_scale(0, duration=0.2)
            invoke(lambda: destroy(self.entity), delay=0.2)
            self.entity = None

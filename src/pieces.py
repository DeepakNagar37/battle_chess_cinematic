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
        
        # Get target position
        target_col, target_row = target_piece.board_position
        target_x = target_col - 3.5
        target_z = target_row - 3.5
        
        original_pos = (self.entity.x, self.entity.y, self.entity.z)
        original_scale = self.entity.scale
        
        if self.piece_type == "pawn":
            # Short forward lunge
            self.entity.animate_position((target_x, self.base_y + 0.3, target_z), duration=0.2)
            invoke(lambda: self._finish_animation(target_piece, callback, original_scale), delay=0.2)
        
        elif self.piece_type == "knight":
            # Quick charge with hop
            mid_x = (self.entity.x + target_x) / 2
            mid_z = (self.entity.z + target_z) / 2
            self.entity.animate_position((mid_x, self.base_y + 1, mid_z), duration=0.15)
            invoke(lambda: self.entity.animate_position((target_x, self.base_y, target_z), duration=0.1), delay=0.15)
            invoke(lambda: self._finish_animation(target_piece, callback, original_scale), delay=0.25)
        
        elif self.piece_type == "bishop":
            # Diagonal strike movement
            self.entity.animate_position((target_x, self.base_y + 0.5, target_z), duration=0.15)
            self.entity.animate_rotation((0, 360, 0), duration=0.15)
            invoke(lambda: self._finish_animation(target_piece, callback, original_scale), delay=0.15)
        
        elif self.piece_type == "rook":
            # Heavy smash with scale pulse
            self.entity.animate_scale(original_scale * 1.5, duration=0.1)
            invoke(lambda: self.entity.animate_scale(original_scale, duration=0.1), delay=0.1)
            invoke(lambda: self.entity.animate_position((target_x, self.base_y, target_z), duration=0.1), delay=0.1)
            invoke(lambda: self._finish_animation(target_piece, callback, original_scale), delay=0.2)
        
        elif self.piece_type == "queen":
            # Fast sharp strike
            self.entity.animate_position((target_x, self.base_y + 0.4, target_z), duration=0.12)
            self.entity.animate_scale(original_scale * 1.2, duration=0.12)
            invoke(lambda: self.entity.animate_scale(original_scale, duration=0.08), delay=0.12)
            invoke(lambda: self._finish_animation(target_piece, callback, original_scale), delay=0.2)
        
        elif self.piece_type == "king":
            # Slow powerful strike
            self.entity.animate_scale(original_scale * 1.4, duration=0.2)
            self.entity.animate_position((target_x, self.base_y + 0.2, target_z), duration=0.25)
            invoke(lambda: self.entity.animate_scale(original_scale, duration=0.15), delay=0.2)
            invoke(lambda: self._finish_animation(target_piece, callback, original_scale), delay=0.35)
    
    def _finish_animation(self, target_piece, callback, original_scale):
        self.entity.scale = original_scale
        target_piece.remove()
        self.is_animating = False
        callback()
    
    def remove(self):
        print(f"{self.color} {self.piece_type} captured")
        if self.entity:
            self.entity.animate_scale(0, duration=0.2)
            invoke(lambda: destroy(self.entity), delay=0.2)
            self.entity = None

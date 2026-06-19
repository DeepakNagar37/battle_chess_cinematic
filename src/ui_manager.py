from ursina import Text, color

class UIManager:
    def __init__(self):
        print("UIManager initialized")
        self._setup_turn_label()
    
    def _setup_turn_label(self):
        # Current turn label at top of screen
        self.turn_label = Text(
            text="White Turn",
            position=(-0.85, 0.45),
            scale=2,
            color=color.white,
            background=True
        )
        print("Turn label created")
    
    def update_turn_label(self, current_turn):
        # Update label based on current turn
        if current_turn == "white":
            self.turn_label.text = "White Turn"
            self.turn_label.color = color.white
        else:
            self.turn_label.text = "Black Turn"
            self.turn_label.color = color.black
        print(f"Turn label updated: {self.turn_label.text}")

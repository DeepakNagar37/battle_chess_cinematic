from ursina import Text, color

class UIManager:
    def __init__(self):
        print("UIManager initialized")
        self._setup_turn_label()
        self._setup_check_warning()
        self._setup_checkmate_message()
    
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
    
    def _setup_check_warning(self):
        # Check warning label
        self.check_warning = Text(
            text="",
            position=(-0.85, 0.35),
            scale=2,
            color=color.red,
            background=True
        )
        print("Check warning created")
    
    def update_turn_label(self, current_turn):
        # Update label based on current turn
        if current_turn == "white":
            self.turn_label.text = "White Turn"
            self.turn_label.color = color.white
        else:
            self.turn_label.text = "Black Turn"
            self.turn_label.color = color.black
        print(f"Turn label updated: {self.turn_label.text}")
    
    def update_check_warning(self, white_in_check, black_in_check):
        # Update check warning based on check status
        if white_in_check:
            self.check_warning.text = "White King in Check!"
            self.check_warning.color = color.red
            print("Check warning: White King in Check")
        elif black_in_check:
            self.check_warning.text = "Black King in Check!"
            self.check_warning.color = color.red
            print("Check warning: Black King in Check")
        else:
            self.check_warning.text = ""
            print("Check warning cleared")

    def _setup_checkmate_message(self):
        # Checkmate game-over message
        self.checkmate_message = Text(
            text="",
            position=(0, 0),
            scale=4,
            color=color.yellow,
            background=True
        )
        print("Checkmate message created")
    
    def show_checkmate(self, winner):
        # Display checkmate message with winner
        self.checkmate_message.text = f"Checkmate! {winner} wins!"
        self.checkmate_message.color = color.yellow
        print(f"Checkmate! {winner} wins!")

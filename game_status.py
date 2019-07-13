class GameStatus:
    """"Class to represent game status"""

    def __init__(self):
        # flags, 1 means True
        self.menu_active = 1
        self.game_active = 0
        self.pause_active = 0
        self.score_pause = 0

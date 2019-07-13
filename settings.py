class Settings:
    """Class holding game settings"""
    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.pitch_color = (25, 25, 25)
        self.border_thickness = 10
        self.pitch_border = self.border_thickness / 2
        self.middle_line_thickness = 2

        # Paddle settings
        self.paddle_width = 10
        self.paddle_height = 70
        self.paddle_color = (0, 0 , 0)
        self.paddle_step = 1

        # Ball settings
        self.ball_color = (0, 0, 0)
        self.ball_rad = 20
        self.ball_x_speed = 1.5
        self.ball_y_speed = 1

        # Score settings
        self.score_color = (0, 0, 0)

        # Misc
        self.max_diff = self.paddle_height/2 + self.ball_rad/2
        self.max_angle = 70

import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):
    """Class representing paddles"""

    def __init__(self, game, side):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        # flags
        self.moving_up = False
        self.moving_down = False

        # create a rect
        self.rect = pygame.Rect(0, 0, self.settings.paddle_width, self.settings.paddle_height)

        # sets the paddle x position depending if its left paddle or right paddle
        if side == 1:
            self.rect.x = 10
        elif side == 2:
            self.rect.x = self.screen_rect.right - 20

        # sets the paddle y position to the centre
        self.rect.centery = self.screen_rect.centery
        self.y = float(self.rect.y)

    def move(self):
        """Moves the paddle"""
        # paddle moving up, modify temporary pos
        if self.moving_up and self.rect.top > self.settings.border_thickness / 2:
            self.y -= self.settings.paddle_step

        # paddle moving down, modify temporary pos
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom - (self.settings.border_thickness / 2):
            self.y += self.settings.paddle_step

        # move the paddle according to the temporary position
        self.rect.y = self.y

    def center(self):
        """Centers the paddle position"""
        self.rect.centery = self.screen_rect.centery
        self.y = self.rect.y

    def draw_paddle(self):
        """"Moves the paddle, then draws the paddle to the screen"""
        self.move()
        pygame.draw.rect(self.screen, self.settings.paddle_color, self.rect)

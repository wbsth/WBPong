import pygame
import random
import math

class Ball:
    """Class representing ball behaviour"""

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.rect = pygame.Rect(0, 0, self.settings.ball_rad, self.settings.ball_rad)

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.directionx = random.choice([-1, 1])
        self.directiony = 1
        self.angle = 0

    def move(self):
        """Moves the ball"""
        self.x += self.settings.ball_x_speed * self.directionx
        ydiff = self.settings.ball_y_speed * math.sin(math.radians(self.angle)) * self.directiony
        self.y += ydiff

        self.rect.x = self.x
        self.rect.y = self.y

    def reset(self):
        """"Resets ball position"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.x = self.rect.x
        self.y = self.rect.y
        self.directionx = random.choice([-1, 1])
        self.directiony = 1
        self.angle = 0
        self.move()

    def draw(self):
        """Moves, then draw the ball"""
        pygame.draw.rect(self.screen, self.settings.ball_color, self.rect)


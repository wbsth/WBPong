import pygame
import time
import sys

from settings import Settings
from menu import Menu
from game_status import GameStatus
from paddle import Paddle
from ball import Ball
from score import Score
from button import Button

class WBPong:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.gamestatus = GameStatus()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("WBPong")

        self.main_menu = Menu(self, "Play", "Exit")
        self.pause_menu = Menu(self, "Resume", "New game", "Exit")
        self.pause_button = Button(self, 24, 50, 25, "Pause")
        self.left_paddle = Paddle(self, 1)
        self.right_paddle = Paddle(self, 2)
        self.ball = Ball(self)
        self.scores = Score(self)

    def run_game(self):
        """"Main loop of the game"""
        while True:
            self.screen.fill(self.settings.bg_color)
            if self.gamestatus.menu_active:
                self.main_menu.draw_menu()
            if self.gamestatus.game_active:
                # draw the border of the screen
                border = pygame.draw.rect(self.screen, self.settings.pitch_color, self.screen_rect,
                                          self.settings.border_thickness)

                # draw the middle pitch line
                middle_line = pygame.draw.line(self.screen, self.settings.pitch_color,
                                               (self.screen_rect.centerx, 0),
                                               (self.screen_rect.centerx, self.screen_rect.bottom),
                                               self.settings.middle_line_thickness)

                # draws the left paddle
                self.left_paddle.draw_paddle()
                self.right_paddle.draw_paddle()

                # draws the ball
                self.ball.draw()

                # draws the score
                self.scores.prep_score()

                # draws menu button
                self.pause_button.rect.topright = self.screen_rect.topright
                self.pause_button.draw_button()

                if not self.gamestatus.score_pause:
                    # moves the ball
                    self.ball.move()

                    # checks collisions
                    self._check_paddle_ball_collisions()
                    self._check_topdown_ball_collisions()

                    # check for goals
                    self._check_goals()


            if self.gamestatus.pause_active:
                self.pause_menu.draw_menu()

            self._check_events()

            # checking key and mouse presses
            pygame.display.flip()

    def _check_paddle_ball_collisions(self):
        """Checks collisions between paddle and ball"""
        if pygame.Rect.colliderect(self.left_paddle.rect, self.ball.rect):
            self.ball.directionx *= -1
            diff = - (self.left_paddle.rect.centery - self.ball.rect.centery)
            self.ball.angle = self.settings.max_angle * diff/self.settings.max_diff
        elif pygame.Rect.colliderect(self.right_paddle.rect, self.ball.rect):
            self.ball.directionx *= -1
            diff = - (self.right_paddle.rect.centery - self.ball.rect.centery)
            self.ball.angle = self.settings.max_angle * diff/self.settings.max_diff

    def _check_topdown_ball_collisions(self):
        """Change ball y direction if ball hit bottom or top"""
        if self.ball.rect.top <= self.settings.pitch_border \
                or self.ball.rect.bottom >= self.screen_rect.bottom - self.settings.pitch_border:
            self.ball.directiony *= -1

    def _check_goals(self):
        if self.ball.rect.left <= self.settings.pitch_border:
            self._goal_scored(1)
        if self.ball.rect.right >= self.screen_rect.right - self.settings.pitch_border:
            self._goal_scored(2)

    def _goal_scored(self, side):
        # zatrzymac pilke, ustawic w centrum
        # zresetowac paletk
        # ustawic wynik

        # pause
        self.gamestatus.score_pause = 1

        # sets score
        if side == 1:
            self.scores.scores[1] += 1
        elif side == 2:
            self.scores.scores[0] += 1

        # resets ball postion
        self.ball.reset()

        # resets paddle position
        self._reset_paddles()

        # delay
        time.sleep(2)

        # unpause
        self.gamestatus.score_pause = 0

    def _reset_paddles(self):
        self.right_paddle.center()
        self.left_paddle.center()

    def _check_events(self):
        """Responds to key and mouse presses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_mousedown_event(mouse_position)

    def _check_keydown_event(self, event):
        """Responds to keypresses"""
        if self.gamestatus.game_active:
            if event.key == pygame.K_UP:
                self.right_paddle.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.right_paddle.moving_down = True
            elif event.key == pygame.K_w:
                self.left_paddle.moving_up = True
            elif event.key == pygame.K_s:
                self.left_paddle.moving_down = True
            elif event.key == pygame.K_q:
                self.ball.reset()
                self.left_paddle.center()
                self.right_paddle.center()

    def _check_keyup_event(self, event):
        """Responds to key releases"""
        if self.gamestatus.game_active:
            if event.key == pygame.K_UP:
                self.right_paddle.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.right_paddle.moving_down = False
            elif event.key == pygame.K_w:
                self.left_paddle.moving_up = False
            elif event.key == pygame.K_s:
                self.left_paddle.moving_down = False

    def _check_mousedown_event(self, mouse_pos):
        """"Responds to mouse clicks"""
        # main menu active
        if self.gamestatus.menu_active:
            if self.main_menu.buttons[0].rect.collidepoint(mouse_pos):
                self._menu_to_game()
            if self.main_menu.buttons[1].rect.collidepoint(mouse_pos):
                # second button clicked, quit game
                sys.exit()

        # game active
        elif self.gamestatus.game_active:
            if self.pause_button.rect.collidepoint(mouse_pos):
                self._pausegame()
        elif self.gamestatus.pause_active:
            if self.pause_menu.buttons[0].rect.collidepoint(mouse_pos):
                self._resume_game()
            elif self.pause_menu.buttons[1].rect.collidepoint(mouse_pos):
                # New game
                self._newgame()
            elif self.pause_menu.buttons[2].rect.collidepoint(mouse_pos):
                # Exit
                sys.exit()

    def _newgame(self):
        self.ball.reset()
        self.left_paddle.center()
        self.right_paddle.center()
        self.scores.scores = [0, 0]
        self._resume_game()

    def _resume_game(self):
        self.gamestatus.game_active = 1
        self.gamestatus.pause_active = 0

    def _pausegame(self):
        self.gamestatus.game_active = 0
        self.gamestatus.pause_active = 1

    def _menu_to_game(self):
        self.gamestatus.menu_active = 0
        self.gamestatus.game_active = 1


if __name__ == '__main__':
    # Make a game instance, and run the game
    wbpong = WBPong()
    wbpong.run_game()

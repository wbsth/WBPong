import pygame.font

class Button:

    def __init__(self, game, font_size, button_width, button_height, msg):

        self.screen = game.screen

        # Set the attributes of the button
        self.font = pygame.font.SysFont(None, font_size)

        self.txt_color = (255, 255, 255)
        self.button_color = (150, 150, 150)

        # Build button rect
        self.rect = pygame.Rect(0, 0, button_width, button_height)

        # Prepare message
        self._make_text(msg)

    def _make_text(self, msg):
        """Make a rendered image from specified text"""
        self.msg_img = self.font.render(msg, True, self.txt_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()

    def draw_button(self):
        """Draws button, and text"""
        self.msg_img_rect.center = self.rect.center
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)

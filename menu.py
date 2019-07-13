from button import Button
import pygame


class Menu:
    def __init__(self, game, *argv):

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # buttons params
        self.button_number = len(argv)
        self.button_height = 50
        self.button_width = 200

        # empty button list
        self.buttons = []

        # menu params
        self.height = self.button_height * 2 + (self.button_number * 2 - 1) * 50
        self.width = 300
        self.menu_color = (200, 200, 200)

        # building menu rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # preparing buttons
        for i in range(self.button_number):
            self.buttons.append(Button(game, 48, self.button_width, self.button_height, argv[i]))

        self.draw_menu()

    def draw_menu(self):
        """Draws menu"""
        self.screen.fill(self.menu_color, self.rect)
        self.draw_buttons()


    def draw_buttons(self):
        """Draw buttons on top of menu"""
        for number, button in enumerate(self.buttons):
            button.rect.centerx = self.screen_rect.centerx
            button.rect.y = self.rect.top + 50 + number * 100
            button.draw_button()





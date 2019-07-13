import pygame.font


class Score:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.settings = game.settings
        self.scores = [0, 0]
        self.displacement = 50
        self.y = 50
        # Sets font type and size
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        self.scores_text = [str(i) for i in self.scores]
        self.scores_img = [self.font.render(i, True, self.settings.score_color) for i in self.scores_text]
        self.scores_rect = [i.get_rect() for i in self.scores_img]

        for rect in self.scores_rect:
            rect.y = self.y

        self.scores_rect[0].right = self.screen_rect.centerx - self.displacement
        self.scores_rect[1].left = self.screen_rect.centerx + self.displacement

        for i in range(len(self.scores_rect)):
            self.screen.blit(self.scores_img[i], self.scores_rect[i])




import pygame
from constants import LINE_COLOR, WIDTH, HEIGHT
from EasyMediumHard import draw_game_start

class WScreen:

    def __init__(self, screen):
        self.screen = screen

    def DrawScreen(self):

        win = pygame.image.load('win_screen.png')
        self.screen.blit(win, (0,0))

        button_font = pygame.font.Font(None, 70)
        restart_text = button_font.render("Exit", 0, (255, 255, 255))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill(LINE_COLOR)
        restart_surface.blit(restart_text, (10, 10))
        restart_rectangle = restart_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 100))
        self.screen.blit(restart_surface, restart_rectangle)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rectangle.collidepoint(event.pos):
                        pygame.quit()
                        exit()

            pygame.display.update()


class LScreen:

    def __init__(self, screen):
        self.screen = screen

    def DrawScreen(self):

        lose = pygame.image.load('lose_screen.png')
        self.screen.blit(lose, (0,0))

        button_font = pygame.font.Font(None, 70)
        restart_text = button_font.render("Restart", 0, (255, 255, 255))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill(LINE_COLOR)
        restart_surface.blit(restart_text, (10, 10))
        restart_rectangle = restart_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 100))
        self.screen.blit(restart_surface, restart_rectangle)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rectangle.collidepoint(event.pos):
                        pygame.quit()
                        from sudoku import Game
                        g = Game()
                        g.Run()

            pygame.display.update()


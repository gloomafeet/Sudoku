import pygame
from sudoku_generator import *
from EasyMediumHard import draw_game_start
from End_screen import *

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Sudoku")
    self.screen = pygame.display.set_mode((600, 800))

  def Run(self):
    difficulty = draw_game_start(self.screen)
    self.screen.fill((245, 245, 245))
    b = Board(600, 600, self.screen, difficulty)
    b.draw()

    while True:
      pygame.display.update()

      button_font = pygame.font.Font(None, 70)

      # Initialize buttons
      # Initialize text first
      easy_text = button_font.render("Reset", 0, (255, 255, 255))
      medium_text = button_font.render("Restart", 0, (255, 255, 255))
      hard_text = button_font.render("Exit", 0, (255, 255, 255))

      # Initialize button background color and text
      easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
      easy_surface.fill(LINE_COLOR)
      easy_surface.blit(easy_text, (10, 10))
      medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
      medium_surface.fill(LINE_COLOR)
      medium_surface.blit(medium_text, (10, 10))
      hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
      hard_surface.fill(LINE_COLOR)
      hard_surface.blit(hard_text, (10, 10))
      # Initialize button rectangle
      easy_rectangle = easy_surface.get_rect(
        center=(70, 800 - 50))
      medium_rectangle = medium_surface.get_rect(
        center=(300, 800 - 50))
      hard_rectangle = hard_surface.get_rect(
        center=(WIDTH - 70, 800 - 50))

      # Draw buttons
      self.screen.blit(easy_surface, easy_rectangle)
      self.screen.blit(medium_surface, medium_rectangle)
      self.screen.blit(hard_surface, hard_rectangle)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
          if easy_rectangle.collidepoint(event.pos):
            b.reset_to_original()
            print(b.CurrentInternalBoard)
            b.draw()
          elif medium_rectangle.collidepoint(event.pos):
            pygame.quit()
            g = Game()
            g.Run()
          elif hard_rectangle.collidepoint(event.pos):
            pygame.quit()
            quit()

        elif event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          cell = b.click(pos[0], pos[1])

          if cell != None:
            b.select(cell[0], cell[1])

        elif event.type == pygame.KEYDOWN:
          dif = event.key - 48
          if event.key == 13:
            b.place_number()

          if dif > 0 and dif < 10:
            if b.SelectedCell != None:
              b.sketch(dif)

g = Game()
g.Run()
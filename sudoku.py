import pygame
from board import *
from sudoku_generator import *
from EasyMediumHard import draw_game_start
from End_screen import *

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Sudoku")
    self.screen = pygame.display.set_mode((600, 600))

  def Run(self):
    difficulty = draw_game_start(self.screen)
    self.screen.fill((245, 245, 245))
    b = Board(600, 600, self.screen, difficulty)
    b.draw()

    while True:
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()

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
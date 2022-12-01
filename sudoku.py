import pygame
from board import *
from constants import *


pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((600, 600))
screen.fill((245,245,245))
b = Board(3, 3, WIDTH, HEIGHT, screen)
b.draw()



while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  pygame.display.update()
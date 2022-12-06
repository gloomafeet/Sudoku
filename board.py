import pygame
from constants import *
from cell import Cell


class Board:
    def _init_(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        removed = None
        if difficulty == "Easy":
            removed = 30
        elif difficulty == "Medium":
            removed = 40
        else:
            removed = 50

        self.board = generate_sudoku(9, removed)
        print(self.board)

    def draw(self):
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)

        for i in range(1, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (0, CELL_SIZE * i), (WIDTH, CELL_SIZE * i), int(LINE_WIDTH / 3))

        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

        for i in range(1, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (CELL_SIZE * i, 0), (CELL_SIZE * i, HEIGHT), int(LINE_WIDTH / 3))

        pygame.font.init()
        font = pygame.font.SysFont('Arial', 20, bold=False)

        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    img = font.render(str(self.board[row][col]), True, pygame.Color(0, 0, 0),
                                      pygame.Color(255, 255, 255))
                    position = (
                        (CELL_SIZE * col + (CELL_SIZE / 2)) - 5,
                        (CELL_SIZE * row + (CELL_SIZE / 2)) - 10
                    )
                    self.screen.blit(img, position)

    def select(self, row, col):
        currentcellvalue = 0  # board[row][col]
        currentcell = Cell(currentcellvalue, row, col, self.screen)
        currentcell.draw()

    def click(self, x, y):
        for i in range(2):
            if abs(x - ((i + 1) * 200)) <= int(LINE_WIDTH):
                return None

        for i in range(8):
            if abs(x - ((i + 1) * (CELL_SIZE))) <= int(LINE_WIDTH / 3):
                return None

        Xcell = math.floor(x / (600 / 9))

        for i in range(2):
            if abs(y - ((i + 1) * 200)) <= int(LINE_WIDTH):
                return None

        for i in range(8):
            if abs(y - ((i + 1) * (CELL_SIZE))) <= int(LINE_WIDTH / 3):
                return None

        Ycell = math.floor(y / (CELL_SIZE))

        return [Xcell, Ycell]

    def clear(self):
        Board[self.width][self.height] == " "

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        num = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    num += 1
        if num == 81:
            return True
        else:
            return False

    def update_board(self):
        pass

    def find_empty(self):
        found = True
        while found:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        return i, j
                        found = False
                    else:
                        continue

    def check_board(self):
        pass
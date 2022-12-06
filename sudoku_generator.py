import pygame
import math, random
from constants import *
from End_screen import *
from copy import deepcopy
import math, random


# class created to initialize the sudoku and make sure moves are valid
class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = 9
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(row_length)] for j in range(row_length)]
        self.box_length = int(math.sqrt(self.row_length))

    # initializes rows, removed cells, and board with 0s
    def get_board(self):
        return deepcopy(self.board)

    # returns board
    def print_board(self):
        for i in self.board:
            print(i)

        return self.board

    def valid_in_row(self, row, num):
        if num in self.board[row]:
            return False
        else:
            return True

    def valid_in_col(self, col, num):
        for i in range(9):
            if self.board[i][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        row = row_start
        col = col_start

        for i in range(3):
            for j in range(3):
                if self.board[row][col] == num:
                    return False
                else:
                    col += 1
            row += 1
            col = col_start

        return True

    def is_valid(self, row, col, num):
        row_start = (math.floor(row / 3) * 3)
        col_start = (math.floor(col / 3) * 3)

        isValidInRow = self.valid_in_row(row, num)
        isValidInCol = self.valid_in_col(col, num)
        isValidInBox = self.valid_in_box(row_start, col_start, num)

        if isValidInRow and isValidInCol and isValidInBox:
            return True
        else:
            return False

    def fill_box(self, row_start, col_start):
        row = row_start
        col = col_start

        for i in range(3):
            for j in range(3):
                while True:
                    SetNumber = random.randint(1, 9)

                    if self.valid_in_box(row_start, col_start, SetNumber):
                        self.board[row][col] = SetNumber
                        col += 1
                        break

            row += 1
            col = col_start

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(int(row), int(col), int(num)):
                self.board[int(row)][int(col)] = int(num)
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[int(row)][int(col)] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        num = self.removed_cells
        NumberOfRemovedCells = 0

        while NumberOfRemovedCells < num:
            remove_row = random.randint(0, 8)
            remove_col = random.randint(0, 8)

            if self.board[remove_row][remove_col] != 0:
                self.board[remove_row][remove_col] = 0
                NumberOfRemovedCells += 1


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    sudoku.remove_cells()
    return deepcopy(sudoku.get_board())


# to display the sudoku after we remove cells

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.SketchedValue = None

    def set_cell_value(self, value):
        pass

    def set_sketched_value(self, value):
        self.SketchedValue = value

    def draw(self, SelectedCell):
        pygame.font.init()

        if self.value != 0:
            font = pygame.font.SysFont('Arial', 25, bold=False)

            img = font.render(str(self.value), True, pygame.Color(0, 0, 0), pygame.Color(255, 255, 255))
            position = (
                (CELL_SIZE * self.col + (CELL_SIZE / 2)) - 5,
                (CELL_SIZE * self.row + (CELL_SIZE / 2)) - 10
            )
            self.screen.blit(img, position)

        if SelectedCell != None:
            if SelectedCell[0] == self.row and SelectedCell[1] == self.col:
                color = (255, 0, 0)
                left = self.row * (600 / 9)
                top = self.col * (600 / 9)
                pygame.draw.rect(self.screen, color, pygame.Rect(left, top, 600 / 9, 600 / 9), LINE_WIDTH)

        if self.SketchedValue != None:
            font = pygame.font.SysFont('Arial', 25, bold=False)

            img = font.render(str(self.SketchedValue), True, pygame.Color(80, 80, 80), pygame.Color(255, 255, 255))
            position = (
                (CELL_SIZE * self.col) + 13,
                (CELL_SIZE * self.row) + 13
            )
            self.screen.blit(img, position)


# check Board.py file and fix it
class Board:

    def __init__(self, width, height, screen, difficulty):
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

        self.OriginalBoard = generate_sudoku(9, difficulty)
        self.CurrentInternalBoard = deepcopy(self.OriginalBoard)

        self.CurrentCellBoard = self.CreateCellTable()
        self.SelectedCell = None
        print(self.CurrentInternalBoard)

    def CreateCellTable(self):
        CellTable = [[0 for i in range(9)] for j in range(9)]

        for row in range(9):
            for col in range(9):
                CellTable[row][col] = Cell(self.CurrentInternalBoard[row][col], row, col, self.screen)

        return CellTable

    def draw(self):
        self.screen.fill((255, 255, 255))

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
                self.CurrentCellBoard[row][col].draw(self.SelectedCell)

    def select(self, row, col):
        self.SelectedCell = [row, col]
        self.draw()

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
        if self.CurrentCellBoard[self.SelectedCell[1]][self.SelectedCell[0]].value == 0:
            self.CurrentCellBoard[self.SelectedCell[1]][self.SelectedCell[0]].set_sketched_value(value)
            self.draw()

    def place_number(self):  # Part done by Jatin
        if self.CurrentCellBoard[self.SelectedCell[1]][self.SelectedCell[0]].SketchedValue != None:
            self.CurrentInternalBoard[self.SelectedCell[1]][self.SelectedCell[0]] = self.CurrentCellBoard[self.SelectedCell[1]][self.SelectedCell[0]].SketchedValue
            self.CurrentCellBoard = self.CreateCellTable()
            self.draw()

            if self.check_board():
                newScreen = WScreen(self.screen)
                newScreen.DrawScreen()
            else:
                if self.is_full():
                    newScreen = LScreen(self.screen)
                    newScreen.DrawScreen()



    def reset_to_original(self):
        self.CurrentInternalBoard = deepcopy(self.OriginalBoard)
        self.CurrentCellBoard = self.CreateCellTable()
        self.SelectedCell = None
        self.draw()

    def is_full(self):
        num = 0
        for i in range(9):
            for j in range(9):
                if self.CurrentInternalBoard[i][j] != 0:
                    num += 1
        if num == 81:
            return True
        else:
            return False

    def update_board(self):
        self.draw()

    def find_empty(self):
        found = True
        while found:
            for i in range(9):
                for j in range(9):
                    if CurrentInternalBoard[i][j] == 0:
                        return i, j
                        found = False
                    else:
                        continue

    def valid_in_row(self, row, num):
        if num in self.CurrentInternalBoard[row]:
            element_counter = self.CurrentInternalBoard[row].count(num)

            if element_counter > 1:
                return False
            else:
                return True
        else:
            return True

    def valid_in_col(self, col, num):
        newColList = []
        for i in range(9):
            newColList.append(self.CurrentInternalBoard[i][col])

        element_counter = newColList.count(num)

        if element_counter > 1:
            return False
        else:
            return True

    def valid_in_box(self, row_start, col_start, num):
        row = row_start
        col = col_start

        newBoxList = []
        for i in range(3):
            for j in range(3):
                newBoxList.append(self.CurrentInternalBoard[row][col])
                col += 1

            row += 1
            col = col_start

        element_counter = newBoxList.count(num)

        if element_counter > 1:
            return False
        else:
            return True

    def check_board(self):
        if self.is_full():
            for row in range(9):
                for col in range(9):

                    row_start = (math.floor(row / 3) * 3)
                    col_start = (math.floor(col / 3) * 3)

                    isValidInRow = self.valid_in_row(row, self.CurrentInternalBoard[row][col])
                    isValidInCol = self.valid_in_col(col, self.CurrentInternalBoard[row][col])
                    isValidInBox = self.valid_in_box(row_start, col_start, self.CurrentInternalBoard[row][col])

                    if isValidInRow and isValidInCol and isValidInBox:
                        pass
                        # return True
                    else:
                        return False

            # End_screen.WScreen(screen)
            return True
        else:
            return False

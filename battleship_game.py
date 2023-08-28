import pygame
import sys
import random
import collections


class Battleship:
    def __init__(self, name: str, length: int, orientation: str) -> None:
        self.name = name
        self.length = length
        self.orientation = orientation
        self.is_sunk = False


    def hit(self):
        self.length -= 1
        if self.length == 0:
            self.is_sunk = True


class GameBoard:
    def __init__(self, board_size: int = 7) -> None:
        """Note that board_size must be at least 3 to accommodate all ships
        """
        self.board_size = board_size
        self.board = [['.' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ships = {"A": 3, "B": 2, "C": 1}  # Ship lengths
        self.ships_location = collections.defaultdict(list)
        self.game_over = False
        self.place_ships()


    def place_ships(self) -> None:
        for ship, length in self.ships.items():
            placed = False
            while not placed:
                orientation = random.choice(["horizontal", "vertical"])
                if orientation == "horizontal":
                    row = random.randint(0, self.board_size - 1)
                    col = random.randint(0, self.board_size - length)
                else:
                    row = random.randint(0, self.board_size - length)
                    col = random.randint(0, self.board_size - 1)
                
                if self._is_valid_placement(row, col, length, orientation):
                    new_ship = Battleship(ship, length, orientation)
                    for i in range(length):
                        if orientation == "horizontal":
                            self.board[row][col + i] = new_ship
                            self.ships_location[new_ship].append((row, col + i))  # switch to ship?
                        else:
                            self.board[row + i][col] = new_ship
                            self.ships_location[new_ship].append((row + i, col))  # switch to ship?
                    placed = True
                    

    def _is_valid_placement(self, row: int, col: int, length: int, orientation: int) -> bool:
        adjacent_positions = []
        if orientation == "horizontal":
            adjacent_positions.extend([(row, col + i) for i in range(length)])
        else:
            adjacent_positions.extend([(row + i, col) for i in range(length)])

        for r, c in adjacent_positions:
            if self.board[r][c] != '.':
                return False
        return True
    
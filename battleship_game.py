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


    def __str__(self):
        return 'O'


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
    

    def __str__(self):
        board_str = ""
        for row in self.board:
            row_str = []
            for item in row:
                if isinstance(item, Battleship):
                    row_str.append(str(item))
                else:
                    row_str.append(item)
            board_str += " ".join(row_str) + "\n"
        return board_str
    

    def attack(self, row: int, col: int) -> str:
        target = self.board[row][col]
        
        if isinstance(target, Battleship):
            ship_object = target
            ship_cells = self.ships_location[ship_object]
            ship_cells.remove((row, col))
            self.board[row][col] = "X"
            ship_object.hit()

            if not ship_cells:
                del self.ships_location[ship_object]
                return f"Ship {ship_object.name} has sunk!"
            else:
                return f"You hit ship {ship_object.name}!"
        elif target == '.':
            return 'You missed!'
        else:
            return 'You already hit this part of the ship.'
        
        
    def game_over(self) -> bool:
        for ship in self.ships_location:
            if not ship.is_sunk:
                return False
        
        return True


if __name__ == '__main__':
    ...

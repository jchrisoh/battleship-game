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
    
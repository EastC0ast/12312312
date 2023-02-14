import pygame
from Game import Game

class Hero:

    def __init__(self, rect,  xcord, ycord):
        self.rect = rect
        self.xcord = xcord
        self.ycord = ycord
        self.game = Game()


    def current_skin(self):
        pass

    def all_available_skin(self):
        pass


import pygame_menu
import pygame
from Game import Game

class Menu:

    def __init__(self):
        self.game = Game()

    def start_menu(self):
        pygame.init()
        menu = pygame_menu.Menu('Welcome', 650, 800,
                                theme=pygame_menu.themes.THEME_BLUE)
        menu.add.button('Play', self.game.start_game)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.game.screen)

    def choose_menu_theme(self):
        pass

    def create_menu(self):
        pass

    def quit(self):
        pass

    def to_game(self):
        pass


import pygame_menu
import pygame
from script import Game


class Menu:

    def __init__(self):
        self.game = Game()

    def start_menu(self):
        pygame.init()
        menu = pygame_menu.Menu('Little Clicker', 800, 500,
                                theme=pygame_menu.themes.THEME_BLUE)
        menu.add.button('Play', self.game.game_loop)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.game.game_display)

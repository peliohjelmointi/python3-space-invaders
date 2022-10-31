import pygame
import sys

class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.caption = "Space Invaders"
        #RGB (red, green, blue, 0-255 kunkin arvo)        
        self.bg_color = (0,0,255)

    def check_keys(self, game_ship):       
        # vastaanotetaan näppäin- ja hiirikomentoja
            for event in pygame.event.get(): 
                # mikäli ikkuna suljetaan
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        game_ship.moving_right = True
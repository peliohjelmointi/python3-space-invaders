import pygame
import sys

class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.caption = "Space Invaders"
    
    def check_keys(self):
        # while True = kunnes ruutu suljetaan
        while True: 
            # vastaanotetaan näppäin- ja hiirikomentoja
            for event in pygame.event.get(): 
                # mikäli ikkuna suljetaan
                if event.type == pygame.QUIT:
                    sys.exit()
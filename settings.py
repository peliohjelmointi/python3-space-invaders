import pygame
import sys

class Settings:
    def __init__(self):
    
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.caption = "Space Invaders"
        #RGB (red, green, blue, 0-255 kunkin arvo)        
        self.bg_color = (0,0,255)

        # ship settings
        self.ship_speed = 0.5

    def check_keys(self, game_ship):       
        # vastaanotetaan näppäin- ja hiirikomentoja
            for event in pygame.event.get(): 
                # mikäli ikkuna suljetaan
                if event.type == pygame.QUIT:
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        game_ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        game_ship.moving_left = True
            
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        game_ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        game_ship.moving_left = False
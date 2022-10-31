# jotta pygame toimii, tulee se importata
# suosittelen luomaan virtuaaliympäristön:
# python -m venv env
# ->sitten aktivoimaan sen: env\scripts\activate
# ->asennetaan pygame: pip install pygame
# ->jos vs codessa näkyy vielä sahalaitaisena, käynnistä uudelleen
import pygame 
from settings import Settings

class SpaceInvaders:
    def __init__(self):
        # pygamen initialisointi pitää tehdä aina ensimmäisenä
        pygame.init()         
        # luodaan olio Settings-luokasta
        self.settings = Settings()
        # asetetaan resoluutio (tämän faktoroimme myöhemmin)
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        # asetetaan yläpalkkiin pelin nimi
        pygame.display.set_caption(self.settings.caption)
        
    def run(self):
        self.settings.check_keys()

# ainoastaan, mikäli tätä tiedostoa yritetään ajaa:
if __name__ == '__main__':
    # luodaan olio eli instanssi luokasta:
    game = SpaceInvaders()
    # kutsutaan luokan metodia (metodi = luokan funktio)
    game.run()
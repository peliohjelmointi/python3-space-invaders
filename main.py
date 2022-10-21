# jotta pygame toimii, tulee se importata
# suosittelen luomaan virtuaaliympäristön:
# python -m venv env
# ->sitten aktivoimaan sen: env\scripts\activate
# ->asennetaan pygame: pip install pygame
# ->jos vs codessa näkyy vielä sahalaitaisena, käynnistä uudelleen
import pygame 
import sys

class SpaceInvaders:
    def __init__(self):
        # pygamen initialisointi pitää tehdä aina ensimmäisenä
        pygame.init() 
        # asetetaan resoluutio (tämän faktoroimme myöhemmin)
        self.screen = pygame.display.set_mode((1200,800))
        # asetetaan yläpalkkiin pelin nimi
        pygame.display.set_caption("Space Invaders")

    def run(self):
        # while True = kunnes ruutu suljetaan
        while True: 
            # vastaanotetaan näppäin- ja hiirikomentoja
            for event in pygame.event.get(): 
                # mikäli ikkuna suljetaan
                if event.type == pygame.QUIT:
                    sys.exit()

# ainoastaan, mikäli tätä tiedostoa yritetään ajaa:
if __name__ == '__main__':
    # luodaan olio eli instanssi luokasta:
    game = SpaceInvaders()
    # kutsutaan luokan metodia (metodi = luokan funktio)
    game.run()
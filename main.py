# jotta pygame toimii, tulee se importata
# suosittelen luomaan virtuaaliympäristön:
# python -m venv env
# ->sitten aktivoimaan sen: env\scripts\activate
# ->asennetaan pygame: pip install pygame
# ->jos vs codessa näkyy vielä sahalaitaisena, käynnistä uudelleen
import pygame 
from settings import Settings
from ship import Ship

class SpaceInvaders:
    def __init__(self):
        # pygamen initialisointi pitää tehdä aina ensimmäisenä
        pygame.init()         
        # luodaan olio Settings-luokasta
        self.settings = Settings()
        # asetetaan resoluutio
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        # asetetaan yläpalkkiin pelin nimi
        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self) #ship-olio saa 
                            # käyttöönsä kaikki
                            # olion muuttujat
        
    def run(self):
        # main loop
        while True: 
            self.settings.check_keys(self.ship)
            #täytetään ruutu sinisellä värillä
            self.screen.fill(self.settings.bg_color)
            #piirretään alus ruudulle
            self.ship.blit()
            self.ship.update()
            # päivitetään ruudulta vain päivittyneet kohdat
            pygame.display.flip()

# ainoastaan, mikäli tätä tiedostoa yritetään ajaa:
if __name__ == '__main__':
    # luodaan olio eli instanssi luokasta:
    game = SpaceInvaders()
    # kutsutaan luokan metodia (metodi = luokan funktio)
    game.run()
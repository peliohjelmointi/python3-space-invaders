# jotta pygame toimii, tulee se importata
# suosittelen luomaan virtuaaliympäristön:
# python -m venv env
# ->sitten aktivoimaan sen: env\scripts\activate
# ->asennetaan pygame: pip install pygame
# ->jos vs codessa näkyy vielä sahalaitaisena, käynnistä uudelleen
import pygame 
from settings import Settings
from ship import Ship
from events import Events


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
        # asetetaan taustakuva muuttujaan
        self.bg_image = pygame.image.load("images/starfield.png").convert_alpha()

        self.ship = Ship(self) 
        self.events = Events()

    def run(self): 
        
        while True: # main loop
            self.events.check_keys(self.ship)       #täytetään ruutu sinisellä värillä        
            self.screen.blit(self.bg_image, self.screen.get_rect())
            #self.screen.fill((0,0,0),self.screen.get_rect())
            self.ship.blit()                        #piirretään alus ruudulle        
            self.ship.update() 
            self.ship.update_bullets() #kutsuu jokaisen 
                                        #bulletin update()-metodia                    
            for b in self.ship.bullets:  #.sprites()
                b.draw_bullet() #piirretään kukin bullet

            pygame.display.flip()                 # päivitetään päivittyneet kohdat

# ainoastaan, mikäli tätä tiedostoa yritetään ajaa:
if __name__ == '__main__':
    # luodaan olio eli instanssi luokasta:
    game = SpaceInvaders()
    # kutsutaan luokan metodia (metodi = luokan funktio)
    game.run()
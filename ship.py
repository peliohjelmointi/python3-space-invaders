import pygame

class Ship:
    def __init__(self,game):     
        # haetaan pääohjelman screen-muuttuja, asetaan olion käyttöön   
        self.screen = game.screen        
        #screen_rect-muuttujaan haetaan pääohjelman screen-muuttujan
        # dimensiot (mahdollistaa mm. midbottom-käytön)
        self.screen_rect = game.screen.get_rect()
        # haetaan image-muuttujaan kuva
        # TODO: laita try:n "taakse"!
        self.image = pygame.image.load('images/ship.png').convert_alpha()
        # rect-muuttujaan asetetaan kuvan dimensiot
        self.rect = self.image.get_rect()
        #asetetaan olion suorakulmio keskelle pääohjelman ruudun alaosaa         
        self.rect.midbottom = self.screen_rect.midbottom

        #asetetaan oikealle liikkuminen aluksi Falseksi
        self.moving_right = False

    def blit(self): #blittaus on kuvien piirtämistä
        #piirretään kuva, 1.parametri on kuva, toinen on dimensio
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.x +=1
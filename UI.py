import pygame

class Text:
    def __init__(self, game,x,y):
       self.screen = game.screen
       self.text_color = (255,255,255)  #white
       self.font = pygame.font.SysFont(None,48)
       #self.font = pygame.font.Font('fontin_nimi.ttf',48)
       self.x = x
       self.y = y
       self.game = game

    def blit(self):
        text_string= str(self.game.ship.x) #convert to string
        text = self.font.render(text_string,True,self.text_color)
        text_rect = text.get_rect()
        text_rect.topleft = (self.x,self.y)
        self.screen.blit(text,text_rect)



                    
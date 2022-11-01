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

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,255,255)
        self.bullet_speed = 0.5
        self.bullets_allowed = 3
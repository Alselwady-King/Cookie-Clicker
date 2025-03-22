import pygame
from sys import exit
from paths import IMAGE_DIR
from paths import TEXT_DIR




pygame.init()

width = 1500
height = 900

screen = pygame.display.set_mode((width, height))
cookie = pygame.image.load(IMAGE_DIR / "cookiePic.png").convert_alpha()
background = pygame.image.load(IMAGE_DIR / "candle.jpg").convert_alpha()
background = pygame.transform.scale(background, (1500,900))


cookieSize = pygame.transform.smoothscale_by(cookie, .5)


font = pygame.font.Font(TEXT_DIR / 'fonten.otf', 52)


my_text = font.render('Cookie Clicker', True, '#e3ab9f')








pygame.display.set_caption('Cookie Clicker')
clock = pygame.time.Clock()






class Game:
    def __init__(self):
        self.cookies = 0
        self.cookie_per_click = 1
        self.cookie = cookieSize.get_rect(topleft=(50, 50))
        self.clicked = False




    def draw_score(self):
        self.display_cookies = font.render(f'Cookies: {str(self.cookies)}',True, 'white')
        screen.blit(self.display_cookies, (50,300))
    def click_button(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if self.cookie.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]: # 0 is left click, 1 is scroll wheel, 2 is right click.
                self.clicked = True
            else:
                if self.clicked:
                    self.cookies += 1
                    self.clicked = False









    #def auto_clicker(self): work on this
     


    def render(self):
        self.click_button()
        self.draw_score()













game = Game()





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(background, (0,0))
    screen.blit(my_text,(580,50))
    screen.blit(cookieSize, (50,50))
    game.render()
    
    pygame.display.update()
    clock.tick(60)

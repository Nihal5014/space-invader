import pygame


HEIGHT = 800
WIDTH = 1000
TITLE = "Space invader"
run = True
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

img1 = pygame.image.load("images\\yellow spaceship.png")
img2 = pygame.image.load("images\\red spaceship.png")
bg = pygame.image.load("images\\galaxy image.png")
bg = pygame.transform.scale(bg,[1000,800])
img2 = pygame.transform.scale(img2,[100,100])
img1 = pygame.transform.scale(img1,[100,100])
img2 = pygame.transform.rotate(img2,270)
img1 = pygame.transform.rotate(img1,90)

class spaceship(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

spaceship_y = spaceship(img1,210,250)
spaceship_r = spaceship(img2,750,250)
sprites = pygame.sprite.Group()
sprites.add(spaceship_y)
sprites.add(spaceship_r)



while run == True:
    screen.blit(bg,(0,0))
    sprites.draw(screen)
    pygame.draw.line(screen,"yellow",(500,0),(500,800),5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_UP]:
        spaceship_r.rect.y = spaceship_r.rect.y-1
    if key_press[pygame.K_DOWN]:
        spaceship_r.rect.y = spaceship_r.rect.y+1
    if key_press[pygame.K_LEFT]:
        spaceship_r.rect.x = spaceship_r.rect.x-1
    if key_press[pygame.K_RIGHT]:
        spaceship_r.rect.x = spaceship_r.rect.x+1
    


    pygame.display.update()

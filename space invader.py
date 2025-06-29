import pygame
pygame.init()
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
health_r = 100
health_y = 100

red_bullets = []
yellow_bullets = []
def handle_bullets():
    global health_y
    global health_r
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,"yellow",bullet)
        bullet.x = bullet.x+0.75
        if bullet.colliderect(spaceship_r.rect):
            health_r = health_r - 10
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        pygame.draw.rect(screen,"red",bullet) 
        bullet.x = bullet.x-0.75
        if bullet.colliderect(spaceship_y.rect):
            health_y = health_y - 10
            red_bullets.remove(bullet)
while run == True:
    screen.blit(bg,(0,0))
    sprites.draw(screen)
    pygame.draw.line(screen,"yellow",(500,0),(500,800),5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                bullet = pygame.Rect(spaceship_y.rect.x,spaceship_y.rect.y,15,5)
                yellow_bullets.append(bullet)
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_m:
                bullet2 =  pygame.Rect(spaceship_r.rect.x,spaceship_r.rect.y,15,5)
                red_bullets.append(bullet2)
    
    font = pygame.font.SysFont('arial',30)
    text = font.render("health"+str(health_r),True,'white')
    screen.blit(text,[800,25])
    
    font =  pygame.font.SysFont ('arial',30)
    text = font.render("health"+str(health_y),True,'white')
    screen.blit(text,[100,25])
    handle_bullets()

    if health_r == 0:
        font = pygame.font.SysFont('arial',40)
        text = font.render("GAME OVER , Yellow is the winner",True,'white')
        screen.blit(text,(400,525))
        pygame.display.update()
        pygame.time.delay(5000)
        run = False
    
    if health_y == 0:
        font = pygame.font.SysFont('arial',40)
        text = font.render("GAME OVER , Red is the winner",True,'white')
        screen.blit(text,(400,525))
        pygame.display.update()
        pygame.time.delay(5000)
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
    
    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_w]:
         spaceship_y.rect.y = spaceship_y.rect.y-1
    if key_press[pygame.K_s]:
        spaceship_y.rect.y = spaceship_y.rect.y+1
    if key_press[pygame.K_a]:
        spaceship_y.rect.x = spaceship_y.rect.x-1 
    if key_press[pygame.K_d]:
        spaceship_y.rect.x = spaceship_y.rect.x+1
    
    if spaceship_y.rect.top < 0:
        spaceship_y.rect.top = 0
    if spaceship_y.rect.left < 0:
        spaceship_y.rect.left = 0
    if spaceship_y.rect.bottom > 800:
        spaceship_y.rect.bottom = 800
    if spaceship_y.rect.right>500:
        spaceship_y.rect.right = 500
    
    if spaceship_r.rect.top < 0:
        spaceship_r.rect.top = 0
    if spaceship_r.rect.left < 500:
        spaceship_r.rect.left = 500
    if spaceship_r.rect.bottom >800:
        spaceship_r.rect.bottom = 800
    if spaceship_r.rect.right > 1000:
        spaceship_r.rect.right = 1000


        
    
    
    
    pygame.display.update()

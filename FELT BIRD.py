import pygame
from random import randrange
pygame.init()
pygame.display.set_caption("Felt noobie birdie")
bird_dsa = pygame.image.load('image/Nft hehehe.PNG')
pygame.display.set_icon(bird_dsa)
speed = 8
w = 900
h = 900
H = 5*h//6
S = h//3
u = 145
FPS = 50
t = 2 * FPS
a = (S - u*t)*2//t**2
a = abs(a)

print(a)
jump = False
abb = "FELT DOWN BIRD"
sc = pygame.display.set_mode((w, h))
bg = pygame.image.load('image/BackgroundFeltBird.PNG').convert()
bg = pygame.transform.scale(bg, (w, 770))
sc.blit(bg, (0,0))
hero= pygame.image.load('image/Roblox Amongus.png').convert_alpha()
hero_rect = hero.get_rect()
hero_rect.centerx = w//2
hero_rect.centery = h//6*6
sc.blit(hero, hero_rect)
clock = pygame.time.Clock()
sc.fill((255, 255, 255))
color1 = (randrange(0, 256), randrange(0, 256), randrange(0, 256))
color2 = (115, 81, 132)
color3 = (43,141,36)
f = pygame.font.SysFont('arial', 56)
sc_text = f.render(str(abb), 1, color3, (255, 255, 255))
pygame.draw.rect(sc, color3, (0, H, w, h))
pygame.draw.circle(sc, color1, (w//2, H-50), 50)
R = 50
pygame.draw.aaline(sc, color3, (0, H), (w, H))
sc.blit(sc_text, (w//4, h//2))
pipe = pygame.image.load('image/pixilart-drawing (3).png').convert_alpha()
pipe2 = pygame.transform.flip(pipe, 0, 1)
xl = w
x2 = w + 2*w//3
yl = randrange(100, h - h//2 - h//6 - 100)
y2 = randrange(100, h - h//2 - h//6 - 100)
pygame.display.update()
choto = 0
while 1==1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
                u = 35
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                jump = True
                u = 35

    if jump:
        u = u - a
        hero_rect.centery = hero_rect.centery - u
    else:
        u = 0
    if hero_rect.centery > H-50:
        hero_rect.centery = H-50
        jump = False
    elif hero_rect.centery < 0:
        hero_rect.centery = 0+50
    if xl < -100:
        xl = w
        yl = randrange(100, h - h//2 - h//6 - 100)
    if x2 < -100:
       x2 = w
       y2 = randrange(100, h - h//2 - h//6 - 100)
    xl = xl - speed
    x2 = x2 - speed
    sc.fill((255, 255, 255))
    f = pygame.font.SysFont('arial', 56)
    sc.blit(bg, (0,0))
    sc.blit(hero, hero_rect)
    if hero_rect.x - xl == 4 or hero_rect.x - x2 == 4:
        choto = choto + 1
    rect1 = pygame.Rect(xl, 0, 100, yl)
    rect2 = pygame.Rect(xl, yl + h//2, 100, h-h//2-yl-h//6)
    rect3 = pygame.Rect(x2, 0, 100, y2)
    if choto == 11 or choto > 11:
        rect4 = pygame.Rect(x2, y2 + h//2 , 100, h-h//2-y2-h//6)

    wall_1 = pygame.transform.scale(pipe, (100, yl))
    wall_2 = pygame.transform.scale(pipe2, (100, h-h//2-yl-h//6))
    wall_3 = pygame.transform.scale(pipe, (100, y2))
    if choto == 11 or choto > 11:
        wall_4 = pygame.transform.scale(pipe2, (100, h-h//2-y2-h//6))

    sc.blit(wall_1, rect1)
    pygame.draw.rect(sc, color3, (0, H, w, h//6))
    sc.blit(wall_2, rect2)
    sc.blit(wall_3, rect3)


    if choto == 11 or choto > 11:
       sc.blit(wall_4, rect4)
    sc_text = f.render(str(abb), 1, color3, (255, 255, 255))
    sc_text.set_colorkey((255, 255, 255))
    sc.blit(sc_text, (w//4, h//2))
    sc_text2 = f.render(str(choto), 1, (0,0,0), (255, 255, 255))
    sc_text2.set_colorkey((255, 255, 255))
    sc.blit(sc_text2, (800, 10))
    ##colision box
    #pygame.draw.rect(sc, color2, hero_rect)

    pygame.display.update()
    if choto == 11 or choto > 11:
        if hero_rect.colliderect(rect4):
            jump = False
            speed = 0
            abb = "Youre dead bozo"
            color3 = (255, 0, 0)
    if hero_rect.colliderect(rect1) or hero_rect.colliderect(rect2) or hero_rect.colliderect(rect3):
        jump = False
        speed = 0
        abb = "Youre dead bozo"
        color3 = (255, 0, 0)
    clock.tick(FPS)

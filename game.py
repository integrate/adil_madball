import pygame, settings
pygame.init()
variable = 0

lifes = 0
level = 1
hits_to_end = 10

letters = pygame.font.match_font("arial", True, False)
print(letters)

f = pygame.font.Font(letters, 20)

r = pygame.Rect(10, 10, 20, 20)

c = pygame.Rect(600, 80, 100, 100)

basespeed = 3
speedy = basespeed
speedx = basespeed
k = pygame.image.load("supports/descarga.png").convert()
k = pygame.transform.scale(k, (100, 100))

k.set_colorkey([255, 255, 255])

def game(screen):
    global lifes, level, hits_to_end, basespeed, speedy, speedx


    mode = "GAME"

    #events

    t = pygame.event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                r.height = settings.SCREEN_HEIGHT
                r.width = settings.BORDERWIDTH
                r.y = 0
                r.right = settings.SCREEN_WIDTH
                if r.colliderect(c):
                    c.right = r.left
                    speedx = -basespeed
                    hits_to_end -= 1

            if i.key == pygame.K_LEFT:
                r.height = settings.SCREEN_HEIGHT
                r.width = settings.BORDERWIDTH
                r.left = 0
                r.y = 0
                if r.colliderect(c):
                    c.left = r.right
                    speedx = basespeed
                    hits_to_end -= 1


            if i.key == pygame.K_UP:
                r.width = settings.SCREEN_WIDTH
                r.height = settings.BORDERWIDTH
                r.top = 0
                r.x = 0
                if r.colliderect(c):
                    c.top = r.bottom
                    speedy = basespeed
                    hits_to_end -= 1


            if i.key == pygame.K_DOWN:
                r.width = settings.SCREEN_WIDTH
                r.height = settings.BORDERWIDTH
                r.bottom = settings.SCREEN_HEIGHT
                r.x = 0
                if r.colliderect(c):
                    c.bottom = r.top
                    speedy = -basespeed
                    hits_to_end -= 1








    c.x += speedx


    if c.right > settings.SCREEN_WIDTH:
        c.right = settings.SCREEN_WIDTH
        lifes -= 1
        speedx = -basespeed

    if c.left < 0:
        c.left = 0
        lifes -= 1
        speedx = basespeed


    if c.colliderect(r):
        hits_to_end -= 1
        if speedx < 0:
            c.left = r.right
            speedx = basespeed

        elif speedx > 0:
            c.right = r.left
            speedx = -basespeed





    c.y += speedy


    if c.bottom > settings.SCREEN_HEIGHT :
        c.bottom = settings.SCREEN_HEIGHT
        lifes -= 1
        speedy = -basespeed


    if c.top < 0:
        c.top = 0
        lifes -= 1
        speedy = basespeed



    if c.colliderect(r):
        hits_to_end -= 1
        if speedy > 0:
            c.bottom = r.top
            speedy = -basespeed


        elif speedy < 0:
            c.top = r.bottom
            speedy = basespeed


    if lifes == -1:
        lifes = 0
        return "MENU"


    if hits_to_end == 0:
        hits_to_end = 10
        basespeed += 2
        speedy = basespeed
        speedx = basespeed
        level += 1






    #rendering

    screen.fill([variable % 255, 255, variable % 180])

    lives = f.render("LIVES = " + str(lifes), True, [0, 0, 255])
    lewel = f.render("LEVEL = " + str(level), True, [0, 0, 255])
    hits = f.render("HITS TO END = " + str(hits_to_end), True, [0, 0, 255])


    pygame.draw.rect(screen, [189, 0, 0], r)


    #pygame.draw.circle(screen, [0, 0, 255], [c.centerx, c.centery], 20)
    #pygame.draw.rect(screen, [67, 0, 0], c)
    screen.blit(lives, [900, 30])
    screen.blit(lewel, (900, 10))
    screen.blit(hits, [900, 50])
    screen.blit(k, c)
    pygame.display.flip()


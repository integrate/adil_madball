import pygame, os, time, menu
os.environ["SDL_VIDEODRIVER"] = "directx"
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BORDERWIDTH = 100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#SCREEN_WIDTH = screen.get_width()
#SCREEN_HEIGHT = screen.get_height()

mode = "MENU"



variable = 0


lifes = 1000
level = 1
hits_to_end = 10

letters = pygame.font.match_font("arial", True, False)
print(letters)

f = pygame.font.Font(letters, 20)

r = pygame.Rect(10, 10, 20, 20)

c = pygame.Rect(600, 80, 40, 40)



basespeed = 3
speedy = basespeed
speedx = basespeed

#if mode == "GAME":
running = True

while running:
    time.sleep(1 / 60)
    if mode == "MENU":
        m = menu.menu(screen)
        if m == "GAME":
            mode = "GAME"

    elif mode == "GAME":

        #events

        t = pygame.event.get()
        for i in t:
            if i.type == pygame.QUIT:
                exit()

            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_RIGHT:
                    r.height = SCREEN_HEIGHT
                    r.width = BORDERWIDTH
                    r.y = 0
                    r.right = SCREEN_WIDTH
                    if r.colliderect(c):
                        c.right = r.left
                        speedx = -basespeed
                        hits_to_end -= 1

                if i.key == pygame.K_LEFT:
                    r.height = SCREEN_HEIGHT
                    r.width = BORDERWIDTH
                    r.left = 0
                    r.y = 0
                    if r.colliderect(c):
                        c.left = r.right
                        speedx = basespeed
                        hits_to_end -= 1


                if i.key == pygame.K_UP:
                    r.width = SCREEN_WIDTH
                    r.height = BORDERWIDTH
                    r.top = 0
                    r.x = 0
                    if r.colliderect(c):
                        c.top = r.bottom
                        speedy = basespeed
                        hits_to_end -= 1


                if i.key == pygame.K_DOWN:
                    r.width = SCREEN_WIDTH
                    r.height = BORDERWIDTH
                    r.bottom = SCREEN_HEIGHT
                    r.x = 0
                    if r.colliderect(c):
                        c.bottom = r.top
                        speedy = -basespeed
                        hits_to_end -= 1








        c.x += speedx


        if c.right > SCREEN_WIDTH :
            c.right = SCREEN_WIDTH
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


        if c.bottom > SCREEN_HEIGHT :
            c.bottom = SCREEN_HEIGHT
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
            exit()

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
        #pygame.draw.rect(screen, [67, 0, 0], c)
        pygame.draw.circle(screen, [0, 0, 255], [c.centerx, c.centery], 20)
        screen.blit(lives, [900, 30])
        screen.blit(lewel, (900, 10))
        screen.blit(hits, [900, 50])

        pygame.display.flip()





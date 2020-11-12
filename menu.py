import pygame, settings
pygame.init()
font = pygame.font.match_font("arial", True, False)
print(font)

fo = pygame.font.Font(font, 100)
text = fo.render("PRESS SPACE TO START", True, [255, 255, 255])
y = pygame.Rect(50, 50, text.get_width(), text.get_height())

y.centerx = settings.SCREEN_WIDTH // 2
y.centery = settings.SCREEN_HEIGHT // 2

def menu(screen):
    bc = "MENU"

    t = pygame.event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
               bc = "GAME"



    #drawing frame

    bck = pygame.image.load("supports/menu background.jpg")
    screen.blit(bck, [0, 0])
    pygame.draw.rect(screen, [255, 0, 0], y)
    screen.blit(text, [y.left, y.top])

    pygame.display.flip()

    return bc
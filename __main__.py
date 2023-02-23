import pygame, os, time, settings
# os.environ["SDL_VIDEODRIVER"] = "directx"
pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
import game, menu



mode = "MENU"

while True:
    time.sleep(1 / 60)

    if mode == "MENU":
        m = menu.menu(screen)
        if m == "GAME":
            mode = "GAME"


    elif mode == "GAME":
        g = game.game(screen)
        if g == "MENU":
            mode = "MENU"
            # game.save_records()
            game.restart()


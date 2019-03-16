import pygame

pygame.init()

# Set window resolution
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))

# Set window title
pygame.display.set_caption('Space')

# Set window "FPS"
clock = pygame.time.Clock()


def game_loop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

    clock.tick(30)


game_loop()
pygame.quit()
quit()

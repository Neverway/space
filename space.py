import logging

import pygame
from pygame.locals import *


log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())
clock = pygame.time.Clock()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((1, 255, 1))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


def create_display(height=600, width=800, title=True):
    """
    Create a PyGame display.

    :param height: Vertical resolution in pixels
    :param width: Horizontal resolution in pixels
    :param title: Window title
    :return: A PyGame display object
    """
    display = pygame.display.set_mode((width, height))
    try:
        pygame.display.set_caption(title)
    except TypeError:
        log.debug("Using default title")
    return display


def game_loop(display):
    game_exit = False
    mob = Mob()

    while not game_exit:
        for event in pygame.event.get():
            log.debug(event)
            if event.type == pygame.QUIT:
                game_exit = True
            pressed_keys = pygame.key.get_pressed()

        mob.update(pressed_keys)
        display.blit(mob.surf, mob.rect)
        pygame.display.flip()
        clock.tick(30)


def main():
    """Run the program."""
    # Set window resolution
    display_width = 800
    display_height = 600

    pygame.init()
    display = create_display(display_height, display_width, 'Space')
    game_loop(display)
    pygame.quit()



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

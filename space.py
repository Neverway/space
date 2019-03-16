import pygame


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
        pass
    return display


def game_loop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True


def main():
    """Run the program."""
    # Set window resolution
    display_width = 800
    display_height = 600

    pygame.init()
    create_display(display_height, display_width, 'Space')
    game_loop()
    pygame.quit()


if __name__ == '__main__':
    main()

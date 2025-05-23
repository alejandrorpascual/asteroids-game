import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    upadatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, upadatable, drawable)
    AsteroidField.containers = upadatable
    asteroid_field = AsteroidField()

    Player.containers = (upadatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        upadatable.update(dt)

        screen.fill("black")

        for g in drawable:
            g.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

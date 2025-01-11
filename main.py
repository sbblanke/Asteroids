import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid, Shot
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = pygame.Color(0,0,0,255)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()

    shots = pygame.sprite.Group()
    Shot.containers = (shots,)

    Player.containers = (updatable_group, drawable_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2, shots)

    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable_group, drawable_group)

    AsteroidField.containers = (updatable_group,)

    asteroid = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(black)

        for object in updatable_group:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        shots.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.kill()

        for object in drawable_group:
            object.draw(screen)

        for shot in shots:
            shot.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

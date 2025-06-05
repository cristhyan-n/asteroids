import pygame, sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (drawable, updatable, shoots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = fps.tick(60) / 1000
        updatable.update(dt)
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        for thing in asteroids:
            if thing.collision_check(player):
                print("Game over!")
                sys.exit()
            for bullet in shoots:
                if bullet.collision_check(thing):
                    bullet.kill()
                    thing.split()

        pygame.display.flip()


if __name__ == "__main__":
    main()

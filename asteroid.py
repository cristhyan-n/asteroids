from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            split_velocity1 = self.velocity.rotate(random_angle)
            split_velocity2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = self.__class__(
                self.position.x, self.position.y, new_radius
            )
            new_asteroid_1.velocity = split_velocity1 * 1.2
            new_asteroid_2 = self.__class__(
                self.position.x, self.position.y, new_radius
            )
            new_asteroid_2.velocity = split_velocity2 * 1.2

import pygame
import random

from circleshape import *
from constants import SHOT_RADIUS, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(random_angle)
            vector_2 = self.velocity.rotate(-random_angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            broken_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            broken_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            broken_asteroid1.velocity = vector_1 * 1.2
            broken_asteroid2.velocity = vector_2 * 1.2


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS

    def update(self, dt):
        self.position += self.velocity * dt


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 0)

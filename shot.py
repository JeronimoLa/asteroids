import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, SHOT_RADIUS, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt


class BigShot(Shot):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, SHOT_RADIUS, width=5)

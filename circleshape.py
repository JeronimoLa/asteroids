import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collisions(self, CircleShapeObject):
        dist = pygame.math.Vector2.distance_to(self.position, CircleShapeObject.position)
        if dist <= self.radius+ CircleShapeObject.radius:
            return True
    
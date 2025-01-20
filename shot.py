from circleshape import *

class Shot(CircleShape):
    def __init__(x, y, radius):
        SHOT_RADIUS = 5
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

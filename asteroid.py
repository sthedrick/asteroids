import pygame
import circleshape
from constants import *


class Asteroid(circleshape.CircleShape):
    
    def __init__(self, x, y, radius=2):
        super().__init__(x,y, radius)
        
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    

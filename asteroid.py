import pygame
import circleshape
import random
from constants import *
from asteroidfield import *


class Asteroid(circleshape.CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return # small asteroid just goes away
        
        #spawn 2 asteroids
        r = random.uniform(20,50)
        v = self.velocity
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = self.velocity.rotate(-r)
        asteroid1.velocity *= 1.2
        
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = self.velocity.rotate(+r)
        asteroid2.velocity *= 1.2

        return (asteroid1, asteroid2)


    

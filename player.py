from pygame import *
from circleshape import *
from constants import *
from shot import *



class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        a = self.position + forward * self.radius # type: ignore
        b = self.position - forward * self.radius - right # type: ignore
        c = self.position - forward * self.radius + right # type: ignore
        return [a, b, c]
        
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # A spin left
            self.rotate(-dt)
        if keys[pygame.K_d]: # D spin right
            self.rotate(dt)
        if keys[pygame.K_s]: # S Forward
            self.move(dt)
        if keys[pygame.K_w]: # W Backward
            self.move(-dt)
        if keys[pygame.K_SPACE]: # space Shoot
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot = Shot()
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

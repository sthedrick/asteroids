import sys
import pygame
from    constants import *
from    player import *
from    asteroidfield import *
from    circleshape import *
import asteroid



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0

    #sprite containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable) # type: ignore
    Asteroid.containers = (updatable, drawable, asteroids) # type: ignore
    Shot.containers = (updatable, drawable, shots) # type: ignore
    AsteroidField.containers = (updatable) # type: ignore
    asteroid_field = AsteroidField()
    # updatable.add(asteroid_field)


    #create player and add it to the 2 groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # updatable.add(player)
    # drawable.add(player)

    
    print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    
    #game loop
    while(True):
        # 1) Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # 2) update game state
        updatable.update(dt)
        for a in asteroids:
            if player.overlaps(a):
                print("Game over!")
                sys.exit()
                return

        
        # 3) Clear screen
        screen.fill("BLACK")
        
        # 4) Draw everything
        for obj in drawable:
            obj.draw(screen)

        #5) Flip to display the frame
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = gameClock.tick(60)/1000


if __name__ == "__main__":
    main()





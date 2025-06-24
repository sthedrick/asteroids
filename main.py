import pygame
from    constants import *
from    player import *
import circleshape 


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    fps = gameClock.get_fps()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    

    #game loop
    while(True):
        # 1) Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # 2) update game state

        
        # 3) Clear screen
        screen.fill("BLACK")
        
        # 4) Draw everything
        player.draw(screen)

        #5) Flip to display the frame
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = gameClock.tick(60)/1000


if __name__ == "__main__":
    main()





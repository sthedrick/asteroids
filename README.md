# asteroids
This is a basic asteroids game built to learn more about the pygame interface.  Includes moving, shooting, splitting asteroids, and collision detection

* circleshape.py - Base class for game objects.  Holds position, velocity and radius of asteroids, player ship and shots.  Contains function to test if 2 objects are overlapping
        
* asteroid.py - building from circleshape, it includes additional code to split an asteroid into 2 when hit

* asteroidfield.py - this class contains the main sprite code for spawning asteroids of various sizes and speeds

* player.py -  class to handle the player ship, motions, and shooting

* shot.py - class to create and move shots on the screen

* main.py - main game play logic loop, sprite containers, testing for shots, crashes between player and asteroid

* constants.py and requirements.txt - settings files with gameplay constants and pygame version settings 

This project was part of a training module from boot.dev that explained the basics of pygame and provided guidance about building the classes and pointed me to important sections of the pygame documentation
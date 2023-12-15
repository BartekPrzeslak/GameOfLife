# GameOfLife

 To create & start using python venv:
       python -m venv venv
       source venv/bin/activate
 Install specific modules with pip:
 f.e.:   pip install pygame

 ## Requirements
 1. Make simulation real time
 2. Add pause / resume logic
 3. Add save / load logic

## High-level logic
 1. Create and init the simulation grid
 2. Start the simulation with a tick interval of <n> seconds
 3. At each tick:
   3.1. Update the grid - loop over each element of the board
   3.2. Render new generation

 ## General approach
 1. Plan & write down the general workflow
  1.1. Define Input&Output 
  1.2. Consider adding validation
 2. Separate the main algorithms / actors in the code. Try to abstract as much common code as possible
 3. Define communication between the objects
 4. List the patterns you could apply
 5. Build PoCs (Proof of concepts). Try to separate implementation of specific steps. Prepare smaller modules
    and combine them into a complete application
 6. Refine if needed

 ## Deadline - 15th of December 2023
 Mail with: 
 1. short screen recording demonstrating the new features
 2. Linked code
 3. Short description of the changes. Which design patterns you used and how you applied them.

# Libraries
pygame: is used for the game's graphical interface and handling user input

numpy: is used for numerical operations on the game state array.

os:  is used for interacting with the operating system, specifically for file-related operations.

# Methods:

**GameOfLife class methods**:

- `__new__(cls)`: A special method used for creating and returning a new instance of the class. In this case, it ensures that only one instance of the GameOfLife class is created (Singleton pattern).
- `initialize(self)`: Initializes the game, including Pygame, screen dimensions, grid dimensions, game state, colors, button dimensions, and clock.
- `draw_button(self, rect, text)`: Draws a button on the screen using Pygame.
- `draw_grid(self)`: Draws the grid on the screen using Pygame.
- `next_generation(self)`: Calculates the next generation of the Game of Life based on the rules.
- `draw_cells(self)`: Draws the live cells on the screen using Pygame.
- `run(self)`: The main loop that runs the game, handling events, updating the screen, and controlling the frame rate.




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

## Libraries Used

- **pygame**: Utilized for creating the graphical user interface and handling game-related functionalities.
- **numpy**: Used for creating and manipulating arrays for the game state.
- **os**: Enables interaction with the operating system, used for file-related operations.

## Techniques and Methods

### Classes and Methods
- **GameOfLifeApp**: Manages the Game of Life application, including game logic and graphical interface.
    - `draw_grid(self)`: Draws the grid on the screen.
    - `next_generation(self)`: Computes the next generation of the game state based on rules.
    - `draw_cells(self)`: Draws the cells on the screen.
    - `run(self)`: Main loop for running the game.

### Attributes
- `width, height`: Screen dimensions.
- `n_cells_x, n_cells_y`: Grid dimensions.
- `cell_width, cell_height`: Dimensions of individual cells in the grid.
- `game_state`: Current state of the Game of Life.
- `white, black, gray, green`: Colors used in the graphical interface.
- `button_width, button_height`: Dimensions of buttons.
- `button_gap`: Gap between buttons.
- `button_x, button_y`: Position of buttons on the screen.
- `clock`: Controls the frame rate.
- `paused`: Boolean to control the pause state.

### Rectangles for Buttons
- `pause_button_rect, save_button_rect, load_button_rect`: Rectangles for Pause/Resume, Save, and Load buttons.

## How to run it
To run the Game of Life, execute the main file `gameoflife.py`.

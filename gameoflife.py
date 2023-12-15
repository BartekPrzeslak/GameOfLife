import pygame
import numpy as np
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Grid dimensions
n_cells_x, n_cells_y = 40, 30
cell_width = width // n_cells_x
cell_height = height // n_cells_y

# Game state
game_state = np.random.choice([0, 1], size=(n_cells_x, n_cells_y), p=[0.8, 0.2])

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
green = (0, 255, 0)

# Button dimensions
button_width, button_height = 150, 50  # Adjust the button width here
button_gap = 20  # Adjust the gap between buttons here
button_x, button_y = (width - 3 * button_width - 2 * button_gap) // 2, height - button_height - 10

# Clock to control the frame rate
clock = pygame.time.Clock()

# Boolean to control the pause state
paused = False

def draw_button(rect, text):
    pygame.draw.rect(screen, green, rect)
    font = pygame.font.Font(None, 36)
    text = font.render(text, True, black)
    text_rect = text.get_rect(center=(rect.x + rect.width // 2, rect.y + rect.height // 2))
    screen.blit(text, text_rect)

def draw_grid():
    for y in range(0, height, cell_height):
        for x in range(0, width, cell_width):
            cell = pygame.Rect(x, y, cell_width, cell_height)
            pygame.draw.rect(screen, gray, cell, 1)

def next_generation():
    global game_state
    new_state = np.copy(game_state)

    for y in range(n_cells_y):
        for x in range(n_cells_x):
            n_neighbors = game_state[(x - 1) % n_cells_x, (y - 1) % n_cells_y] + \
                          game_state[(x)     % n_cells_x, (y - 1) % n_cells_y] + \
                          game_state[(x + 1) % n_cells_x, (y - 1) % n_cells_y] + \
                          game_state[(x - 1) % n_cells_x, (y)     % n_cells_y] + \
                          game_state[(x + 1) % n_cells_x, (y)     % n_cells_y] + \
                          game_state[(x - 1) % n_cells_x, (y + 1) % n_cells_y] + \
                          game_state[(x)     % n_cells_x, (y + 1) % n_cells_y] + \
                          game_state[(x + 1) % n_cells_x, (y + 1) % n_cells_y]

            if game_state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                new_state[x, y] = 0
            elif game_state[x, y] == 0 and n_neighbors == 3:
                new_state[x, y] = 1

    game_state = new_state

def draw_cells():
    for y in range(n_cells_y):
        for x in range(n_cells_x):
            cell = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)
            if game_state[x, y] == 1:
                pygame.draw.rect(screen, black, cell)

# Rectangles for Pause/Resume, Save, and Load buttons
pause_button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
save_button_rect = pygame.Rect(pause_button_rect.right + button_gap, button_y, button_width, button_height)
load_button_rect = pygame.Rect(save_button_rect.right + button_gap, button_y, button_width, button_height)

running = True
while running:
    screen.fill(white)
    draw_grid()
    draw_cells()

    # Draw Pause/Resume button based on the paused state
    if paused:
        draw_button(pause_button_rect, "Resume")
    else:
        draw_button(pause_button_rect, "Pause")

    # Draw Save button
    draw_button(save_button_rect, "Save")

    # Draw Load button
    draw_button(load_button_rect, "Load")

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the Pause/Resume button is clicked
            if paused and pause_button_rect.collidepoint(event.pos):
                paused = not paused
            elif not paused and pause_button_rect.collidepoint(event.pos):
                paused = not paused
            # Check if the Save button is clicked
            elif save_button_rect.collidepoint(event.pos):
                np.save("saved_game_state.npy", game_state)
            # Check if the Load button is clicked
            elif load_button_rect.collidepoint(event.pos):
                if os.path.exists("saved_game_state.npy"):
                    game_state = np.load("saved_game_state.npy")
            else:
                x, y = event.pos[0] // cell_width, event.pos[1] // cell_height
                game_state[x, y] = not game_state[x, y]

    # Update the simulation only if not paused
    if not paused:
        next_generation()

    clock.tick(10)  # Adjust the frames per second as needed

pygame.quit()

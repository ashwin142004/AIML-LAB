import random

# Constants
GRID_SIZE = 3  # Size of the grid (3x3)
DIRTY = 'D'
CLEAN = 'C'
VACUUM = 'V'

# Create a grid with random dirt placement
def create_grid(size):
    return [[random.choice([DIRTY, CLEAN]) for _ in range(size)] for _ in range(size)]

# Print the grid
def print_grid(grid, vacuum_pos):
    print("-" * (GRID_SIZE * 4))  # Grid border
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) == vacuum_pos:
                print(f'[{VACUUM}]', end=' ')
            else:
                print(f' {grid[i][j]} ', end=' ')
        print()
    print("-" * (GRID_SIZE * 4))  # Grid border
    print()

# Simple Reflex Agent
def simple_reflex_agent(grid, vacuum_pos):
    x, y = vacuum_pos
    if grid[x][y] == DIRTY:
        print(f"→ Cell ({x}, {y}) is dirty. Cleaning...")
        grid[x][y] = CLEAN
    else:
        print(f"→ Cell ({x}, {y}) is already clean. Moving next.")

# Get next position for the vacuum
def get_next_position(pos, grid_size):
    x, y = pos
    if y < grid_size - 1:  # Move right if not at the end of the row
        return x, y + 1
    elif x < grid_size - 1:  # Move down to the next row
        return x + 1, 0
    return None  # No more positions to move to (finished)

# Main Function
def main():
    grid = create_grid(GRID_SIZE)
    vacuum_pos = (0, 0)  # Start at the top-left corner

    print("\n=== Initial Grid ===")
    print_grid(grid, vacuum_pos)

    while vacuum_pos:
        simple_reflex_agent(grid, vacuum_pos)
        print_grid(grid, vacuum_pos)
        vacuum_pos = get_next_position(vacuum_pos, GRID_SIZE)

    print("✅ All cells are clean!")

if __name__ == "__main__":
    main()

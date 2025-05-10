#Simple Reflex Agent
import random

GRID_SIZE = 3
DIRTY, CLEAN, VACUUM = 'D', 'C', 'V'

def create_grid(size): return [[random.choice([DIRTY, CLEAN]) for _ in range(size)] for _ in range(size)]

def print_grid(grid, pos):
    print("-" * (GRID_SIZE * 4))
    for i in range(GRID_SIZE):
        print(' '.join(f'[{VACUUM}]' if (i, j) == pos else f' {grid[i][j]} ' for j in range(GRID_SIZE)))
    print("-" * (GRID_SIZE * 4), "\n")

def main():
    grid = create_grid(GRID_SIZE)
    pos = (0, 0)
    print("\n=== Initial Grid ===")
    print_grid(grid, pos)

    while pos:
        x, y = pos
        if grid[x][y] == DIRTY:
            print(f"→ Cleaning cell ({x}, {y})")
            grid[x][y] = CLEAN
        else:
            print(f"→ Cell ({x}, {y}) already clean")
        print_grid(grid, pos)
        pos = (x, y + 1) if y < GRID_SIZE - 1 else (x + 1, 0) if x < GRID_SIZE - 1 else None

    print("✅ All cells are clean!")

if __name__ == "__main__":
    main()

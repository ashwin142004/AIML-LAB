import numpy as np
import random

# Grid size (n x n)
grid_size = 3

# Initialize Q-table: shape = [rows, cols, actions]
# 4 actions: 0 = up, 1 = right, 2 = down, 3 = left
Q_table = np.zeros((grid_size, grid_size, 4))

# Possible movements for actions: [Up, Right, Down, Left]
action_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Define the step function
def step(state, action):
    """Takes a step in the grid world and returns new state and reward."""
    row, col = state
    d_row, d_col = action_directions[action]

    # Apply movement and clip to stay within grid
    new_row = np.clip(row + d_row, 0, grid_size - 1)
    new_col = np.clip(col + d_col, 0, grid_size - 1)
    new_state = (new_row, new_col)

    # Reward: +98 for reaching the goal, -1 for every other step
    reward = 99 if new_state == (grid_size - 1, grid_size - 1) else -1
    return new_state, reward

# Training loop
num_episodes = 500
learning_rate = 0.1      # Alpha
discount_factor = 0.9    # Gamma

for episode in range(num_episodes):
    state = (0, 0)  # Start from top-left
    epsilon = max(0.1, 1 * 0.99**episode)  # Epsilon decay

    while state != (grid_size - 1, grid_size - 1):  # Until goal is reached
        # Choose action: Explore (random) or Exploit (best known)
        if random.random() < epsilon:
            action = random.randint(0, 3)
        else:
            action = Q_table[state].argmax()

        next_state, reward = step(state, action)

        # Q-learning update rule
        old_value = Q_table[state][action]
        next_max = Q_table[next_state].max()

        Q_table[state][action] = old_value + learning_rate * (reward + discount_factor * next_max - old_value)

        state = next_state  # Move to next state

# Show learned Q-values
print("Q-table (rounded):")
print(np.round(Q_table, 1))

# Show best action (0–3) at each state
print("\nBest actions for each state:")
print(Q_table.argmax(axis=2))

# Follow the learned path from start to goal
print("\nLearned path from (0, 0) to goal:")
state = (0, 0)
path = [state]

while state != (grid_size - 1, grid_size - 1):
    action = Q_table[state].argmax()
    state, _ = step(state, action)
    path.append(state)

print(path)

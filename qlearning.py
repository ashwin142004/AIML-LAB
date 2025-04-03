import numpy as np 

import random 

import matplotlib.pyplot as plt 

 

# Define the grid environment 

# 0: Empty cell, 1: Obstacle, 2: Goal 

grid = np.array([ 

    [0, 0, 0, 1, 0], 

    [0, 1, 0, 1, 0], 

    [0, 1, 0, 0, 0], 

    [0, 0, 0, 1, 2] 

]) 

 

# Define the size of the grid 

n_rows, n_cols = grid.shape 

 

# Define the possible actions: Up, Right, Down, Left 

actions = ['up', 'right', 'down', 'left'] 

action_map = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)} 

 

# Q-table initialization (state space = n_rows * n_cols, actions = 4) 

Q = np.zeros((n_rows * n_cols, len(actions))) 

 

# Define parameters 

alpha = 0.1  # Learning rate 

gamma = 0.9  # Discount factor 

epsilon = 0.1  # Exploration rate 

episodes = 1000  # Number of episodes to train 

max_steps = 100  # Max steps per episode 

 

# Function to get the state index from row and column 

def state_to_index(row, col): 

    return row * n_cols + col 

 

# Function to get row and column from the state index 

def index_to_state(index): 

    return divmod(index, n_cols) 

 

# Check if a move is valid 

def is_valid_move(row, col): 

    # Check if the new position is within bounds and not an obstacle 

    if 0 <= row < n_rows and 0 <= col < n_cols and grid[row, col] != 1: 

        return True 

    return False 

 

# Function to choose the next action using epsilon-greedy 

def epsilon_greedy(state): 

    if random.uniform(0, 1) < epsilon: 

        return random.choice(range(len(actions)))  # Explore: Random action 

    else: 

        return np.argmax(Q[state])  # Exploit: Choose the best action 

 

# Function to run a single episode 

def run_episode(start_row, start_col): 

    state = state_to_index(start_row, start_col) 

    total_reward = 0 

    for _ in range(max_steps): 

        # Choose the next action 

        action_idx = epsilon_greedy(state) 

        action = actions[action_idx] 

         

        # Get the new state based on the chosen action 

        row, col = index_to_state(state) 

        delta_row, delta_col = action_map[action] 

        new_row, new_col = row + delta_row, col + delta_col 

         

        # Check if the new state is valid 

        if is_valid_move(new_row, new_col): 

            new_state = state_to_index(new_row, new_col) 

        else: 

            new_state = state  # Stay in the same state if move is invalid 

         

        # Define the reward: Goal gives +1, otherwise -0.1 for each step 

        if 0 <= new_row < n_rows and 0 <= new_col < n_cols:  # Check if the new position is within bounds 

            if grid[new_row, new_col] == 2: 

                reward = 1  # Goal state 

                total_reward += reward 

                break  # Episode ends when goal is reache 

            else: 

                reward = -0.1  # Small negative reward for each step 

                total_reward += reward 

        else: 

            reward = -0.1  # Negative reward for invalid move 

            total_reward += reward 

         

        # Update Q-table using the Q-learning update rule 

        Q[state, action_idx] = Q[state, action_idx] + alpha * (reward + gamma * np.max(Q[new_state]) - Q[state, action_idx]) 

         

        # Move to the next state 

        state = new_state 

     

    return total_reward 

 

# Training the Q-learning agent 

rewards = [] 

for episode in range(episodes): 

    start_row, start_col = 0, 0  # Start position (0,0) 

    total_reward = run_episode(start_row, start_col) 

    rewards.append(total_reward) 

     

    if episode % 100 == 0: 

        print(f"Episode {episode}: Total Reward = {total_reward}") 

 

# Plot the rewards over time to visualize learning progress 

plt.plot(rewards) 

plt.xlabel('Episodes') 

plt.ylabel('Total Reward') 

plt.title('Q-learning Training Progress') 

plt.show() 

 

# Show the learned Q-table 

print("Learned Q-table:") 

print(Q) 

 

# Visualize the path taken by the agent (if needed, e.g., after training) 

def visualize_solution(start_row, start_col): 

    state = state_to_index(start_row, start_col) 

    path = [(start_row, start_col)] 

     

    while True: 

        action_idx = np.argmax(Q[state])  # Choose the best action based on the learned Q-table 

        action = actions[action_idx] 

        row, col = index_to_state(state) 

        delta_row, delta_col = action_map[action] 

        new_row, new_col = row + delta_row, col + delta_col 

         

        if not is_valid_move(new_row, new_col):  # If the move is invalid (out of bounds or obstacle) 

            break  # End if no valid move 

         

        path.append((new_row, new_col))  # Add valid move to the path 

        state = state_to_index(new_row, new_col) 

         

        if grid[new_row, new_col] == 2:  # Goal reached 

            path.append((new_row, new_col)) 

            break 

     

    # Plot the path taken by the agent 

    path = np.array(path) 

    plt.imshow(grid, cmap='gray', origin='upper') 

    plt.plot(path[:, 1], path[:, 0], color='red', marker='o', linestyle='-', markersize=5) 

    plt.title('Learned Path') 

    plt.show() 

 

# Visualize the solution (path taken by agent after training) 

visualize_solution(0, 0) 
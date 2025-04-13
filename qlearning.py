import numpy as np
import random

# Simple 3x3 Grid World
class GridWorld:
    def __init__(self, size=3, start=(0, 0), goal=(2, 2)):
        self.size = size
        self.start = start
        self.goal = goal
        self.state = start

    def reset(self):
        self.state = self.start
        return self.state

    def step(self, action):
        row, col = self.state
        if action == 0: row = max(0, row - 1)      # UP
        if action == 1: col = min(self.size-1, col + 1)  # RIGHT
        if action == 2: row = min(self.size-1, row + 1)  # DOWN
        if action == 3: col = max(0, col - 1)      # LEFT
        self.state = (row, col)
        reward = 100 if self.state == self.goal else -1
        return self.state, reward

# Q-learning function
def train_q_learning(env, episodes=500, lr=0.1, gamma=0.9, epsilon=1.0):
    Q = np.zeros((env.size, env.size, 4))  # 4 actions per cell

    for _ in range(episodes):
        state = env.reset()
        while state != env.goal:
            if random.random() < epsilon:
                action = random.randint(0, 3)  # Explore
            else:
                action = np.argmax(Q[state])   # Exploit

            next_state, reward = env.step(action)
            Q[state][action] += lr * (reward + gamma * np.max(Q[next_state]) - Q[state][action])
            state = next_state

        epsilon = max(0.1, epsilon * 0.99)  # Epsilon decay

    return Q

# Run everything
env = GridWorld()
Q = train_q_learning(env)

# Show results
print("Final Q-Table:\n", Q)
print("Optimal Policy (0=UP, 1=RIGHT, 2=DOWN, 3=LEFT):\n", np.argmax(Q, axis=2))

# Test policy from start to goal
state = env.reset()
print("Path taken:")
while state != env.goal:
    action = np.argmax(Q[state])
    state, _ = env.step(action)
    print(state)

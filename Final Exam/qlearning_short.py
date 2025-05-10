# Q Learning 
import numpy as np, random

n = 3
Q = np.zeros((n, n, 4))  # Q-table: (row, col, action)
actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

def move(state, action):
    r, c = state
    dr, dc = actions[action]
    r, c = np.clip(r + dr, 0, n - 1), np.clip(c + dc, 0, n - 1)
    next_state = (r, c)
    reward = 99 if next_state == (n - 1, n - 1) else -1
    return next_state, reward

for episode in range(500):
    state = (0, 0)
    epsilon = max(0.1, 0.99 ** episode)
    while state != (n - 1, n - 1):
        if random.random() < epsilon:
            action = random.randint(0, 3)
        else:
            action = Q[state].argmax()
        next_state, reward = move(state, action)
        Q[state][action] += 0.1 * (reward + 0.9 * Q[next_state].max() - Q[state][action])
        state = next_state

print("Q-values:\n", np.round(Q, 1))
print("Policy:\n", Q.argmax(2))  # best action per state

# Print learned path
state = (0, 0); print("Path:")
while state != (n - 1, n - 1):
    print(state, end=" -> ")
    state, _ = move(state, Q[state].argmax())
print(state)

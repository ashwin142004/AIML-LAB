import numpy as np, random

class GridWorld:
    def __init__(s, n=3): s.n, s.start, s.goal, s.state = n, (0,0), (n-1,n-1), (0,0)
    def reset(s): s.state = s.start; return s.state
    def step(s,a):
        r,c = s.state
        moves = [(-1,0),(0,1),(1,0),(0,-1)]
        r,c = max(0,min(s.n-1,r+moves[a][0])), max(0,min(s.n-1,c+moves[a][1]))
        s.state = (r,c)
        return s.state, 100 if s.state==s.goal else -1

def train_q(env, ep=500, lr=0.1, gamma=0.9, eps=1.0):
    Q = np.zeros((env.n, env.n, 4))
    for _ in range(ep):
        s = env.reset()
        while s != env.goal:
            a = random.randint(0,3) if random.random()<eps else np.argmax(Q[s])
            ns, r = env.step(a)
            Q[s][a] += lr * (r + gamma*np.max(Q[ns]) - Q[s][a])
            s = ns
        eps = max(0.1, eps*0.99)
    return Q

env = GridWorld()
Q = train_q(env)

print("Final Q-Table:\n", Q)
print("Optimal Policy (0=UP,1=RIGHT,2=DOWN,3=LEFT):\n", np.argmax(Q,axis=2))

s = env.reset()
print("Path taken:")
while s != env.goal:
    a = np.argmax(Q[s])
    s,_ = env.step(a)
    print(s)

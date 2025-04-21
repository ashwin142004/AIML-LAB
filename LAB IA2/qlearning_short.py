import numpy as np,random

n=3
Q=np.zeros((n,n,4))
def step(s,a):
    d=[(-1,0),(0,1),(1,0),(0,-1)]
    s=tuple(np.clip(np.add(s,d[a]),0,n-1))
    return s,99*(s==(n-1,n-1))-1

for ep in range(500):
    s=(0,0);eps=max(.1,1*.99**ep)
    while s!=(n-1,n-1):
        a=random.randrange(4) if random.random()<eps else Q[s].argmax()
        ns,r=step(s,a)
        Q[s][a]+=0.1*(r+0.9*Q[ns].max()-Q[s][a])
        s=ns

print(Q)
print(Q.argmax(2))

s=(0,0)
while s!=(n-1,n-1):
    s,_=step(s,Q[s].argmax())
    print(s)

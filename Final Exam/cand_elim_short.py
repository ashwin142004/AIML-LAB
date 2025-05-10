#Candidate Elimination Algorithm
import numpy as np
import pandas as pd

data = pd.DataFrame({
    'sky': ['sunny', 'sunny', 'rainy', 'sunny'],
    'airtemp': ['warm', 'warm', 'cold', 'warm'],
    'humidity': ['normal', 'high', 'high', 'high'],
    'wind': ['strong'] * 4,
    'water': ['warm', 'warm', 'warm', 'cool'],
    'forecast': ['same', 'same', 'change', 'change'],
    'enjoysport': ['yes', 'yes', 'no', 'yes']
})

concepts = data.iloc[:, :-1].values
target = data.iloc[:, -1].values

def candidate_elimination(concepts, target):
    S = concepts[0].copy()
    G = [['?'] * len(S) for _ in S]
    
    for i, row in enumerate(concepts):
        if target[i] == 'yes':
            S = ['?' if S[j] != row[j] else S[j] for j in range(len(S))]
        else:
            for j in range(len(S)):
                if row[j] != S[j]:
                    G[j][j] = S[j]
                else:
                    G[j][j] = '?'
    
    G = [g for g in G if g != ['?'] * len(S)]
    return S, G

S, G = candidate_elimination(concepts, target)
print("Final Specific Hypothesis:\n", S)
print("Final General Hypothesis:\n", G)

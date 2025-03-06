import numpy as np
import pandas as pd

#data = pd.read_csv('trainingexample.csv')
data = pd.DataFrame({
    'sky': ['sunny', 'sunny', 'rainy', 'sunny'],
    'airtemp': ['warm', 'warm', 'cold', 'warm'],
    'humidity': ['normal', 'high', 'high', 'high'],
    'wind': ['strong', 'strong', 'strong', 'strong'],
    'water': ['warm', 'warm', 'warm', 'cool'],
    'forecast': ['same', 'same', 'change', 'change'],
    'enjoysport': ['yes', 'yes', 'no', 'yes']
})

concepts = np.array(data.iloc[:, :-1])
target = np.array(data.iloc[:, -1])

def learn(concepts, target):
    specific_h = concepts[0].copy()
    general_h = [['?'] * len(specific_h) for _ in range(len(specific_h))]
    
    for i, h in enumerate(concepts):
        if target[i] == "yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        else:
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
    
    general_h = [h for h in general_h if h != ['?'] * len(specific_h)]
    return specific_h, general_h

s_final, g_final = learn(concepts, target)
print("Final Specific Hypothesis:", s_final, sep="\n")
print("Final General Hypothesis:", g_final, sep="\n")

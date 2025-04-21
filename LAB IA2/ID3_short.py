import pandas as pd, numpy as np
from pprint import pprint

eps = np.finfo(float).eps

def entropy(df): 
    p = df.iloc[:,-1].value_counts()/len(df)
    return -np.sum(p*np.log2(p+eps))

def best_attr(df):
    ent=entropy(df)
    return max(df.columns[:-1], key=lambda a: ent - sum((df[a]==v).mean()*entropy(df[df[a]==v]) for v in df[a].unique()))

def build(df):
    if len(df.iloc[:,-1].unique())==1: return df.iloc[0,-1]
    attr=best_attr(df)
    return {attr:{v:build(df[df[attr]==v].drop(columns=[attr])) for v in df[attr].unique()}}

def predict(tree, sample):
    if not isinstance(tree,dict): return tree
    attr=list(tree.keys())[0]
    return predict(tree[attr].get(sample[attr], None), sample)

df = pd.read_csv("D:\\AIML-LAB\\PlayTennis.csv")
print("Dataset:\n",df)

tree = build(df)
print("\nDecision Tree:\n")
pprint(tree)

sample = {'Outlook':'Rainy','Temperature':'Mild','Humidity':'Normal','Wind':'Strong'}
print("\nPrediction:",predict(tree,sample))

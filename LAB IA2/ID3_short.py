import pandas as pd
import numpy as np
from pprint import pprint

eps = np.finfo(float).eps

def entropy(df):
    class_counts = df.iloc[:, -1].value_counts()
    probabilities = class_counts / len(df)
    return -np.sum(probabilities * np.log2(probabilities + eps))

def entropy_attribute(df, attribute):
    values, counts = np.unique(df[attribute], return_counts=True)
    entropy_sum = sum((counts[i]/len(df)) * entropy(df[df[attribute] == v]) for i, v in enumerate(values))
    return entropy_sum

def find_best_attribute(df):
    return max(df.columns[:-1], key=lambda attr: entropy(df) - entropy_attribute(df, attr))

def build_tree(df):
    if len(df.iloc[:, -1].unique()) == 1:
        return df.iloc[0, -1]
    
    best_attr = find_best_attribute(df)
    tree = {best_attr: {}}
    
    for value in df[best_attr].unique():
        subtree = build_tree(df[df[best_attr] == value].drop(columns=[best_attr]))
        tree[best_attr][value] = subtree
    
    return tree

def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    
    attribute = next(iter(tree))
    return predict(tree[attribute].get(sample[attribute], None), sample)

# Load dataset
df = pd.read_csv("id3.csv")
print("Given Dataset: \n", df)

decision_tree = build_tree(df)
print("\nDecision Tree: \n")
pprint(decision_tree)

# Test prediction
test_sample = {'Outlook': 'Rainy', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong'}
print("\nPrediction: ", predict(decision_tree, test_sample))

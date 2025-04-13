import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

# Step 1: Load dataset
df = pd.read_csv("heart.csv")

# Step 2: Convert target to binary (1 = disease, 0 = no disease)
df["target"] = df["target"].apply(lambda x: 1 if x > 0 else 0)

# Step 3: Select important features
df = df[["age", "sex", "cp", "chol", "thalach", "target"]]

# Step 4: Discretize continuous features into categories
df['age'] = pd.cut(df['age'], [28, 40, 55, 77], labels=[0, 1, 2]).astype(int)
df['chol'] = pd.cut(df['chol'], [120, 200, 300, 600], labels=[0, 1, 2]).astype(int)
df['thalach'] = pd.cut(df['thalach'], [70, 120, 160, 210], labels=[0, 1, 2]).astype(int)

# Step 5: Define network structure
model = BayesianNetwork([
    ('age', 'target'),
    ('sex', 'target'),
    ('cp', 'target'),
    ('chol', 'target'),
    ('thalach', 'target')
])

# Step 6: Learn CPDs (Conditional Probability Distributions)
model.fit(df, estimator=MaximumLikelihoodEstimator)

# Step 7: Perform inference
inference = VariableElimination(model)

# Step 8: Query probability of heart disease for given conditions
result = inference.query(variables=['target'], evidence={
    'age': 1,        # Middle age
    'sex': 1,        # Male
    'cp': 3,         # Chest pain type 3
    'chol': 1,       # Moderate cholesterol
    'thalach': 2     # High max heart rate
})

# Output result
print("\nProbability of Heart Disease:")
print(result)

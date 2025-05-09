import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork as BN
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

# Load and preprocess
df = pd.read_csv("D:\\AIML-LAB\\heart.csv")

df["target"] = (df["target"] > 0).astype(int)
df = df[["age", "sex", "cp", "chol", "thalach", "target"]]
df['age'] = pd.cut(df['age'], [28,40,55,77], labels=[0,1,2]).astype(int)
df['chol'] = pd.cut(df['chol'], [120,200,300,600], labels=[0,1,2]).astype(int)
df['thalach'] = pd.cut(df['thalach'], [70,120,160,210], labels=[0,1,2]).astype(int)

# Build and train model
model = BN([('age','target'),('sex','target'),('cp','target'),('chol','target'),('thalach','target')])
model.fit(df, estimator=MaximumLikelihoodEstimator)

# Inference
infer = VariableElimination(model)
res = infer.query(variables=['target'], evidence={'age':1,'sex':1,'cp':3,'chol':1,'thalach':2})

# Output
print("\nProbability of Heart Disease:\n", res)

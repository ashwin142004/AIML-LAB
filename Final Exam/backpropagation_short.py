#Backpropagation 
import numpy as np

# Input and normalization
X = np.array([[2,9],[1,5],[3,6]], dtype=float)
y = np.array([[92],[86],[89]], dtype=float) / 100
X /= X.max(axis=0)

# Activation functions
sigmoid = lambda x: 1/(1+np.exp(-x))
dsigmoid = lambda x: x*(1-x)

# Initialize variables
epoch, lr = 5000, 0.1
wh, bh = np.random.rand(2,3), np.random.rand(1,3)
wout, bout = np.random.rand(3,1), np.random.rand(1,1)

# Training loop
for _ in range(epoch):
    hlayer = sigmoid(np.dot(X, wh) + bh)
    output = sigmoid(np.dot(hlayer, wout) + bout)

    d_output = (y - output) * dsigmoid(output)
    d_hidden = d_output.dot(wout.T) * dsigmoid(hlayer)

    wout += hlayer.T.dot(d_output) * lr
    wh += X.T.dot(d_hidden) * lr

# Results
print("Input:\n", X)
print("Actual Output:\n", y)
print("Predicted Output:\n", output)

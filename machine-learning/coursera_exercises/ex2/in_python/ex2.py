from exercises.plotData import plot
from exercises.costFunction import getCost
import pandas as pd
import numpy as np

inp = pd.read_csv('../ex2data1.txt', header=None)

X = inp[inp.columns[0:2]].values
# Giving directly the index of column for dataframe
y_df = inp[2].values
# Number of training samples
m = len(y_df)
# Reshaping from (100,) to (100,1)
y = y_df.reshape((m, 1))

plot(X, y)

(m, n) = X.shape

# the intercept vector
column_ones = np.ones((m, 1))
# Adding the intercept one's for theta0
X = np.concatenate((column_ones, X), axis=1)


initial_theta = np.zeros((n+1, 1))
(cost_J, gradient) = getCost(X, y, initial_theta)

print('Cost at initial theta (zeros):\n', cost_J)
print('Expected cost (approx): 0.693\n')
print('Gradient at initial theta (zeros): \n')
print(gradient)
print('Expected gradients (approx):\n -0.1000\n -12.0092\n -11.2628\n')
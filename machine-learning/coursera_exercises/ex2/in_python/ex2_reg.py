# On Regularization
import pandas as pd
import numpy as np
from exercises.plotData import plot
from exercises.mapFeature import featureMap
from exercises.costFunctionReg import getCost

inp = pd.read_csv('../ex2data2.txt', header=None)

X_org = inp[inp.columns[0:2]].values
y_df = inp[2].values

m = len(y_df)

y = y_df.reshape((m, 1))

plt = plot(X_org, y)
# Labelling the markers
plt.legend(['y=1', 'y=0'])
# Labelling Axes
plt.xlabel('Microchip Test 1')
plt.ylabel('Microchip Test 2')
plt.show()

# Generating new features which are polynomial to try to fit the data points
X = featureMap(X_org)
X_shape = X.shape
print('New features vector shape', X_shape)

initial_theta = np.zeros((X_shape[1], 1))
# Setting= regularization parameter lambda to 1
lambd = 1
cost, grad = getCost(X, y, initial_theta, lambd)

print('Cost at initial theta (zeros): %f\n', cost)
print('Expected cost (approx): 0.693\n')
print('Gradient at initial theta (zeros) - first five values only:\n')
print('\n', grad[0:5])
print('Expected gradients (approx) - first five values only:\n')
print(' 0.0085\n 0.0188\n 0.0001\n 0.0503\n 0.0115\n')
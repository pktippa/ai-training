from exercises.plotData import plot
import pandas as pd

inp = pd.read_csv('../ex2data1.txt', header=None)

X = inp[inp.columns[0:2]].values
# Giving directly the index of column for dataframe
y_df = inp[2].values
# Number of training samples
m = len(y_df)
# Reshaping from (100,) to (100,1)
y = y_df.reshape((m, 1))

plot(X, y)
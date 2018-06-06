import matplotlib.pyplot as plt

def plot(X, y):
    plt.scatter(X,y,c='r',marker='x')
    plt.xlabel('Profit in $10,000s')
    plt.ylabel('Population of City in 10,000s')
    plt.show()
import numpy as np
from .sigmoid import sigm

def getCost(X, y, theta, lambd):
    # Calculating matrix multiplication of X and theta
    X_x_theta = np.matmul(X, theta)
    # Getting the sigmoid values for calculating hypothesis function
    h_theta = sigm(X_x_theta)
    # Caluclating transpose of X which is used for calculating gradient
    X_trans = np.transpose(X)

    # Performing logarthmic operation on each element of matrix
    log_h_theta = np.log(h_theta)
    log_1_h_theta = np.log(1-h_theta)
    
    log_h_tht_trans = np.transpose(log_h_theta)
    log_1_h_tht_trans = np.transpose(log_1_h_theta)

    m = len(y)
    # Calculating Cost
    cost_J = (-1/m) * (np.matmul(log_h_tht_trans, y) + np.matmul(log_1_h_tht_trans, (1 - y)))

    # extra cost for regularization
    cost_reg = ( lambd / m ) * ( np.sum(theta ** 2) - np.asscalar(theta[0] ** 2) )

    # Combining both cost and regularization term
    total_cost = cost_J + cost_reg

    # Calculating Gradient.
    grad = (1/m) * (np.matmul(X_trans, (h_theta - y)))

    # grad for regularization term
    funny_mat = np.eye(len(theta))
    funny_mat[0][0] = 0
    print('funny mat shape', funny_mat.shape)
    grad_reg = (lambd / m) * (funny_mat.dot(theta))

    # Combining gradients
    grad_total = grad + grad_reg
    
    return total_cost, grad_total
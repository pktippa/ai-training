import numpy as np
from .sigmoid import sigm

def getCost(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lambd):
    # Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
    Theta1 = nn_params[0:( ( input_layer_size + 1 ) * hidden_layer_size),]
    Theta1 = Theta1.reshape((hidden_layer_size, input_layer_size + 1))
    Theta2 = nn_params[( ( input_layer_size + 1 ) * hidden_layer_size):,]
    Theta2 = Theta2.reshape((num_labels, hidden_layer_size + 1))

    print('Theta1[24][356]',  Theta1[24][356])
    print('Theta2[7][23]', Theta2[7][23])
    # input_layer_size 400
    # hidden_layer_size 25
    # num_labels 10
    # Theta1.shape (25, 401)
    # Theta2.shape (10, 26)
    # X.shape (5000, 400)
    # y (5000, 1)

    #print('theta1' , Theta1)
    #print('theta2', Theta2)

    m, n = X.shape # n is similar to input_layer_size
    # First Layer
    ones = np.ones((m ,1))
    a1 = np.concatenate((ones, X), axis=1) # (5000, 401)

    z1 = a1.dot(Theta1.T) # (5000, 401) X (401, 25) = (5000, 25)
    h1 = sigm(z1) # (5000, 25)

    # Second Layer
    a2 = np.concatenate((ones, h1), axis=1) # (5000, 26)
    z2 = a2.dot(Theta2.T) # (5000, 26) X (26, 10) = (5000, 10)
    h2 = sigm(z2) # (5000, 10)

    log_h2  = np.log(h2) # (5000, 10)
    log_1_h2 = np.log(1 - h2) # (5000, 10)
    
    # Setting initial cost to 0
    J = 0 

    #print(log_h2[1,:])
    # Zeros column vector
    term_z = np.zeros((num_labels + 1, 1)) # (10, 1)
    
    for i in range(m):
        val = np.asscalar(y[i]) # value ranging from 1 to 10
        #print(' Value returned ', val)
        term_z[int(val)] = 1 # Setting the particular index to 1, rest all zeros
        lh2 = log_h2[i, :].reshape(1, num_labels) # (1, 10)
        l_1_h2 = log_1_h2[i, :].reshape(1, num_labels)
        cst = lh2.dot(term_z[1:,]) + l_1_h2.dot(1 - term_z[1:,])

        J += (-1/m) * np.asscalar(cst)
        if(i < 10): print('J', J)
    
    return J

def getGrad():
    pass
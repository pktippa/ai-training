def getCost(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lambd):
    # Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
    Theta1 = nn_params[0:( ( input_layer_size + 1 ) * hidden_layer_size),]
    Theta1 = Theta1.reshape((hidden_layer_size, input_layer_size + 1))
    Theta2 = nn_params[( ( input_layer_size + 1 ) * hidden_layer_size):,]
    Theta2 = Theta2.reshape((num_labels, hidden_layer_size + 1))

    print('theta1' , Theta1)
    print('theta2', Theta2)
    return 1
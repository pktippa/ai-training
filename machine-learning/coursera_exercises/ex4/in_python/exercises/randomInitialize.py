import numpy as np

def rand(m, n):
    
    epsolon = 0.12

    return ( ( np.random.rand(m,n) * 2 * epsolon ) - epsolon )
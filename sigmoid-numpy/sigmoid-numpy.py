import numpy as np

def sigmoid(x):
    a=np.array(x)
    y=np.array(1/(1+np.exp(-a)))
    pass
    return y
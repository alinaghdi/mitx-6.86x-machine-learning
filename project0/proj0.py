# Sec 1
# Randomization
# Write a function called randomization that takes as input a positive integer n, and returns A, a random n x 1 Numpy array.

def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    #Your code here
    A = np.random.rand(n,1)
    #raise NotImplementedError
    return A

# Sec 2
# Operations
#Write a function called operations that takes as input two positive integers h and w, makes two random matrices A and B, of size h x w, and returns A,B, and s, the sum of A and B.

def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    #Your code here
    A = np.random.random(size=(h,w))
    B = np.random.random(size=(h,w))
    s = A + B
    #raise NotImplementedError
    return A, B, s

# Sec 3
# Norm
# Write a function called norm that takes as input two Numpy column arrays A and B, adds them, and returns s, the L2 norm of their sum.

def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    #Your code here
    #raise NotImplementedError
    s = np.linalg.norm(A + B)
    return s

# Sec 4
# Neural Network
# Here, we will write a function neural_network, which will apply a neural network operation with 2 inputs and 1 output and a given weight matrix.

def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    #Your code here
    #raise NotImplementedError
    return np.tanh(weights.T.dot( inputs))

# Sec 5
# Scalar function
# Let's start with writing a scalar function scalar_function, which will apply the following operation with input x and y.

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    #Your code here
    #raise NotImplementedError
    if x <= y:
        return x *y
    else:
        return x / y

# Sec 6
# Debugging exercise
'''
The function get_sum_metrics takes two arguments: a prediction and a list of metrics to apply to the prediction 
(say, for instance, the accuracy or the precision). Note that each metric is a function, not a number. 
The function should compute each of the metrics for the prediction and sum them. It should also add 
to this sum three default metrics, in this case, adding 0, 1 or 2 to the prediction.
'''

def get_sum_metrics(predictions, metrics=None):
    if metrics is None:
        metrics = []

    for i in range(3):
        metrics.append(lambda x, i=i: x + i)

    sum_metrics = 0
    for metric in metrics:
        sum_metrics += metric(predictions)

    return sum_metrics

# Sec 7









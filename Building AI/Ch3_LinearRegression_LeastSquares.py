"""
Linear Regression. 

1. Finding the Optimum of different fixed sets of coefficients
by using the least squares method. 

2. Data input of features and target label (price). Using least suqares method 
to find the best coefficients to predict the price.
"""

# 1. Finding the optimum of different fixed sets of coefficients
# by using the least squares method. 
import numpy as np

print("1. Part")
print("------------------------------------------------------------")
# data
# feature columns 
features = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])

# target label (price)
ylabel = np.array([250000, 60000, 525000])

# coefficient sets
coeff = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    """
    Parameters
    ----------
    X : Input values for three mökkis: size, size of sauna, distance to water,
        number of indoor bathrooms, proximity of neighbors
    y : train data/real price of the mökki
    c : Coefficients to calculate the price of each feature value

    Returns
    -------
    Index of best set of coefficients.
    """
    smallest_error = np.Inf 
    best_index = -1
    i = 0
    for coeff in c: # for each set of coefficients
        error = sum((y - X@coeff)**2) # sum of squared errors
        if error < smallest_error:
            smallest_error = error 
            best_index = i  
        i += 1
        
    print("the best set is set %d" % best_index)
    
    return 

find_best(features, ylabel, coeff) # finding best set of fixed coefficients

print("------------------------------------------------------------")

# 2. Data input of features and target label (price). Using least suqares method 
# to find the best coefficients to predict the price.

from io import StringIO

print("------------------------------------------------------------")
print("2. Part")
print("------------------------------------------------------------")

# input data, features and target label
train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

np.set_printoptions(precision=1) # this just changes the output settings for easier reading
 
def fit_model(input_file):
    """
    This function reads in an input file and calculates the best coefficients
    by using the least squares method.
    """
    # read the data in and fit it. the values below are placeholder values
    data = np.genfromtxt(input_file, skip_header=1)
    X = data[:,:5] # feature columns 
    y = data[:,5] # target label column (price)
    c = np.linalg.lstsq(X, y, rcond=None)[0] # least squares method

    print("fitted coefficients:\n", c)
    print("predicted prices using train data:\n", X @ c)
    print("prices of train data:\n", y)
    return c

# train the model
input_file_train = StringIO(train_string)
c_fit = fit_model(input_file_train)

# test the model
def test_model(input_file, c):
    """
    This function predicts the price using input data (test data).
    
    Parameters
    ----------
    input_file : test data
    c : fitted coefficients

    Returns
    -------
    None.
    """
    data = np.genfromtxt(input_file, skip_header=1)
    X = data[:,:5]
    y = data[:,5]
    
    print("predicted prices using test data:\n", X@c)
    print("prices of test data\n", y)
    
    return

# test the model
input_file_test = StringIO(test_string)    
test_model(input_file_test, c_fit)

print("------------------------------------------------------------")


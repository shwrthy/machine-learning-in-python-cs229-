import pandas as pd
import numpy as np
from scipy.optimize import minimize

def sigmoid (x):
    z = 1 / (1 + np.exp(-x))
    return z

def costFunction(initial_theta, X, y):
    m = np.size(y, 0)
    J = (-np.dot(np.log(sigmoid(np.dot(X, initial_theta))), y)\
        -np.dot(np.log(1 - sigmoid(np.dot(X, initial_theta))),1 - y)) / m
    return J
 
 
def gradient(initial_theta, X, y):
    m, n = X.shape
    y = y.reshape((1, m))
    grad = np.dot(sigmoid(np.dot(X, initial_theta))-y, X) / m
    return grad

def optimize (initial_theta, X, y):
    result = minimize(fun = costFunction, x0 = initial_theta, \
                      args = (X, y) ,method = 'TNC', jac = gradient)
    return result

def costFunction_Reg (theta, X, y, Lambda):
    m, n = X.shape
    J = (-np.dot(np.log(sigmoid(np.dot(X, theta))), y) -np.dot(np.log(1 - \
         sigmoid(np.dot(X, theta))),1 - y)) / m + Lambda / m / 2 * \
         np.power(np.multiply(theta, np.insert(np.ones((n-1)), 0, 0.)), 2).sum()
    return J

def gradient_Reg (theta, X, y, Lambda):
    m, n = X.shape
    y = y.reshape((1, m))
    grad = np.dot(sigmoid(np.dot(X, theta))-y, X) / m + \
    Lambda / m * np.multiply(theta, np.insert(np.ones((n-1)), 0, 0.))
    return grad

def optimize_Reg (initial_theta, X, y, Lambda):
    result = minimize (fun = costFunction_Reg, x0 = initial_theta, \
                       args = (X, y, Lambda), method = 'TNC', jac = gradient_Reg)
    return result
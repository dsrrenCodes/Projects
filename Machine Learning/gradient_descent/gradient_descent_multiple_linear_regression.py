import numpy as np

#Gradient Descent on multiple linear regression

def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0
    for i in range(m):
        fwb = np.dot(w, x[i]) + b
        cost += (fwb - y[i]) ** 2
    total_cost = (1 / (2 * m)) * cost
    return total_cost

def compute_gradient(x, y, w, b):
    m, n = x.shape  # (number of examples, number of features)
    #djdw into [0,0,0,0] each representing feaure j 
    djdw = np.zeros(n)
    djdb = 0.

    for i in range(m):
        error = ((np.dot(x[i], w) + b) - y[i])
        for j in range(n):
            djdw[j] = djdw[j] + error * x[i, j]
        djdb += error
    djdw = djdw / m
    djdb = djdb / m

    return djdb, djdw

def gradient_descent(x, y, w, b, alpha):
    for _ in range(1000):
        djdb, djdw = compute_gradient(x, y, w, b)
        w = w - alpha * djdw
        b = b - alpha * djdb
    
    cost = compute_cost(x, y, w, b)
    print(f'Cost Function: {cost}, w: {w}, b: {b}')

x = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y = np.array([460, 232, 178])
w = np.zeros(4)

#set b and w to 0
gradient_descent(x, y, w, 0, 5.0e-7)  # Initial b set to 0, alpha set to 0.001


#Logistic Regression With L2 regularization

import numpy as np

def sigmoid(z):
    """
    Compute the sigmoid of z

    Args:
        z (ndarray): A scalar, numpy array of any size.

    Returns:
        g (ndarray): sigmoid(z), with the same shape as z
         
    """
          
    g=1/(1+np.exp(-z))
    
    return g

def compute_cost(x,y,w,b,lamdba_=1):
    m,n=x.shape

    cost=0
    for i in range(m):
        function=np.dot(w,x[i])+b
        fwb=sigmoid(function)
        cost+=(y[i]*np.log(fwb)+(1-y[i])*np.log(1-fwb))
    cost=cost*(-1/m)

    reg_cost=0
    for j in range(n):
        reg_cost+=w[j]**2
    reg_cost=reg_cost*(lamdba_/(2*m))

    total_cost=reg_cost+cost
    return total_cost

def compute_gradient(x,y,w,b,lambda_=1):
    m,n=x.shape
    djdw=np.zeros(n)
    djdb=0
    
    for i in range(m):
        function=np.dot(w,x[i])+b
        fwb=sigmoid(function)
        cal=fwb-y[i]
        for j in range(n):
            djdw[j]+=(cal)*x[i,j]
        djdb+=cal
        for j in range(n):
            djdw[j]+=((lambda_/m)*w[j])
    djdw=djdw/m
    djdb=djdb/m
    return djdw,djdb

def gradient_descent(x, y, w, b, alpha, num_iters, lambda_):
    
    for i in range(num_iters):
        djdw,djdb=compute_gradient(x,y,w,b,lambda_)
        w=w-alpha*(djdw)
        b=b-alpha*(djdb)
        cost=compute_cost(x,y,w,b,lambda_)
        print(f"Iteration: {i}, cost_function: {cost}")
    cost=compute_cost(x,y,w,b,lambda_)
    
    return f"final w: {w}, final b: {b}, final cost value {cost}"


np.random.seed(1)
X_tmp = np.random.rand(5,3)
y_tmp = np.array([0,1,0,1,0])
w_tmp = np.random.rand(X_tmp.shape[1])
b_tmp = 0.5
lambda_tmp = 0.7
gradient_descent(X_tmp, y_tmp, w_tmp, b_tmp, alpha=0.01,num_iters=1000,lambda_=1)




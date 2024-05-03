import numpy as np

# Gradient Descent On univariate Linear Regression 

def cost_function(x,y,w,b):
    m=x.shape[0]
    cost=0
    for i in range(m):
        cost+=((w*x[i]+b)-y[i])**2
        
    total_cost= (1/(2*m))*cost

    return total_cost

def compute_gradient(x,y,w,b):
    m=x.shape[0]
    dw=0
    db=0
    
    for i in range(m):
        dw+=((w*x[i]+b)-y[i])*x[i]
        db+=((w*x[i]+b)-y[i])
    djdw=(1/m)*dw
    djdb=(1/m)*db
    
    return djdw, djdb

def gradient_descent(x,y,w,b,alpha):
    for _ in range(1000):
        djdw, djdb= compute_gradient(x,y,w,b)
        w=w-alpha*djdw
        b=b-alpha*djdb
    
    costfunction=cost_function(x,y,w,b)
    print(f"cost function: {costfunction},b : {b},w : {w}")




x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])
gradient_descent(x,y,0,0,0.1)

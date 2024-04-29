import numpy as np

# Gradient Descent On Linear Regression

def gradient_descent(x,y):
    m_curr=0
    b_curr=0
    iterations=1000
    n= len(x)
    #Any learning Rate
    learning_rate=0.01
    for i in range(iterations):
        #y          =  m     * x + c
        y_predicted = m_curr * x + b_curr
        
        #cost function (mse)
        cost= (1/n)*sum([val**2 for val in (y-y_predicted)])

        #Deratives Forms
        m_d=-(2/n) * sum(x*(y-y_predicted))
        b_d=-(2/n) * sum((y-y_predicted))

        #Adjusting Parameters 
        m_curr=m_curr-learning_rate*m_d

        b_curr=b_curr-learning_rate *b_d

        print(f"m_curr: {m_curr},b_curr: {b_curr}, cost:{cost}")

x=np.array([1,2,3,4,5])
y=x=np.array([5,7,9,11,13])
gradient_descent(x,y)
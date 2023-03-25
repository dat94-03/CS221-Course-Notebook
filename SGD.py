# Reflex-based model:Machine Learning 24/03/2023
import numpy as np

# generate artificial data

true_w = np.array([1,2,3,4,5])
dimemsion = len(true_w)
points = []

for i in range(100):
    x = np.random.randn(dimemsion)
    y = true_w.dot(x) + np.random.randn()
    points.append((x,y))
    print("data : [{}] - {}".format(i,points[i]))

def F(w):
    sum = 0
    for x,y in points:
        return sum((w.dot(x) - y)**2 for x,y in points)/len(points)
def dF(w):
    return sum(2*(w.dot(x) - y)*x for x,y in points)/len(points)
def sF(w,i):
    x,y = points[i]
    return (w.dot(x) - y)**2

def sdF(w,i):
    x,y = points[i]
    return (w.dot(x)-y)*2*x
    

# algorithms

def gradientDecent():
    w = np.zeros(dimemsion)
    eta = 0.02 #step
    for i in range(15000):
        score = F(w)
        gradient = dF(w)
        w = w - eta*gradient
        print("Iteration: {} W = {} score = {}".format(i,w,score))
def stochasticGradientDecent(len):
    w = np.zeros(dimemsion)
    eta = 1
    numIteration = 1
    for j in range(1000):
        for i in range(len):
            score = sF(w,i)
            
            eta = 1.0/numIteration
            gradient = sdF(w,i)
            w = w - eta*gradient
        numIteration = numIteration +1
        print("Iteration : [{}] W = {} Score = {}".format(numIteration,w,score))


#gradientDecent()
stochasticGradientDecent(len(points))
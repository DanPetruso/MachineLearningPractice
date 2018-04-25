import numpy as np
import matplotlib.pyplot as plt

#loading data
X = []
Y = []
for line in open('data_1d.csv'):
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))
    
#numpy arrays
X = np.array(X)
Y = np.array(Y)

#plot to see
plt.scatter(X, Y)
plt.show()

#calculate a and b
denom = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean() * X.sum()) / denom
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) /denom

#calc predicted line
Yhat = a * X + b

#plot again
plt.scatter(X,Y)
plt.plot(X,Yhat)
plt.show()

#calc r^2
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print('r-squared:',r2)
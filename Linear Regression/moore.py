import re
import numpy as np
import matplotlib as plt

X = []
Y = []

non_decimal = re.compile(r'[^\d]+')

for line in open('moore.csv'):
    r = line.split(',')
    
    x = int(non_decimal.sub('', r[2].split('[')[0]))
    y = int(non_decimal.sub('', r[1].split('[')[0]))
    X.append(x)
    Y.append(y)
    
X = np.array(X)
Y = np.array(Y)

plt.scatter(X, Y)
plt.show()

Y = np.log(Y)
plt.scatter(X,Y)
plt.show()

denom = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean() * X.sum()) / denom
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) /denom

Yhat = a*X + b

plt.scatter(X,Y)
plt.plot(X, Yhat)
plt.show()

d1 = Y - Yhat
d2 = Y - Yhat
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print('a:',a,'b:',b)
print('r-squared:',r2)

print('time to double:', np.log(2)/a, 'years')
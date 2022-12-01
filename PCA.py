import numpy as np
import pandas as pd
from math import sqrt

df = pd.read_csv(r"dataset2.csv")
df = df[['English','Hindi','Maths','Science']]
dataset = df.astype(float).values.tolist()
X = np.float64(df.values)
print(type(X))

print(X.shape)

for j in range(X.shape[1]) :

    s = 0.0

    for i in range(X.shape[0]) : 
        s += X[i][j]

    print('s = ',s)
    for i in range(X.shape[0]) : 
        print(X[i][j] - (s/X.shape[0]))
        val = X[i][j] - (s/X.shape[0])
        X[i][j] = val
        print('s/X.shape[0] = ',s/X.shape[0])
        print('s/X.shape[0] = ',s/X.shape[0])
        print(X[i][j])
    

transpose = np.transpose(X)

multi = np.matmul(transpose,X)/(X.shape[0])



print(X)

print(transpose)

print(multi)

w, v = np.linalg.eig(multi)


w1 = list(w) 
w1.sort(reverse=True) 

print(w)
print(w1)

final = []

for i in w1 : 
    for j in range(len(w)) : 
        if(i == w[j]) : 
            if j == 0 :
                final.append("English")
            if j == 1 :
                final.append("Hindi")
            if j == 2 :
                final.append("Maths")
            if j == 3 :
                final.append("Science")
            break
    if(len(final)) >= 2: 
        break

print(final)

import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from math import sqrt

def dist(a, b) : 
    x1 = a[0] 
    y1 = a[1] 
    x2 = b[0]
    y2 = b[1] 

    return sqrt(pow(x1-x2,2) + pow(y1-y2,2))

df = pd.read_csv(r"dataset.csv")
df = df[['A', 'B']]
dataset = df.astype(float).values.tolist()
X = df.values #returns a numpy array

# print(X)

# print(shuffle(X))

X = shuffle(X)

k = 3 

X = list(X)

centroids = [list(X[0]),list(X[1]),list(X[2])]

clusters = [[],[],[]]

for i in range(len(X)) : 
    mini = 1e9 
    ind = -1 

    for j in range(len(centroids)) : 
        if(dist(centroids[j],X[i]) < mini) : 
            mini =  dist(centroids[j],X[i])
            ind = j
    
    clusters[ind].append(list(X[i]))
    
    # print("ind = ",ind)
    # cluasters = np.append(clusters[ind], X[i])
    # print("clusters = ",clusters)
    # clusters[ind].append(X[i])

# print(clusters)
# print(centroids)


for i in range(k) : 
    l = len(clusters[i])
    x = np.float64(0)
    y = np.float64(0) 

    for j in range(len(clusters[i])) : 
        x = x + clusters[i][j][0]
        y = y + clusters[i][j][1]
    
    # print((centroids))
    # print(type(centroids))
    # print(type(centroids[i][0]))
    # print(type(x))
    centroids[i][0] = x/l
    centroids[i][1] = y/l
    
#     # centroids[i][0] = xen 
#     # centroids[i][1] = yen

# print(centroids)
# for cluster in clusters : 
#     print("cluster = ",cluster)

iterations = 500 

while iterations : 
    # print(centroids)
    iterations -= 1
    tempCentroid = centroids
    clusters = [[],[],[]]

    for i in range(len(X)) : 
        mini = 1e9 
        ind = -1 

        for j in range(len(centroids)) : 
            if(dist(centroids[j],X[i]) < mini) : 
                mini =  dist(centroids[j],X[i])
                ind = j
        clusters[ind].append(list(X[i]))
    
    for i in range(k) : 
        l = len(clusters[i])
        x = 0
        y = 0 

        if(len(clusters[i]) == 0) :
            exit()

        for j in range(len(clusters[i])) : 
            x = x + clusters[i][j][0]
            y = y + clusters[i][j][1]
        
        centroids[i][0] = x/l
        centroids[i][1] = y/l
    
    if((centroids == tempCentroid)) : 
        print("Final centroid = ",centroids)
      
        break
print("Final clusters : ")
for cluster in clusters : 
    print(cluster)


# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 00:21:38 2019

@author: samue
"""
import math


#I'm sorry that the file reading and result isn't well formatted. 
#I didn't have much time so had to enter
#in some of the variables myself and change the answer to fit rosalind

k = 7
m = 5

#f = open("rosalind_ba8c.txt", "r") #real deal
#x = 0
#data = []
#for line in f:
#    data.append([float(i) for i in line.split()])
#    x += 1
#f.close()

#print(data)
data = [[1.3, 1.1], [1.3, 0.2], [0.6, 2.8], [3.0, 3.2], [1.2, 0.7], [1.4, 1.6], [1.2, 1.0], [1.2, 1.1], [0.6, 1.5], [1.8, 2.6], [1.2, 1.3], [1.2, 1.0], [0.0, 1.9]]

def CenterOfGravity(data):
    result = []
    
    for x in range(len(data[0])):
        d = 0
        for datapoint in data:  
            d += datapoint[x]
        result.append(d/len(data))
        
    return result

def distance(datapoint, center):
    d = 0
    for x in range(m):
        d += (datapoint[x] - center[x])**2
        
    return math.sqrt(d)

#print(distance([1, 2, 1], [3, 1, 2]))

def CentersToClusters(centers, data):
    clusters = []
    for x in range(k):
        clusters.append([])
    
    for datapoint in data:
        mincenter = MinCenter(datapoint, centers)
        i = centers.index(mincenter)
        clusters[i].append(datapoint)
    
    return clusters

def MinCenter(datapoint, centers):
    mindistance = 100000
    for center in centers:
        if distance(datapoint, center) < mindistance:
            mindistance = distance(datapoint, center)
            mincenter = center
    return mincenter

def ClustersToCenters(clusters):
    centers = []
    for cluster in clusters:
        cog = CenterOfGravity(cluster)
        centers.append(cog)
    return centers

def kmeans(data, k, m):
    prevcenters = []
    currcenters = data[0:k]
    while (prevcenters != currcenters):
        prevcenters = currcenters
        clusters = CentersToClusters(currcenters, data)
        currcenters = ClustersToCenters(clusters)
    return currcenters

data = [[1,1],[1.5,2],[3,4],[5,7],[3.5,5],[4.5,5],[3.5,4.5]]
k = 2
result = kmeans(data, k, 6)

for i, ls in enumerate(result):
    for j, num in enumerate(ls):
        result[i][j] = round(result[i][j], 3)
        
print(result)
        

        
        
        
        

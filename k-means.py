import numpy as np

x = np.array([1,2,3,8,9,10,50,55,60])
y = np.array([1,2,3,8,9,10,50,55,60])

data_points = np.column_stack((x, y))

centroids = np.array([
    [1,2],
    [8,9],
    [50,50]
])

# membuat cluster
K = len(centroids)

klusters = []

for i in range(K):
    klusters.append([])
    
        
for data in data_points:
    all_distance_centroid = []
    
    for i in range(len(centroids)):
        centroid = centroids[i]
        
        #menghitung jarak equaliden
        distance = ((data[0] - centroid[0])**2 + (data[1] - centroid[1])**2)** 0.5
        
        all_distance_centroid.append(distance)
        
    index_terdekat = np.argmin(all_distance_centroid)
    
    klusters[index_terdekat].append(data)

for i in range(len(klusters)):
    print(f"kluster {i + 1} : {klusters[i]}")
    

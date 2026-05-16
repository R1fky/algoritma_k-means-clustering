import numpy as np

#fungsi menghitung distance
def distance(p, c):
    return ((p[0] - c[0])**2 + (p[1] - c[1])**2) ** 0.5


# fungsi kmeans
def k_means(point_datas, centroids):
    data = point_datas.copy()
    centroid = centroids.copy()

        
    # menghitung distance 
    status = True
    while(status):
        #membuat kluster tergantung centroid
        K = len(centroid)
        klusters = []
        for i in range(K):
            klusters.append([])
            
        for d in data:
            all_distance = []  
            for c in range(len(centroid)):
                pusat = centroid[c]
                
                #hitung jarak/ distance
                distances = distance(d, pusat)
                all_distance.append((distances))
                
            # mencari index terdekat
            index_terdekat = np.argmin(all_distance) 
                
            #masuk ke cluster 
            klusters[index_terdekat].append(d) 
        
        for k in range(len(klusters)):
            print(f"kluser {k + 1} : {klusters[k]}")
            
        status = False
        
    

# data yang mau di cluster 
x = np.array([1,2,3,8,9,10,50,55,60])
y = np.array([1,2,3,8,9,10,50,55,60])
datas = np.column_stack((x, y))

#centroid
c = np.array([
    [1,2],
    [8,9],
    [50,50]
])

k_means(datas, c)
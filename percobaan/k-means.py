import numpy as np

#fungsi menghitung distance
def distance(p, c):
    return ((p[0] - c[0])**2 + (p[1] - c[1])**2) ** 0.5

# menghitung centroid baru 
def calculate_new_c(cluster):
    if(len(cluster) == 0):
        return np.array([0,0])
    else: 
        cluster = np.array(cluster)
        
        values_0 = np.mean(cluster[:, 0])
        values_1 = np.mean(cluster[:, 1])
        
        return values_0, values_1
        
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
        
        # menghitung jarak atau distance data dan centroid
        for d in data:
            all_distance = []  
            for c in range(len(centroid)):
                titik = centroid[c]
                #hitung jarak/ distance
                distances = distance(d, titik)
                all_distance.append((distances))
                
            #  mencari index terdekat
            index_terdekat = np.argmin(all_distance) 
                
            # masuk ke cluster 
            klusters[index_terdekat].append(d) 
            
        
        #menghtitung new centroid
        new_centroid = []
        for k in range(len(klusters)):
            cluster = klusters[k]
            n_centroid = calculate_new_c(cluster)
            new_centroid.append(n_centroid)
        
        new_centroid = np.array(new_centroid)
        
        if(np.allclose(new_centroid, centroid)):
            status = False
        else:
            centroid = new_centroid
            
    return klusters
    

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

all_klusters = k_means(datas, c)

for kluster in range(len(all_klusters)):
    print(f'kluster ke {kluster + 1} : {all_klusters[kluster]}')
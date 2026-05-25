import numpy as np

#hitung jarak function
def distance(p, c):
    return ((p[0] - c[0])**2 + (p[1] - c[1])**2) ** 0.5


# fungsi predict cluster
def predict_cluster(datas, centroids):
    all_distance = []
    
    for centroid in centroids:
        #menghitung jarak
        d = distance(datas, centroid)
        
        all_distance.append(d)
    
    #clustering
    cluster = np.argmin(all_distance)
    
    return int(cluster)
        
        
        
    
    



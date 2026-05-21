#melihat perubahan algoritma
import numpy as np
import matplotlib.pyplot as plt
#aturan k-means
# jika jarak ke C1 < jarak ke C2 → masuk Cluster 1
# jika jarak ke C2 < jarak ke C1 → masuk Cluster 2

# menghitung jarak
def distance(p, c):
    return ((p[0] - c[0])**2 + (p[1] - c[1])**2) ** 0.5

# mencari centroid baru
def calculate_centroid(cluster):

    if len(cluster) == 0:
        return np.array([0,0])

    cluster = np.array(cluster)

    return np.array([
        np.mean(cluster[:,0]),
        np.mean(cluster[:,1])
    ])

#K Means function
def kMeans(x, y, c1 , c2):
    x_datas  = x.copy()
    y_datas = y.copy() 
    
    # history centroid berubah- ubah
    history_centroid1 = []
    history_centroid2 = []
    
    history_centroid1.append(c1.copy())
    history_centroid2.append(c2.copy())
    
    
    #menggabungkan data
    point = np.column_stack((x_datas, y_datas))
    
    # mencari cluster
    status = True 
    while(status):
        cluster1 = []
        cluster2 = []
        
        #mencari jarak distance dan menentukan cluster   
        for data in point:
            jarak_c1 = distance(data, c1)
            jarak_c2 = distance(data, c2)
            
            if(jarak_c1 < jarak_c2):
                cluster1.append(data)
            else:
                cluster2.append(data)
                
        # mencari new centroid
        new_c1 = calculate_centroid(cluster1)
        new_c2 = calculate_centroid(cluster2)
        
        if(np.array_equal(new_c1, c1) and np.array_equal(new_c2, c2)):
            status = False
        else:
            c1 = new_c1
            c2 = new_c2
            history_centroid1.append(c1.copy())
            history_centroid2.append(c2.copy())
            
    return cluster1, cluster2, c1, c2, history_centroid1, history_centroid2
        
            
# data 
x = np.array([41, 47, 33, 29])
y = np.array([19, 100, 57, 19])
c1 = np.array([41, 19])
c2 = np.array([47, 100])

# c1 = np.array([0,0])
# c2 = np.array([100,100])

#mencari cluster
kluster1, kluster2, new_centroid_1, new_centroid_2, h1, h2 = kMeans(x, y, c1, c2)
kluster1 = np.array(kluster1)
kluster2 = np.array(kluster2)
print("cluster")
print(kluster1)
print(kluster2)
print("centroid")
print("="*20)
print("history centroid")
h1 = np.array(h1)
h2 = np.array(h2)
print(h1)
print(h2)
print("="*20)
print('centroid baru/ new c1: ', new_centroid_1)
print('centroid baru/ new c2: ', new_centroid_2)
print("end cluster end centroid")
# x dan y kluster 1
x_cluster1 = kluster1[:, 0]
y_cluster1 = kluster1[:, 1]
print(x_cluster1)
print(y_cluster1)
# x dan y kluster 2
x_cluster2 = kluster2[:, 0]
y_cluster2 = kluster2[:, 1]
print(x_cluster2)
print(y_cluster2)

# plot scatter sesudah cluster
plt.scatter(x_cluster1, y_cluster1, label='data cluster 1', color="r")
plt.scatter(x_cluster2, y_cluster2, label='data cluster 2', color="y")

for p in h1:
    plt.scatter(p[0], p[1], marker='o', s=200, color="g")
for q in h2:
    plt.scatter(q[0], q[1], marker='x', s=200, color="b", )
# plt.scatter(new_centroid_1[0], new_centroid_1[1], label="centroid 1", marker='o', s=200, color="g")
# plt.scatter(new_centroid_2[0], new_centroid_2[1], label="centroid 2", marker='x', s=200, color="b")
plt.xlabel("sumbu X")
plt.ylabel("sumbu Y")

# menampilkan plot
plt.legend()
plt.show()

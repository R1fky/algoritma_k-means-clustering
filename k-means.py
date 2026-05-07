# data = [(41,19), (47,100), (33,57), (29,19)]
# c1 = (41,19)
# c2 = (47,100)
# aturan k- means
# jika jarak ke C1 < jarak ke C2 → masuk Cluster 1
# jika jarak ke C2 < jarak ke C1 → masuk Cluster 2

#fungsi menghitung jarak
def distance(p, c):
    return ((p[0] - c[0])**2 + (p[1] - c[1])**2) ** 0.5

#fungsi menghitung new centroid
def calculate_new_centroid(klusters) :
    kluster = klusters.copy()
    
    if len(klusters) == 0:
        return (0,0)
    # for x axis
    sum_x = 0
    sum_y = 0
    data_x = []
    data_y = []
    for k in kluster:
        sum_x += k[0]
        sum_y += k[1]
        data_x.append(k[0])
        data_y.append(k[1])
    new_x = sum_x / len(data_x)
    new_y = sum_y / len(data_y)
    
    return new_x, new_y

def k_means(datas, c1, c2):
    data = datas.copy()
    
    # 1. reset cluster kosong
    # 2. assign cluster
    # 3. hitung centroid baru
    # 4. cek apakah centroid berubah
    # 5. update centroid
    
    perubahan = True
    iterasi = 0
    while(perubahan):
        iterasi += 1 
        cluster1 = []
        cluster2 = []
        # hitung jarak dan assign cluster dengan centroid baru
        for d in data:
            jarak_c1 = distance(d, c1)
            jarak_c2 = distance(d, c2)
            
            if(jarak_c1 < jarak_c2):
                cluster1.append(d)
            else:
                cluster2.append(d)
        print('iterasi', iterasi)
        print('clutser 1 : ',cluster1)
        print('cluster 2 : ',cluster2)
        
        #hitung ulang centroid baru
        centroid1_baru = calculate_new_centroid(cluster1)
        centroid2_baru = calculate_new_centroid(cluster2)
        
        print("centroid lama:", c1, c2)
        print("centroid baru:", centroid1_baru, centroid2_baru)
        
        if(centroid1_baru == c1 and centroid2_baru == c2):
            perubahan = False
        else:
            c1 = centroid1_baru
            c2 = centroid2_baru
    
    return cluster1, cluster2
        
    
list_data = [(41,19), (47,100), (33,57), (29,19)]
# c1 = (41,19)
# c2 = (47,100)

c1 = (100,0)
c2 = (0,100)

kluster_1, kluster_2 = k_means(list_data, c1, c2)

print('kluster 1 :', kluster_1)
print('kluster 2 :', kluster_2)
        
# data = [(41,19), (47,100), (33,57), (29,19)]
# c1 = (41,19)
# c2 = (47,100)
# aturan k- means
# jika jarak ke C1 < jarak ke C2 → masuk Cluster 1
# jika jarak ke C2 < jarak ke C1 → masuk Cluster 2
def k_means_1_iterasi(datas, c1, c2):
    data = datas.copy()
    cluster1_lokal = []
    cluster2_lokal = []
    #penjumlahan 
    for d in data:
        hasil_c1 = ((d[0] - c1[0])**2 + (d[1] - c1[1])**2) ** 0.5
        hasil_c2 = ((d[0] - c2[0])**2 + (d[1] - c2[1])**2) ** 0.5 
        print(f"jarak c1 : {hasil_c1}")
        print(f"jarak c2 : {hasil_c2}")
        
        if(hasil_c1 < hasil_c2):
            cluster1_lokal.append(d)
        elif(hasil_c2 < hasil_c1):
            cluster2_lokal.append(d)
            
            
    return cluster1_lokal, cluster2_lokal
        
    
list_data = [(41,19), (47,100), (33,57), (29,19)]
print(len(list_data[0]))
c1 = (41,19)
c2 = (47,100)

kluster_1, kluster_2 = k_means_1_iterasi(list_data, c1, c2)

print('kluster 1 :', kluster_1)
print('kluster 2 :', kluster_2)

#menentukan nilai centroid baru
# centorid 1
jumlahIndex0 = 0
jumlahIndex1 = 0
panjangIndex0 = []
panjangIndex1 = []

for i in kluster_1:
    jumlahIndex0 += i[0]
    jumlahIndex1 += i[1]
    panjangIndex0.append(i[0])
    panjangIndex1.append(i[1])
    
new_centroid1 = ((jumlahIndex0 / len(panjangIndex0)), (jumlahIndex1 / len(panjangIndex1)))
print(f"nilai new centroid 1 : {new_centroid1}") 

# cenrtroid 2
jumlahIndex0_c2 = 0
jumlahIndex1_c2 = 0
panjangIndex0_c2 = []
panjangIndex1_c2 = []
for i in kluster_2:
    jumlahIndex0_c2 += i[0]
    jumlahIndex1_c2 += i[1]
    panjangIndex0_c2.append(i[0])
    panjangIndex1_c2.append(i[1])
    
new_centroid2 = ((jumlahIndex0_c2 / len(panjangIndex0_c2)), (jumlahIndex1_c2 / len(panjangIndex1_c2)))
print(f"nilai new centroid 2 : {new_centroid2}")

#cara clean hitung new centroid
# sum_x = sum([p[0] for p in kluster_1])
# sum_y = sum([p[1] for p in kluster_1])

# centroid1 = (sum_x / len(kluster_1), sum_y / len(kluster_1))
# print(centroid1)



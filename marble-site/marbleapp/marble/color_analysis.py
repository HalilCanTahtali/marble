# import cv2

# def boyut(x):
   
  
#     originalImage = cv2.imread("uploads"+x)
    
#     return [{"renk1":"rgb(82, 1, 42)" , "renk2":"rgb(124, 185, 239)","renk3":"rgb(200, 159, 79)","yüzde1":"60%","yüzde2":"30%","yüzde3":"10%"},]


import cv2, numpy as np
from sklearn.cluster import KMeans

renkkodları = ["", "", "","",""]
yüzdeler = ["", "", "","",""]
hex=["","",""]

def renkanaliz(imagepath):
    try:
    
        # Load image
        src_image = cv2.imread("uploads"+imagepath)
        src_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2RGB)
        reshape_img = src_image.reshape(((src_image.shape[0]) * (src_image.shape[1]), 3))



        
        #çıktı sayısı
        cluster  = KMeans(n_clusters=5).fit(reshape_img)
        
        C_centroids = cluster.cluster_centers_
        


        C_labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
        (C_hist, _ ) = np.histogram(cluster.labels_, bins=C_labels)
        C_hist = C_hist.astype("float")
        C_hist /= C_hist.sum()

        rect_color = np.zeros((50, 300, 3), dtype=np.uint8)
        img_colors = sorted([(percent, color) for (percent, color) in zip(C_hist, C_centroids)])
        start = 0

        i = 0
        for (percent, color) in img_colors:
            
            yüzdeler[i] = int(percent * 100)
            
            end = start + (percent * 300)
            

            start = end
            rgb = color

            hex[0] = ('{:X}').format(int(rgb[0])) 
            hex[1] = ('{:X}').format(int(rgb[1])) 
            hex[2] = ('{:X}').format(int(rgb[2])) 
            if(len(hex[0])<2):
                hex[0]="0"+hex[0]
            if(len(hex[1])<2):
                hex[1]="0"+hex[1]  
            if(len(hex[2])<2):
                hex[2]="0"+hex[2]  
                
            renkkodları[i]="#"+str(hex[0])+str(hex[1])+str(hex[2])
            i =i+1
        toplam = sum(yüzdeler)
        fark= 100 - toplam
        
        yüzdeler[2] = yüzdeler[2]+fark
        
            
            
        return [{
            "renk1" : str(renkkodları[4]),
            "renk2" : str(renkkodları[3]),
            "renk3" : str(renkkodları[2]),
            "renk4" : str(renkkodları[1]),
            "renk5" : str(renkkodları[0]),
            "yüzde1" : int(yüzdeler[4]),
            "yüzde2" : int(yüzdeler[3]),
            "yüzde3" : int(yüzdeler[2]),
            "yüzde4" : int(yüzdeler[1]),
            "yüzde5" : int(yüzdeler[0]),
            
            }]
        
    except:
        
        return [{
            "renk1":"rgb(82, 1, 42)",
            "renk2":"rgb(124, 185, 239)",
            "renk3":"rgb(200, 159, 79)",
            "yüzde1":"60%",
            "yüzde2":"30%",
            "yüzde3":"10%"
            }] 
    
    
    
    
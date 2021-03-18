import cv2
import numpy as np
from KMeans import ClusterImages
from LSB import LSB

def imageDecrypt(input_file):
    image = cv2.imread(input_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image1 = image.reshape(image.shape[0] * image.shape[1], 3)
    labels, centers, bar, maxCluster = ClusterImages(image1).getCluster()

    img = cv2.imread(input_file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    labels = labels.reshape(img.shape[0], img.shape[1])
    index2 = np.argwhere(labels == maxCluster).tolist()
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    steg = LSB(img, index2)

    return steg.decode_text()


#input_file = input("Enter File To Be Decoded : ")
#print(imageDncrypt(input_file))



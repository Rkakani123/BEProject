import cv2
import numpy as np
from KMeans import ClusterImages
from LSB import LSB

def imageEncrypt(input_file, data ):

    image = cv2.imread(input_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image1 = image.reshape(image.shape[0] * image.shape[1], 3)
    labels, centers, bar, maxCluster = ClusterImages(image1).getCluster()

    labels = labels.reshape(image.shape[0], image.shape[1])
    index1 = np.argwhere(labels == maxCluster).tolist()
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    steg = LSB(image, index1)

    output_file = "SampleShare"
    output_file = output_file + ".png"
    cv2.imwrite(output_file, steg.encode_text(data))

    return True

'''
input_file = input("Enter Cover Image Name : ")
data = input("Enter Your Secret Data : ")
print(type(data))
if(imageEncrypt(input_file,data)):
    print("Operation Successfully Completed...!")
'''
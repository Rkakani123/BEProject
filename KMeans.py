import cv2
import numpy as np
from sklearn.cluster import KMeans

class ClusterImages():

    def __init__(self, im):
        clf = KMeans(n_clusters=3, n_jobs=-1)
        clf.fit(im)

        self.labels = clf.labels_
        self.centers = clf.cluster_centers_

    def getCluster(self):
        self.hist = self.centroid_histogram()
        self.bar = self.plot_colors()
        self.maxCluster = self.max_cluster()

        return self.labels, self.centers, self.bar, self.maxCluster

    def centroid_histogram(self):
        numLabels = np.arange(0, len(np.unique(self.labels)) + 1)
        hist, _ = np.histogram(self.labels, bins=numLabels)
        hist = hist.astype("float")
        hist /= hist.sum()

        return hist

    def plot_colors(self):
        bar = np.zeros((50, 300, 3), dtype="uint8")
        startX = 0
        for (percent, color) in zip(self.hist, self.centers):
            endX = startX + (percent * 300)
            cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
            startX = endX

        return bar

    def max_cluster(self):
        nLabels = np.arange(0, len(np.unique(self.labels)) + 1)
        countLabels, _ = np.histogram(self.labels, bins=nLabels)
        countLabels = countLabels.tolist()
        maxcluster = countLabels.index(max(countLabels))

        return maxcluster

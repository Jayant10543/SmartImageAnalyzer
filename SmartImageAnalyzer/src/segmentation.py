import cv2
import numpy as np
from sklearn.cluster import KMeans


def threshold_segmentation(gray_image):
    _, segmented = cv2.threshold(
        gray_image,
        127,
        255,
        cv2.THRESH_BINARY
    )

    return segmented


def kmeans_segmentation(image, k=3):
    pixels = image.reshape((-1, 3))
    pixels = np.float32(pixels)

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(pixels)

    centers = np.uint8(kmeans.cluster_centers_)

    segmented_pixels = centers[labels]

    segmented_image = segmented_pixels.reshape(image.shape)

    return segmented_image
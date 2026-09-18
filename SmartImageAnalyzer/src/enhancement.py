import cv2
import matplotlib.pyplot as plt


def convert_to_grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


def apply_gaussian_filter(image):
    filtered = cv2.GaussianBlur(image, (5, 5), 0)
    return filtered


def apply_histogram_equalization(gray_image):
    equalized = cv2.equalizeHist(gray_image)
    return equalized


def create_histogram(gray_image, output_path):
    plt.figure()
    plt.hist(gray_image.ravel(), 256, [0, 256])
    plt.title("Grayscale Image Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.savefig(output_path)
    plt.close()
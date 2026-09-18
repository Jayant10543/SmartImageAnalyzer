import cv2
import os


def load_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError("Image file not found.")

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Could not read the image.")

    return image


def save_image(image, output_path):
    success = cv2.imwrite(output_path, image)

    if not success:
        raise ValueError("Could not save the image.")
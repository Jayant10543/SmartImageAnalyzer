import cv2
import numpy as np


def detect_canny_edges(gray_image):
    edges = cv2.Canny(gray_image, 100, 200)
    return edges


def detect_harris_corners(gray_image):
    gray_float = np.float32(gray_image)

    corners = cv2.cornerHarris(gray_float, 2, 3, 0.04)

    result = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

    result[corners > 0.01 * corners.max()] = [0, 0, 255]

    return result


def detect_hough_lines(edges, original_image):
    lines = cv2.HoughLinesP(
        edges,
        1,
        np.pi / 180,
        threshold=50,
        minLineLength=50,
        maxLineGap=10
    )

    result = original_image.copy()

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line

            cv2.line(
                result,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

    return result
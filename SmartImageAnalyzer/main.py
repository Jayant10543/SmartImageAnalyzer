import os
from src.image_utils import load_image, save_image

from src.enhancement import (
    convert_to_grayscale,
    apply_gaussian_filter,
    apply_histogram_equalization,
    create_histogram
)

from src.edge_detection import (
    detect_canny_edges,
    detect_harris_corners,
    detect_hough_lines
)

from src.segmentation import (
    threshold_segmentation,
    kmeans_segmentation
)

from src.object_analysis import analyze_objects

from src.report import create_report

os.makedirs("outputs", exist_ok=True)

# Load input image
try:
    image = load_image("input/sample.jpg")
except (FileNotFoundError, ValueError) as error:
    print("Error:", error)
    exit()


# Image Enhancement
gray = convert_to_grayscale(image)

filtered = apply_gaussian_filter(image)

equalized = apply_histogram_equalization(gray)

save_image(gray, "outputs/grayscale.jpg")
save_image(filtered, "outputs/filtered.jpg")
save_image(equalized, "outputs/equalized.jpg")

create_histogram(
    gray,
    "outputs/histogram.png"
)


# Edge and Feature Detection
edges = detect_canny_edges(gray)

corners = detect_harris_corners(gray)

lines = detect_hough_lines(
    edges,
    image
)

save_image(
    edges,
    "outputs/canny_edges.jpg"
)

save_image(
    corners,
    "outputs/harris_corners.jpg"
)

save_image(
    lines,
    "outputs/hough_lines.jpg"
)


# Image Segmentation
threshold = threshold_segmentation(gray)

kmeans = kmeans_segmentation(image)

save_image(
    threshold,
    "outputs/threshold_segmentation.jpg"
)

save_image(
    kmeans,
    "outputs/kmeans_segmentation.jpg"
)


# Object Analysis
detected_image, objects = analyze_objects(
    threshold,
    image
)

save_image(
    detected_image,
    "outputs/detected_objects.jpg"
)

print("Objects detected:", len(objects))


# Generate Report
create_report(
    image,
    objects,
    "outputs/report.json"
)

print("Report generated successfully!")


# Final Status
print("Image enhancement completed!")
print("Edge and feature detection completed!")
print("Image segmentation completed!")

print("Generated:")

print("- grayscale.jpg")
print("- filtered.jpg")
print("- equalized.jpg")
print("- histogram.png")
print("- canny_edges.jpg")
print("- harris_corners.jpg")
print("- hough_lines.jpg")
print("- threshold_segmentation.jpg")
print("- kmeans_segmentation.jpg")
print("- detected_objects.jpg")
print("- report.json")
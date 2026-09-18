import json


def create_report(image, objects, output_path):
    height, width, channels = image.shape

    report = {
        "image_width": width,
        "image_height": height,
        "number_of_channels": channels,
        "number_of_detected_objects": len(objects),
        "objects": objects,
        "techniques_used": [
            "Grayscale Conversion",
            "Gaussian Filtering",
            "Histogram Equalization",
            "Histogram Analysis",
            "Canny Edge Detection",
            "Harris Corner Detection",
            "Hough Line Detection",
            "Threshold Segmentation",
            "K-Means Segmentation",
            "Contour Analysis"
        ]
    }

    with open(output_path, "w") as file:
        json.dump(report, file, indent=4)
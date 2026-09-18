import os

from src.image_utils import load_image
from src.enhancement import (
    convert_to_grayscale,
    apply_gaussian_filter,
    apply_histogram_equalization
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


IMAGE_PATH = "input/sample.jpg"


def test_image_exists():
    assert os.path.exists(IMAGE_PATH)


def test_image_loading():
    image = load_image(IMAGE_PATH)

    assert image is not None
    assert len(image.shape) == 3


def test_grayscale_conversion():
    image = load_image(IMAGE_PATH)

    gray = convert_to_grayscale(image)

    assert gray is not None
    assert len(gray.shape) == 2


def test_gaussian_filter():
    image = load_image(IMAGE_PATH)

    filtered = apply_gaussian_filter(image)

    assert filtered is not None
    assert filtered.shape == image.shape


def test_histogram_equalization():
    image = load_image(IMAGE_PATH)

    gray = convert_to_grayscale(image)
    equalized = apply_histogram_equalization(gray)

    assert equalized is not None
    assert equalized.shape == gray.shape


def test_canny_detection():
    image = load_image(IMAGE_PATH)

    gray = convert_to_grayscale(image)
    edges = detect_canny_edges(gray)

    assert edges is not None
    assert len(edges.shape) == 2


def test_harris_detection():
    image = load_image(IMAGE_PATH)

    gray = convert_to_grayscale(image)
    corners = detect_harris_corners(gray)

    assert corners is not None
    assert corners.shape == image.shape


def test_hough_detection():
    image = load_image(IMAGE_PATH)

    gray = convert_to_grayscale(image)
    edges = detect_canny_edges(gray)

    lines = detect_hough_lines(edges, image)

    assert lines is not None
    assert lines.shape == image.shape


def test_threshold_segmentation():
    image = load_image(IMAGE_PATH)

    gray = convert_to_grayscale(image)
    segmented = threshold_segmentation(gray)

    assert segmented is not None
    assert len(segmented.shape) == 2


def test_kmeans_segmentation():
    image = load_image(IMAGE_PATH)

    segmented = kmeans_segmentation(image, k=3)

    assert segmented is not None
    assert segmented.shape == image.shape


def test_object_analysis():
    image = load_image(IMAGE_PATH)

    gray = convert_to_grayscale(image)
    segmented = threshold_segmentation(gray)

    detected_image, objects = analyze_objects(
        segmented,
        image
    )

    assert detected_image is not None
    assert isinstance(objects, list)
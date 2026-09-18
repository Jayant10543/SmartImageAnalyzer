# Smart Image Analyzer & Object Segmentation System

## 1. Problem Statement

Digital images contain a large amount of visual information, but manually analyzing different image characteristics can be time-consuming. Different computer vision techniques are required to enhance images, detect important features, segment regions, and analyze objects.

The problem addressed by this project is to develop a simple and modular computer vision system that can process an input image and apply multiple image analysis techniques in a single workflow.

The system accepts an input image and performs image enhancement, edge and feature detection, image segmentation, and object analysis. The results are saved as separate output images along with a JSON analysis report.

## 2. Project Scope

The project focuses on fundamental computer vision operations that can be applied to a single input image.

The system includes:

- Grayscale conversion
- Gaussian filtering
- Histogram generation
- Histogram equalization
- Canny edge detection
- Harris corner detection
- Hough line detection
- Threshold-based segmentation
- K-Means segmentation
- Contour detection
- Bounding box detection
- Object area calculation
- Object counting
- Automatic JSON report generation

The project does not focus on real-time video processing, deep learning-based object detection, or 3D computer vision.

## 3. Target Users

The system is primarily intended for:

- Computer vision students
- Beginners learning image processing
- Students experimenting with different computer vision techniques
- Users who want to observe the effect of multiple image processing methods on an image

## 4. High-Level Features

### Image Enhancement

The system converts the input image to grayscale, applies Gaussian filtering, performs histogram equalization, and generates a grayscale histogram.

### Edge and Feature Detection

The system uses Canny edge detection to identify edges, Harris corner detection to identify corner features, and Hough line detection to identify straight lines.

### Image Segmentation

The system performs threshold-based segmentation and K-Means segmentation to divide image pixels into different regions.

### Object Analysis

The system detects contours from the segmented image, calculates object areas, generates bounding boxes, and counts detected objects.

### Automated Report

The system generates a JSON report containing image dimensions, number of detected objects, object information, and the computer vision techniques used.

## 5. Input

The system accepts:

- A single image file
- Supported image formats depend on OpenCV image decoding

The input image is placed inside the `input` folder.

## 6. Output

The system produces:

- Grayscale image
- Gaussian-filtered image
- Histogram
- Histogram-equalized image
- Canny edge image
- Harris corner image
- Hough line image
- Threshold segmentation image
- K-Means segmentation image
- Object detection image
- JSON analysis report
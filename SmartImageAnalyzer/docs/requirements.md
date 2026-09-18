# System Requirements

## 1. Functional Requirements

### FR1: Image Input

The system shall allow the user to provide a single image as input through the `input` folder.

### FR2: Image Validation

The system shall verify that the input image exists and can be successfully read before processing.

### FR3: Image Enhancement

The system shall perform the following image enhancement operations:

- Grayscale conversion
- Gaussian filtering
- Histogram equalization
- Histogram generation

### FR4: Edge and Feature Detection

The system shall detect important image features using:

- Canny edge detection
- Harris corner detection
- Hough line detection

### FR5: Image Segmentation

The system shall segment the input image using:

- Threshold-based segmentation
- K-Means segmentation

### FR6: Object Analysis

The system shall analyze segmented regions using contour detection.

The system shall:

- Calculate object areas
- Generate bounding boxes
- Count detected objects
- Ignore regions with an area of 100 pixels or less

### FR7: Output Generation

The system shall save the processed images in the `outputs` folder.

### FR8: Report Generation

The system shall generate a JSON report containing:

- Image dimensions
- Number of detected objects
- Object areas
- Object locations
- Bounding box dimensions
- Techniques used

### FR9: Error Handling

The system shall display an appropriate error message when the input image is missing, invalid, or cannot be processed.

---

## 2. Non-Functional Requirements

### NFR1: Usability

The system should be simple to execute and should provide clear status messages after processing.

### NFR2: Maintainability

The implementation shall use separate modules for different computer vision operations so that individual components can be modified independently.

### NFR3: Reliability

The system should validate the input image before performing processing operations.

### NFR4: Error Handling

The system should handle invalid or missing input files without causing unexpected processing errors.

### NFR5: Performance

The system should process a normal-sized input image within a reasonable amount of time on a standard computer.

### NFR6: Resource Efficiency

The system should process one input image at a time and avoid unnecessary storage of intermediate data.

### NFR7: Modularity

The system should separate image loading, enhancement, feature detection, segmentation, object analysis, and report generation into different modules.

### NFR8: Testability

The major processing components should be testable independently using automated tests.
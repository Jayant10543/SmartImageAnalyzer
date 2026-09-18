# System Workflow

## 1. Workflow Overview

The Smart Image Analyzer & Object Segmentation System processes an input image through a sequence of computer vision operations.

The workflow starts with loading and validating the image and ends with processed output images and a JSON analysis report.

## 2. Processing Workflow

### Step 1: Input Image

The user places an image inside the `input` folder.

The system loads the image using OpenCV.

If the image does not exist or cannot be read, an appropriate error message is displayed.

### Step 2: Image Enhancement

The input image is processed using several enhancement techniques.

The system:

1. Converts the image to grayscale.
2. Applies Gaussian filtering.
3. Performs histogram equalization.
4. Generates a grayscale histogram.

The generated results are saved in the `outputs` folder.

### Step 3: Edge and Feature Detection

The grayscale image is used for feature detection.

The system applies:

1. Canny edge detection
2. Harris corner detection
3. Hough line detection

Each technique produces a separate output image.

### Step 4: Image Segmentation

The system performs two segmentation techniques.

#### Threshold Segmentation

The grayscale image is converted into a binary image using a fixed threshold value.

#### K-Means Segmentation

The color pixels of the original image are grouped into three clusters using K-Means clustering.

Both segmentation results are saved as output images.

### Step 5: Object Analysis

The threshold-segmented image is analyzed to identify object regions.

The system:

1. Finds contours.
2. Calculates the area of detected regions.
3. Generates bounding boxes.
4. Counts detected objects.

Small regions with an area of 100 pixels or less are ignored.

### Step 6: Report Generation

The system collects information from the object analysis stage.

A JSON report is generated containing:

- Image width
- Image height
- Number of image channels
- Number of detected objects
- Object areas
- Bounding box coordinates
- Bounding box dimensions
- Computer vision techniques used

The report is saved as:

`outputs/report.json`

## 3. Overall Workflow

```text
                START
                  │
                  ▼
          Load Input Image
                  │
                  ▼
           Validate Image
                  │
                  ▼
        Image Enhancement
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
    Grayscale  Gaussian  Histogram
               Filter     Equalization
                  │
                  ▼
       Edge & Feature Detection
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
      Canny    Harris      Hough
      Edges    Corners     Lines
                  │
                  ▼
          Image Segmentation
             ┌────┴────┐
             ▼         ▼
         Threshold   K-Means
             │
             ▼
         Object Analysis
             │
       ┌─────┼─────┐
       ▼     ▼     ▼
    Contours Area  Bounding
                  Boxes
             │
             ▼
        Object Counting
             │
             ▼
       Generate JSON Report
             │
             ▼
       Save All Outputs
             │
             ▼
             END
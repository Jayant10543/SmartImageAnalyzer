# Sequence Diagram

## 1. Overview

The sequence diagram shows the order in which the user and the different system modules interact during image processing.

## 2. Sequence Diagram

```mermaid
sequenceDiagram

    actor User
    participant Main as main.py
    participant Utils as image_utils.py
    participant Enhancement as enhancement.py
    participant Edge as edge_detection.py
    participant Segmentation as segmentation.py
    participant Analysis as object_analysis.py
    participant Report as report.py

    User->>Main: Run application

    Main->>Utils: Load input image
    Utils-->>Main: Return image

    Main->>Enhancement: Convert to grayscale
    Enhancement-->>Main: Return grayscale image

    Main->>Enhancement: Apply Gaussian filtering
    Enhancement-->>Main: Return filtered image

    Main->>Enhancement: Apply histogram equalization
    Enhancement-->>Main: Return equalized image

    Main->>Enhancement: Generate histogram
    Enhancement-->>Main: Save histogram

    Main->>Edge: Detect Canny edges
    Edge-->>Main: Return edge image

    Main->>Edge: Detect Harris corners
    Edge-->>Main: Return corner image

    Main->>Edge: Detect Hough lines
    Edge-->>Main: Return line image

    Main->>Segmentation: Perform threshold segmentation
    Segmentation-->>Main: Return segmented image

    Main->>Segmentation: Perform K-Means segmentation
    Segmentation-->>Main: Return segmented image

    Main->>Analysis: Analyze segmented image
    Analysis-->>Main: Return detected objects

    Main->>Report: Generate JSON report
    Report-->>Main: Save report.json

    Main-->>User: Display completion message
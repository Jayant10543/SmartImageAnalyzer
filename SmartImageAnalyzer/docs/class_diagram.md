# Class / Component Diagram

## 1. Overview

The system is divided into separate Python modules. Each module is responsible for a specific computer vision task.

The modules communicate through image data and processing results.

## 2. Component Diagram

```mermaid
flowchart TD

    Main[main.py<br/>Main Controller]

    Utils[src/image_utils.py<br/>Image Loading & Saving]

    Enhancement[src/enhancement.py<br/>Image Enhancement]

    Edge[src/edge_detection.py<br/>Edge & Feature Detection]

    Segmentation[src/segmentation.py<br/>Image Segmentation]

    Analysis[src/object_analysis.py<br/>Object Analysis]

    Report[src/report.py<br/>Report Generation]

    Main --> Utils
    Main --> Enhancement
    Main --> Edge
    Main --> Segmentation
    Main --> Analysis
    Main --> Report

    Utils --> Enhancement
    Enhancement --> Edge
    Enhancement --> Segmentation
    Segmentation --> Analysis
    Analysis --> Report
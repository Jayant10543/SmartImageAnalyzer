# Use Case Diagram

## 1. Actors

The primary actor of the system is:

- User

The user provides an input image and runs the image analysis system.

## 2. Main Use Cases

The user can:

- Provide an input image
- Run image analysis
- Perform image enhancement
- Detect edges and features
- Perform image segmentation
- Analyze detected objects
- View generated output images
- Generate and view the JSON report

## 3. Use Case Diagram

```mermaid
flowchart LR

    User([User])

    Input[Provide Input Image]
    Process[Run Image Analysis]
    Enhance[Image Enhancement]
    Detect[Edge & Feature Detection]
    Segment[Image Segmentation]
    Analyze[Object Analysis]
    Outputs[View Output Images]
    Report[Generate JSON Report]

    User --> Input
    User --> Process

    Process --> Enhance
    Process --> Detect
    Process --> Segment
    Process --> Analyze
    Process --> Outputs
    Process --> Report
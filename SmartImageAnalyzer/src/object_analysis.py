import cv2


def find_contours(segmented_image):
    contours, _ = cv2.findContours(
        segmented_image,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    return contours


def analyze_objects(segmented_image, original_image):
    contours = find_contours(segmented_image)

    result = original_image.copy()
    objects = []

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 100:
            x, y, width, height = cv2.boundingRect(contour)

            cv2.rectangle(
                result,
                (x, y),
                (x + width, y + height),
                (0, 255, 0),
                2
            )

            objects.append({
                "area": float(area),
                "x": int(x),
                "y": int(y),
                "width": int(width),
                "height": int(height)
            })

    return result, objects
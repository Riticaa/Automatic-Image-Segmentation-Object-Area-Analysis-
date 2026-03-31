import cv2

def analyze_objects(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    areas = []
    total_area = mask.shape[0] * mask.shape[1]

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50:
            areas.append(area)

    return areas, total_area
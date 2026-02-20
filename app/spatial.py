class SpatialAnalyzer:
    def __init__(self):
        print("Spatial Analyzer initialized")

    def analyze(self, detections, frame):
        height, width, _ = frame.shape
        spatial_data = []

        for obj in detections:
            x1, y1, x2, y2 = obj["bbox"]

            # --- Distance Estimation (area-based) ---
            area = (x2 - x1) * (y2 - y1)

            if area > 5000:
                distance = "near"
            elif area > 1500:
                distance = "medium"
            else:
                distance = "far"

            # --- Direction Estimation ---
            center_x = (x1 + x2) / 2

            if center_x < width / 3:
                direction = "left"
            elif center_x < (2 * width / 3):
                direction = "center"
            else:
                direction = "right"

            spatial_data.append({
                "object": obj["object"],
                "distance": distance,
                "direction": direction,
                "area": area
            })

        return spatial_data

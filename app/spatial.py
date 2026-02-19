class SpatialAnalyzer:
    def __init__(self):
        print("Spatial Analyzer initialized")

    def analyze(self, detections, frame):
        analyzed = []
        frame_height, frame_width, _ = frame.shape

        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            box_height = y2 - y1
            box_area = (x2 - x1) * (y2 - y1)

            # Relative height ratio
            height_ratio = box_height / frame_height

            # Distance estimation based on bbox height
            if height_ratio > 0.5:
                distance = "near"
            elif height_ratio > 0.25:
                distance = "medium"
            else:
                distance = "far"

            analyzed.append({
                "object": det["object"],
                "distance": distance,
                "area": box_area
            })

        return analyzed

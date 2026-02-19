class SpatialAnalyzer:
    def __init__(self):
        print("Spatial Analyzer initialized")

    def analyze(self, detections):
        enriched = []

        for obj in detections:
            area = obj["box_area"]

            # Simple distance heuristic
            if area > 100000:
                distance = "near"
            elif area > 30000:
                distance = "medium"
            else:
                distance = "far"

            obj["distance"] = distance
            enriched.append(obj)

        return enriched

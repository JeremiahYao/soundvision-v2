class SpatialAnalyzer:
    def __init__(self):
        print("Spatial Analyzer initialized")

    def estimate_distance(self, bbox, frame_width, frame_height):
        """
        Estimate relative distance using bounding box area ratio.
        """

        x1, y1, x2, y2 = bbox

        bbox_width = x2 - x1
        bbox_height = y2 - y1

        bbox_area = bbox_width * bbox_height
        frame_area = frame_width * frame_height

        if frame_area == 0:
            return "far"

        relative_size = bbox_area / frame_area

        # Tunable thresholds
        if relative_size > 0.15:
            return "near"
        elif relative_size > 0.05:
            return "medium"
        else:
            return "far"


    def analyze(self, detections, frame):
        """
        Convert YOLO detections into structured spatial data
        """

        spatial_data = []

        frame_height, frame_width = frame.shape[:2]

        for det in detections:

            # Expected YOLO detection format:
            # det = {
            #     "object": class_name,
            #     "bbox": [x1, y1, x2, y2],
            #     "confidence": conf_score
            # }

            object_name = det.get("object")
            bbox = det.get("bbox")

            if object_name is None or bbox is None:
                continue

            distance = self.estimate_distance(
                bbox,
                frame_width,
                frame_height
            )

            spatial_data.append({
                "object": object_name,
                "distance": distance
            })

        return spatial_data

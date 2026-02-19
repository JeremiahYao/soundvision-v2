from ultralytics import YOLO


class Detector:
    def __init__(self):
        print("Loading YOLO model...")
        self.model = YOLO("yolov8n.pt")
        print("YOLO loaded.")

    def detect(self, frame):
        results = self.model(frame, verbose=False)

        detections = []

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]
                confidence = float(box.conf[0])

                x1, y1, x2, y2 = box.xyxy[0]
                box_area = (x2 - x1) * (y2 - y1)

                detections.append({
                    "object": label,
                    "confidence": confidence,
                    "box_area": float(box_area)
                })

        return detections

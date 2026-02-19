from ultralytics import YOLO


class Detector:
    def __init__(self):
        print("Loading YOLO model...")
        self.model = YOLO("yolov8n.pt")  # nano version (fastest)
        print("YOLO loaded.")

    def detect(self, frame):
        results = self.model(frame, verbose=False)

        detections = []

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]

                detections.append({
                    "object": label,
                    "confidence": float(box.conf[0]),
                })

        return detections

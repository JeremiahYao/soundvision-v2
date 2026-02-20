import cv2
from detector import Detector
from spatial import SpatialAnalyzer
from risk_engine import RiskEngine
from guidance import GuidanceSystem

def main():

    print("Starting SoundVision V2 Video Mode...")

    # ===== VIDEO INPUT =====
    video_path = "demo_video.mp4"
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # ===== VIDEO OUTPUT =====
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(
        'output_demo.mp4',
        fourcc,
        20.0,
        (int(cap.get(3)), int(cap.get(4)))
    )

    # ===== INITIALISE SYSTEM =====
    detector = Detector()
    spatial = SpatialAnalyzer()
    risk_engine = RiskEngine()
    guidance_system = GuidanceSystem()

    print("System initialised. Processing video...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detection
        detections = detector.detect(frame)

        # Spatial
        spatial_data = spatial.analyze(detections, frame)

        # Risk
        prioritised_risk = risk_engine.evaluate(spatial_data)

        if prioritised_risk:
            top = prioritised_risk
            guidance = guidance_system.generate(top)

            # Overlay text
            cv2.putText(frame,
                        f"Top Risk: {top['object']} {top['distance']} {top['direction']}",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2)

            cv2.putText(frame,
                        f"GUIDANCE: {guidance}",
                        (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 255),
                        2)

        # Draw bounding boxes
        for obj in detections:
            x1, y1, x2, y2 = obj["bbox"]
            label = obj["object"]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame,
                        label,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0,255,0),
                        2)

        out.write(frame)

    cap.release()
    out.release()

    print("Video processing complete.")
    print("Saved as output_demo.mp4")

if __name__ == "__main__":
    main()

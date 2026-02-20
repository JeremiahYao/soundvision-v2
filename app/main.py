import cv2
from detector import Detector
from spatial import SpatialAnalyzer
from risk_engine import RiskEngine
from guidance import GuidanceSystem


def main():

    print("Starting SoundVision V2 Video Mode...")

    # ===== CHANGE THIS TO YOUR VIDEO PATH =====
    video_path = "/content/drive/MyDrive/demo_video.mp4"
    # Example if not using Drive:
    # video_path = "demo_video.mp4"

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("ERROR: Could not open video.")
        return

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps == 0:
        fps = 20.0  # fallback if FPS not detected

    # ===== Output Video =====
    output_path = "/content/drive/MyDrive/output_demo.mp4"
    # If not using Drive:
    # output_path = "output_demo.mp4"

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # ===== Initialise System =====
    detector = Detector()
    spatial = SpatialAnalyzer()
    risk_engine = RiskEngine()
    guidance_system = GuidanceSystem()

    print("System initialised. Processing video...")

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # -------- Detection --------
        detections = detector.detect(frame)

        # -------- Spatial Analysis --------
        spatial_data = spatial.analyze(detections, frame)

        # -------- Risk Evaluation --------
        top_risk = risk_engine.evaluate(spatial_data)

        # -------- Draw Bounding Boxes --------
        for obj in detections:
            x1, y1, x2, y2 = obj["bbox"]
            label = obj["object"]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame,
                        label,
                        (x1, max(y1 - 10, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        2)

        # -------- Overlay Top Risk + Guidance --------
        if top_risk is not None:

            guidance_text = guidance_system.generate(top_risk)

            # Danger color coding
            if top_risk["risk_score"] >= 15:
                color = (0, 0, 255)       # Red
            elif top_risk["risk_score"] >= 8:
                color = (0, 165, 255)     # Orange
            else:
                color = (0, 255, 0)       # Green

            # Top risk line
            cv2.putText(frame,
                        f"Top Risk: {top_risk['object']} {top_risk['distance']} {top_risk['direction']}",
                        (30, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        color,
                        2)

            # Guidance line
            cv2.putText(frame,
                        f"GUIDANCE: {guidance_text}",
                        (30, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (255, 255, 255),
                        2)

        # -------- Write Frame --------
        out.write(frame)

    cap.release()
    out.release()

    print("Video processing complete.")
    print(f"Saved as: {output_path}")


if __name__ == "__main__":
    main()

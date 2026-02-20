import cv2
from detector import Detector
from spatial import SpatialAnalyzer
from risk_engine import RiskEngine


def main():
    print("Starting SoundVision V2...")

    # Load test image (for Colab)
    image_path = "test.jpg"
    frame = cv2.imread(image_path)

    if frame is None:
        print("ERROR: Could not load image. Upload test.jpg")
        return

    print("Image loaded successfully.")

    # Initialize modules
    detector = Detector()
    spatial = SpatialAnalyzer()
    risk_engine = RiskEngine()

    print("Running YOLO detection...")
    detections = detector.detect(frame)

    print("Running spatial analysis...")
    spatial_data = spatial.analyze(detections, frame)

    print("Evaluating prioritised risk...")
    prioritised_risk = risk_engine.evaluate(spatial_data)

    print("\n--- PRIORITISED DECISION ---")

    if prioritised_risk:
        print("Top Risk:", prioritised_risk)

        direction = prioritised_risk["direction"]
        obj = prioritised_risk["object"]
        distance = prioritised_risk["distance"]

        print(f"ALERT: Warning: {obj} {distance} on your {direction}")
    else:
        print("No significant threats detected.")

    print("SoundVision V2 completed successfully.")


if __name__ == "__main__":
    main()

import cv2
from detector import Detector
from spatial import SpatialAnalyzer
from risk_engine import RiskEngine


def main():
    print("Starting SoundVision V2...")

    # ===== LOAD IMAGE (Colab Testing) =====
    image_path = "test.jpg"  # Make sure you upload this file
    frame = cv2.imread(image_path)

    if frame is None:
        print("ERROR: Could not load image. Upload test.jpg")
        return

    print("Image loaded successfully.")

    # ===== INITIALISE MODULES =====
    detector = Detector()
    spatial = SpatialAnalyzer()
    risk_engine = RiskEngine()

    # ===== PIPELINE =====
    print("Running YOLO detection...")
    detections = detector.detect(frame)

    print("Running spatial analysis...")
    spatial_data = spatial.analyze(detections, frame)

    print("Evaluating prioritised risk...")
    risk_output = risk_engine.evaluate(spatial_data)

    # ===== FINAL DECISION OUTPUT =====
    print("\n--- PRIORITISED DECISION ---")
    print("Top Risk:", risk_output["top_risk"])

    if risk_output["alert"]:
        print("ALERT:", risk_output["message"])
    else:
        print("STATUS:", risk_output["message"])

    print("\nSoundVision V2 completed successfully.")


if __name__ == "__main__":
    main()

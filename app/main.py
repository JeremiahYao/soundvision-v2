import cv2
from detector import Detector
from spatial import SpatialAnalyzer
from risk_engine import RiskEngine
from guidance import GuidanceSystem

def main():
    print("Starting SoundVision V2...")

    # =========================
    # Load test image (Colab mode)
    # =========================
    image_path = "test.jpg"
    frame = cv2.imread(image_path)

    if frame is None:
        print("ERROR: Could not load image. Upload test.jpg")
        return

    print("Image loaded successfully.")

    # =========================
    # Initialize systems
    # =========================
    detector = Detector()
    spatial = SpatialAnalyzer()
    risk_engine = RiskEngine()
    guidance = GuidanceSystem()
    
    print("Running YOLO detection...")
    detections = detector.detect(frame)

    print("Running spatial analysis...")
    spatial_data = spatial.analyze(detections, frame)

    print("Evaluating prioritised risk...")
    prioritised_risks = risk_engine.evaluate(spatial_data)

    print("\n--- PRIORITISED DECISION ---")

    if not prioritised_risks:
        print("No threats detected.")
        return

    # ✅ FIX: get highest priority object
    top_risk = prioritised_risks[0]

    print("Top Risk:", top_risk)

    obj = top_risk["object"]
    distance = top_risk["distance"]
    direction = top_risk["direction"]
    score = top_risk["risk_score"]

    print(f"ALERT: Warning: {obj} {distance} {direction}")
    print("SoundVision V2 completed successfully.")

    instruction = guidance.generate(top_risk)

    print("GUIDANCE:", instruction)

if __name__ == "__main__":
    main()

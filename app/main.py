import cv2
from detector import Detector
from spatial import SpatialAnalyzer
from risk_engine import RiskEngine

def main():
    print("Starting SoundVision V2...")

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

    # Run detection
    print("Running YOLO detection...")
    detections = detector.detect(frame)
    print("Detections:", detections)

    # Spatial analysis
    print("Running spatial analysis...")
    spatial_data = spatial.analyze(detections, frame)
    print("Spatial data:", spatial_data)

    # Risk evaluation
    print("Evaluating risk...")
    risk_result = risk_engine.evaluate(spatial_data)

    print("\nFINAL RISK ANALYSIS:")
    for obj in risk_result:
        print(obj)

    print("\nSoundVision V2 completed successfully.")

if __name__ == "__main__":
    main()

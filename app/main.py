import cv2
from detector import Detector
from spatial import SpatialAnalyzer
from risk_engine import RiskEngine
from audio import AudioSystem

def main():
    print("Starting SoundVision V2...")

    cap = cv2.VideoCapture(0)
    print("Camera initialized")

    detector = Detector()
    spatial = SpatialAnalyzer()
    risk_engine = RiskEngine()
    audio = AudioSystem()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.detect(frame)
        spatial_data = spatial.analyze(detections, frame)
        risk_result = risk_engine.evaluate(spatial_data)

        print("RISK ANALYSIS:", risk_result)
        audio.announce(risk_result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

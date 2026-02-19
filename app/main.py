import time
from camera import Camera
from detector import Detector
from spatial import SpatialAnalyzer
from risk_engine import RiskEngine
from audio import AudioOutput


def main():
    print("Starting SoundVision V2...")

    camera = Camera()
    detector = Detector()
    spatial = SpatialAnalyzer()
    risk_engine = RiskEngine()
    audio = AudioOutput()

    for _ in range(1): 
        frame = camera.get_frame()
        if frame is None:
            continue

        detections = detector.detect(frame)
        spatial_data = spatial.analyze(detections, frame)
        risk_result = risk_engine.evaluate(spatial_data)

        if risk_result["speak"]:
            audio.speak(risk_result["message"])

        time.sleep(0.5)  # ← ADD THIS (2 alerts per second max)


if __name__ == "__main__":
    main()

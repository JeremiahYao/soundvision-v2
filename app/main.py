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

    while True:
        frame = camera.get_frame()
        if frame is None:
            continue

        detections = detector.detect(frame)
        spatial_data = spatial.analyze(detections)
        risk_result = risk_engine.evaluate(spatial_data)

        if risk_result["speak"]:
            audio.speak(risk_result["message"])


if __name__ == "__main__":
    main()


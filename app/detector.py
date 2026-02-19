class Detector:
    def __init__(self):
        print("Detector initialized")

    def detect(self, frame):
        # Temporary fake detection
        return [{"object": "person", "distance": "near", "moving": True}]


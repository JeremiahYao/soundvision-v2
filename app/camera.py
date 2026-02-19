import cv2

class Camera:
    def __init__(self):
        print("Camera initialized")
        self.image_path = "/content/test.jpg"

    def get_frame(self):
        frame = cv2.imread(self.image_path)
        return frame

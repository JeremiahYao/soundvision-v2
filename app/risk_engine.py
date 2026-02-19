import time


class RiskEngine:
    def __init__(self):
        print("Risk Engine initialized")
        self.last_objects = set()
        self.last_time_spoken = 0
        self.cooldown = 5  # seconds

    def evaluate(self, spatial_data):
        current_time = time.time()

        current_objects = set()

        for obj in spatial_data:
            if obj["object"] in ["person", "car", "bus", "truck"] and obj["distance"] == "near":
                current_objects.add(obj["object"])

        # Only speak if:
        # 1. New dangerous object appears
        # 2. Or cooldown expired AND object still present

        if current_objects:
            if current_objects != self.last_objects or \
               (current_time - self.last_time_spoken > self.cooldown):

                self.last_objects = current_objects
                self.last_time_spoken = current_time

                message = ", ".join(current_objects) + " nearby"
                return {"speak": True, "message": message}

        return {"speak": False, "message": ""}

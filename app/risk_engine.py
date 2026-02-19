import time

class RiskEngine:
    def __init__(self):
        print("Risk Engine initialized")
        self.last_message = None
        self.last_time_spoken = 0
        self.cooldown = 3

    def evaluate(self, spatial_data):
        current_time = time.time()

        for obj in spatial_data:
            if obj["object"] == "person" and obj["distance"] == "near":
                message = "Person very close"


                if (message != self.last_message) or \
                   (current_time - self.last_time_spoken > self.cooldown):

                    self.last_message = message
                    self.last_time_spoken = current_time

                    return {
                        "speak": True,
                        "message": message
                    }

        return {"speak": False, "message": ""}

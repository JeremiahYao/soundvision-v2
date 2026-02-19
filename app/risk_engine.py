class RiskEngine:
    def __init__(self):
        print("Risk Engine initialized")

    def evaluate(self, spatial_data):
        for obj in spatial_data:
            if obj["object"] == "person" and obj["distance"] == "near":
                return {
                    "speak": True,
                    "message": "Person ahead"
                }

        return {"speak": False, "message": ""}


class RiskEngine:
    def __init__(self):
        print("Risk Engine initialized")

        self.base_risk = {
            "person": 2,
            "car": 6,
            "truck": 8,
            "bus": 8,
            "motorbike": 7,
            "bicycle": 4
        }

        self.distance_multiplier = {
            "near": 3,
            "medium": 2,
            "far": 1
        }

    def evaluate(self, spatial_data):
        results = []

        for obj in spatial_data:
            base = self.base_risk.get(obj["object"], 1)
            multiplier = self.distance_multiplier[obj["distance"]]
            score = base * multiplier

            results.append({
                "object": obj["object"],
                "distance": obj["distance"],
                "risk_score": score
            })

        return results

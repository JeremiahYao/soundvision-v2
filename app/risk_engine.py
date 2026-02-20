class RiskEngine:
    def __init__(self):
        print("Risk Engine initialized")

        # Base danger weights
        self.base_risk = {
            "person": 2,
            "bicycle": 4,
            "motorcycle": 6,
            "car": 7,
            "bus": 8,
            "truck": 9,
        }

        # Distance multipliers
        self.distance_multiplier = {
            "near": 3,
            "medium": 2,
            "far": 1
        }

        # Minimum score required to trigger warning
        self.alert_threshold = 8


    def evaluate(self, spatial_data):

        if not spatial_data:
            return {
                "alert": False,
                "message": "Path appears safe",
                "top_risk": None
            }

        scored = []

        for obj in spatial_data:

            base = self.base_risk.get(obj["object"], 1)
            multiplier = self.distance_multiplier.get(obj["distance"], 1)

            score = base * multiplier

            scored.append({
                "object": obj["object"],
                "distance": obj["distance"],
                "risk_score": score
            })

        # Sort highest first
        scored.sort(key=lambda x: x["risk_score"], reverse=True)

        top = scored[0]

        # Decision logic
        if top["risk_score"] >= self.alert_threshold:

            message = f"Warning: {top['object']} {top['distance']} ahead"

            return {
                "alert": True,
                "message": message,
                "top_risk": top,
                "all_risks": scored
            }

        else:
            return {
                "alert": False,
                "message": "Path appears safe",
                "top_risk": top,
                "all_risks": scored
            }

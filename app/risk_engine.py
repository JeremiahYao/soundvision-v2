class RiskEngine:

    def __init__(self):
        print("Risk Engine initialized")

    def evaluate(self, spatial_data):

        if not spatial_data:
            return None

        risk_list = []

        for obj in spatial_data:

            base_risk = {
                "person": 2,
                "car": 6,
                "truck": 8,
                "bus": 8,
                "motorbike": 7,
                "bicycle": 5
            }.get(obj["object"], 1)

            distance_multiplier = {
                "near": 3,
                "medium": 2,
                "far": 1
            }.get(obj["distance"], 1)

            risk_score = base_risk * distance_multiplier

            risk_list.append({
                "object": obj["object"],
                "distance": obj["distance"],
                "direction": obj["direction"],
                "risk_score": risk_score
            })

        # Sort highest risk first
        risk_list.sort(key=lambda x: x["risk_score"], reverse=True)

        # Return ONLY the highest risk
        return risk_list[0]

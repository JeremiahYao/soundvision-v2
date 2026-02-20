class RiskEngine:
    def __init__(self):
        print("Risk Engine initialized")

    def evaluate(self, spatial_data):
        risk_results = []

        base_risk = {
            "person": 2,
            "car": 6,
            "truck": 8,
            "motorcycle": 7,
            "bicycle": 4
        }

        for obj in spatial_data:
            object_type = obj["object"]
            distance = obj["distance"]

            risk_score = base_risk.get(object_type, 1)

            # Increase risk if closer
            if distance == "near":
                risk_score *= 3
            elif distance == "medium":
                risk_score *= 2

            risk_results.append({
                "object": object_type,
                "distance": distance,
                "direction": obj["direction"],
                "risk_score": risk_score
            })

        # Sort by highest risk
        risk_results = sorted(risk_results, key=lambda x: x["risk_score"], reverse=True)

        return risk_results

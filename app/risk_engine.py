class RiskEngine:
    def __init__(self):
        print("Risk Engine initialized")

        # Base object danger weights
        self.object_weights = {
            "person": 2,
            "bicycle": 3,
            "motorcycle": 5,
            "car": 6,
            "bus": 7,
            "truck": 8,
            "traffic light": 1,
            "bench": 1,
            "chair": 1
        }

        # Distance risk scaling
        self.distance_weights = {
            "near": 5,
            "medium": 3,
            "far": 1
        }

        self.cooldown_counter = 0
        self.cooldown_limit = 10


    def evaluate(self, spatial_data):

        if not spatial_data:
            return {"speak": False, "message": None}

        scored_objects = []

        for obj in spatial_data:

            object_type = obj.get("object")
            distance = obj.get("distance")

            if object_type not in self.object_weights:
                continue

            if distance not in self.distance_weights:
                continue

            object_score = self.object_weights[object_type]
            distance_score = self.distance_weights[distance]

            # CORE RISK FORMULA
            risk_score = object_score * distance_score

            scored_objects.append({
                "object": object_type,
                "distance": distance,
                "risk_score": risk_score
            })

        if not scored_objects:
            return {"speak": False, "message": None}

        # Sort highest risk first
        scored_objects.sort(key=lambda x: x["risk_score"], reverse=True)

        highest_risk = scored_objects[0]

        print("RISK ANALYSIS:", scored_objects)

        # Cooldown control
        if self.cooldown_counter < self.cooldown_limit:
            self.cooldown_counter += 1
            return {"speak": False, "message": None}

        self.cooldown_counter = 0

        message = f"Warning: {highest_risk['object']} {highest_risk['distance']}"

        return {
            "speak": True,
            "message": message
        }

class GuidanceSystem:
    def __init__(self):
        print("Guidance System initialized")

    def generate(self, top_risk):
        if not top_risk:
            return "Path is clear."

        obj = top_risk["object"]
        distance = top_risk["distance"]
        direction = top_risk["direction"]

        # --- High Risk Objects ---
        if obj in ["car", "truck", "bus", "motorcycle"]:
            if distance == "near":
                return f"Danger! {obj} very close on your {direction}. Move away immediately."
            elif distance == "medium":
                return f"Caution. {obj} approaching from {direction}."
            else:
                return f"{obj} detected in the distance."

        # --- Pedestrians ---
        if obj == "person":
            if distance == "near":
                return f"Person very close on your {direction}. Adjust slightly."
            else:
                return f"Person ahead."

        # --- Obstacles ---
        if obj in ["chair", "bench", "bag", "handbag"]:
            if distance == "near":
                return f"Obstacle near on your {direction}. Step around."
            else:
                return f"Obstacle detected."

        # --- Default ---
        return f"{obj} detected on your {direction}."

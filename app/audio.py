class AudioSystem:
    def __init__(self):
        print("Audio system initialized")

    def announce(self, risk_results):
        if not risk_results:
            return

        # Sort by risk
        risk_results = sorted(risk_results, key=lambda x: x["risk_score"], reverse=True)

        top = risk_results[0]

        if top["risk_score"] >= 10:
            print(f"AUDIO: WARNING! {top['object']} very close!")
        elif top["risk_score"] >= 6:
            print(f"AUDIO: {top['object']} ahead")

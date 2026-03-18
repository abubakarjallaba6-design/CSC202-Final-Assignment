from datetime import datetime

class Patient:
    def __init__(self, name, ailment):
        self.name = name  # State: attribute [cite: 12]
        self.ailment = ailment # State: attribute [cite: 12]
        # Requirement: Using datetime API for timestamping [cite: 19, 21]
        self.arrival_time = datetime.now().strftime("%H:%M:%S")

    def get_summary(self):
        """Custom behavior method 1 [cite: 14]"""
        return f"Patient {self.name} is seeking treatment for {self.ailment}."

    def get_display_name(self):
        """Custom behavior method 2 [cite: 14]"""
        return f"Patient: {self.name} (Reason: {self.ailment})"

    # --- NEW METHOD FOR PUSH 10 ---
    def is_urgent(self):
        """Custom behavior method 3: Checks for emergency keywords """
        emergencies = ['emergency', 'accident', 'severe', 'critical']
        return any(word in self.ailment.lower() for word in emergencies)

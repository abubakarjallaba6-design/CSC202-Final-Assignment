from datetime import datetime

class Patient:
    def __init__(self, name, ailment):
        self.name = name
        self.ailment = ailment
        self.arrival_time = datetime.now().strftime("%H:%M:%S")

    def get_summary(self):
        return f"Patient {self.name} is seeking treatment for {self.ailment}."

    def get_display_name(self):
        """Returns a formatted string for the UI."""
        return f"Patient: {self.name} (Reason: {self.ailment})"

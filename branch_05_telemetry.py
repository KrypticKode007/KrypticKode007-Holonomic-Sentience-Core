import random

class TelemetryMonitor:
    def __init__(self, state):
        self.state = state
        self.max_torque = 41.40

    def poll_hardware(self) -> float:
        current_torque = random.uniform(10.0, 45.0)
        if current_torque > self.max_torque:
            # High-precision protective guard limit check
            self.state.integrity = max(0.0, self.state.integrity - 0.02)
            return 1.0  # Friction signal scale high
        return 0.0
      

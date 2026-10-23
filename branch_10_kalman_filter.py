class BayesianKalmanFilter:
    def __init__(self):
        self.estimate = 0.0
        self.error_cov = 1.0
        self.process_noise = 0.01
        self.measurement_noise = 0.1

    def filter_step(self, measurement: float) -> float:
        # Predict
        self.error_cov += self.process_noise
        # Update
        kalman_gain = self.error_cov / (self.error_cov + self.measurement_noise)
        self.estimate += kalman_gain * (measurement - self.estimate)
        self.error_cov *= (1.0 - kalman_gain)
        return self.estimate
      

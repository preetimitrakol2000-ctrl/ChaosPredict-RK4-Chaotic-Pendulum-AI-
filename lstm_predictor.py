class ChaosTimeSeriesPredictor:
    def __init__(self):
        # Statistically trained coefficients for chaotic divergence mapping
        self.weights = [0.85, -0.45, 0.20, -0.05, 0.01]
        self.bias = 0.005

    def forecast_next_state(self, rolling_history):
        """
        Calculates time-series matrix dot products across historical queue states:
        y = bias + Sum(w_i * x_i)
        """
        if len(rolling_history) < 5:
            return rolling_history[-1] if rolling_history else 0.0
            
        prediction = self.bias
        for i in range(5):
            prediction += self.weights[i] * rolling_history[i]
            
        return prediction

import numpy as np
import time

class SimpleAnomalyDetector:
    def __init__(self, window_size=10, threshold=2.0):
        self.window_size = window_size
        self.threshold = threshold
        self.window = []

    def check_anomaly(self, value):
        self.window.append(value)
        if len(self.window) > self.window_size:
            self.window.pop(0)

        if len(self.window) < self.window_size:
            return False

        mean = np.mean(self.window)
        std_dev = np.std(self.window)
        if std_dev == 0:
            return False
        
        z_score = (value - mean) / std_dev
        return abs(z_score) > self.threshold

def create_data(size=1):
    return np.random.normal(0, 1, size).tolist()

def display_data_and_anomalies(data_list, anomaly_list, count_anomalies):
    print(f"\nLatest Data Stream (last {len(data_list)} values):")
    print(" ".join(f"{val:5.2f}" for val in data_list[-50:]))  # Print last 50 values for brevity
    print(f"\nAnomalies Found ({count_anomalies}):")
    for index, value in anomaly_list:
        print(f"Anomaly at index {index}: {value:.2f}")

def main_loop():
    detector = SimpleAnomalyDetector(window_size=10, threshold=2.0)
    data_list = []
    anomaly_list = []
    count_anomalies = 0

    try:
        while True:
            new_values = create_data()
            data_list.extend(new_values)

            for value in new_values:
                if detector.check_anomaly(value):
                    index = len(data_list) - 1
                    anomaly_list.append((index, value))
                    count_anomalies += 1

            # Display data and anomalies
            display_data_and_anomalies(data_list, anomaly_list, count_anomalies)
            
            time.sleep(1)  # Simulate real-time data stream, adjust as needed

    except KeyboardInterrupt:
        print("\nProgram stopped.")
        with open('anomalies.txt', 'w') as file:
            for index, value in anomaly_list:
                file.write(f"Anomaly at index {index}: {value}\n")
        print("Anomalies saved to 'anomalies.txt'.")

if __name__ == "__main__":
    main_loop()

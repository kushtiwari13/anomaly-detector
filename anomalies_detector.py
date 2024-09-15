import numpy as np
import time

class SimpleAnomalyDetector:
    def __init__(self, window_size=10, threshold=2.0):
        # Initialize the detector with a window size and threshold for anomaly detection
        self.window_size = window_size
        self.threshold = threshold
        self.window = []  # List to keep track of the recent values

    def check_anomaly(self, value):
        # Add the new value to the list of recent values
        self.window.append(value)
        # If we exceed the window size, remove the oldest value
        if len(self.window) > self.window_size:
            self.window.pop(0)

        # If we do not have enough data yet, we cannot detect anomalies
        if len(self.window) < self.window_size:
            return False

        # Calculate the mean and standard deviation of the recent values
        mean = np.mean(self.window)
        std_dev = np.std(self.window)
        # Avoid division by zero
        if std_dev == 0:
            return False
        
        # Calculate the Z-score to detect anomalies
        z_score = (value - mean) / std_dev
        # Check if the Z-score exceeds the threshold
        return abs(z_score) > self.threshold

def create_data(size=1):
    # Generate random data with a normal distribution
    return np.random.normal(0, 1, size).tolist()

def display_data_and_anomalies(data_list, anomaly_list, count_anomalies):
    # Print the latest values from the data stream
    print(f"\nLatest Data Stream (last {len(data_list)} values):")
    print(" ".join(f"{val:5.2f}" for val in data_list[-50:]))  # Print last 50 values for brevity
    # Print the detected anomalies and their counts
    print(f"\nAnomalies Found ({count_anomalies}):")
    for index, value in anomaly_list:
        print(f"Anomaly at index {index}: {value:.2f}")

def main_loop():
    # Create an instance of the anomaly detector
    detector = SimpleAnomalyDetector(window_size=10, threshold=2.0)
    data_list = []  # List to store the data stream
    anomaly_list = []  # List to store detected anomalies
    count_anomalies = 0  # Counter for the number of anomalies

    try:
        while True:
            # Generate new data values and add them to the data list
            new_values = create_data()
            data_list.extend(new_values)

            # Check each new value for anomalies
            for value in new_values:
                if detector.check_anomaly(value):
                    index = len(data_list) - 1  # Index of the current value
                    anomaly_list.append((index, value))  # Store the anomaly
                    count_anomalies += 1  # Increment the anomaly count

            # Display the current data and anomalies
            display_data_and_anomalies(data_list, anomaly_list, count_anomalies)
            
            # Pause for a short period to simulate real-time data stream
            time.sleep(1)  # Adjust the delay as needed

    except KeyboardInterrupt:
        # Handle the case when the user interrupts the program
        print("\nProgram stopped.")
        # Save the detected anomalies to a text file
        with open('anomalies.txt', 'w') as file:
            for index, value in anomaly_list:
                file.write(f"Anomaly at index {index}: {value}\n")
        print("Anomalies saved to 'anomalies.txt'.")

if __name__ == "__main__":
    main_loop()

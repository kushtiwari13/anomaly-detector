# Anomaly Detector

This project provides a simple anomaly detection tool that processes a data stream and identifies anomalies based on a specified threshold. The script generates data in real-time, detects anomalies, and displays them in the console. Detected anomalies are also saved to a text file.

## Setup Instructions

Follow the steps below to set up and run the anomaly detection script:

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   "git clone <repository-url>"

   Replace `<repository-url>` with the actual URL of the repository.

2. **Create and Activate a Virtual Environment**

   Navigate to the project directory and create a virtual environment using the following command:

   "python -m venv venv"

   Activate the virtual environment:

   - On Windows:
     "venv\Scripts\activate"

   - On macOS/Linux:
     "source venv/bin/activate"

3. **Install Dependencies**

   Install the required dependencies listed in the `requirements.txt` file:

   "pip install -r requirements.txt"

4. **Run the Script**

   Execute the anomaly detection script with the following command:

   "python anomalies_detector.py"

### Stopping the Script

To stop the script, press `Ctrl + C` in the terminal. The script will save any detected anomalies to `anomalies.txt`.

## File Descriptions

- **anomalies_detector.py**: The main Python script that generates data, detects anomalies, and prints results to the console.
- **requirements.txt**: A file listing the Python packages required to run the script.
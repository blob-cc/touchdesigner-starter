import json
import csv
import os
import numpy as np

# Configuration
DATA_SOURCE = "data/input_data.json"  # Path to the input data file (could be a JSON, CSV, etc.)
PROCESSED_DATA_DIR = "data/processed"  # Directory to save processed data
OUTPUT_FILE = "processed_data.npy"  # Filename for processed data

# Ensure the processed data directory exists
if not os.path.exists(PROCESSED_DATA_DIR):
    os.makedirs(PROCESSED_DATA_DIR)

# Function to read JSON data
def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Function to read CSV data
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return np.array(data, dtype=float)

# Function to normalize data (scales data to a 0-1 range)
def normalize_data(data):
    min_val = np.min(data)
    max_val = np.max(data)
    return (data - min_val) / (max_val - min_val)

# Function to process data
def process_data(data):
    # Example: Normalize data and apply a smoothing filter
    normalized_data = normalize_data(data)
    smoothed_data = np.convolve(normalized_data, np.ones(5)/5, mode='valid')  # Simple moving average
    return smoothed_data

# Function to save processed data
def save_processed_data(data, output_dir, output_file):
    output_path = os.path.join(output_dir, output_file)
    np.save(output_path, data)
    print(f"Processed data saved to {output_path}")

# Main function to read, process, and save data
def main():
    if DATA_SOURCE.endswith('.json'):
        data = read_json(DATA_SOURCE)
        data = np.array(data['values'], dtype=float)  # Assuming JSON structure has a 'values' key
    elif DATA_SOURCE.endswith('.csv'):
        data = read_csv(DATA_SOURCE)
    else:
        raise ValueError("Unsupported data source format. Please use JSON or CSV.")

    processed_data = process_data(data)
    save_processed_data(processed_data, PROCESSED_DATA_DIR, OUTPUT_FILE)

if __name__ == "__main__":
    main()
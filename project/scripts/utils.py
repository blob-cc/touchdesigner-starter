import os
import json
import csv
import numpy as np
from datetime import datetime

# Utility to check if a directory exists and create it if not
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
    else:
        print(f"Directory already exists: {directory}")

# Utility to read a JSON file
def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    print(f"Loaded JSON data from {file_path}")
    return data

# Utility to write data to a JSON file
def write_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Saved JSON data to {file_path}")

# Utility to read a CSV file
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    print(f"Loaded CSV data from {file_path}")
    return np.array(data, dtype=float)

# Utility to write data to a CSV file
def write_csv(data, file_path):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"Saved CSV data to {file_path}")

# Utility to normalize an array (0-1 range)
def normalize_array(data):
    min_val = np.min(data)
    max_val = np.max(data)
    normalized_data = (data - min_val) / (max_val - min_val)
    print(f"Normalized array with min={min_val}, max={max_val}")
    return normalized_data

# Utility to apply a moving average to an array
def moving_average(data, window_size):
    cumsum = np.cumsum(np.insert(data, 0, 0)) 
    ma = (cumsum[window_size:] - cumsum[:-window_size]) / window_size
    print(f"Applied moving average with window size={window_size}")
    return ma

# Utility to generate a timestamped filename
def generate_timestamped_filename(base_name, extension):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{base_name}_{timestamp}.{extension}"
    print(f"Generated timestamped filename: {filename}")
    return filename

# Utility to log messages to a file
def log_message(message, log_file):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as log:
        log.write(f"[{timestamp}] {message}\n")
    print(message)

# Utility to scale a value from one range to another
def scale_value(value, from_range, to_range):
    (from_min, from_max) = from_range
    (to_min, to_max) = to_range
    scaled_value = ((value - from_min) / (from_max - from_min)) * (to_max - to_min) + to_min
    print(f"Scaled value {value} from range {from_range} to {to_range}: {scaled_value}")
    return scaled_value

# Utility to find the nearest value in an array
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    nearest_value = array[idx]
    print(f"Nearest value to {value} in array is {nearest_value}")
    return nearest_value

# Utility to safely load and return content from a file (text-based)
def safe_read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        print(f"Successfully read file: {file_path}")
        return content
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None
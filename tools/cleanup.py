import os
import shutil

# Configuration
PROJECT_DIR = "project"  # The main project directory where your .toe file and assets are stored
TEMP_DIRS = ["cache", "temp", "backup"]  # Directories commonly used for temporary files
TEMP_EXTENSIONS = [".tmp", ".bak", ".log", ".swp"]  # File extensions to clean up

# Function to delete files with specific extensions
def delete_temp_files(directory, extensions):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                filepath = os.path.join(root, file)
                try:
                    os.remove(filepath)
                    print(f"Deleted: {filepath}")
                except Exception as e:
                    print(f"Error deleting {filepath}: {e}")

# Function to delete temporary directories
def delete_temp_dirs(directory, temp_dirs):
    for temp_dir in temp_dirs:
        temp_path = os.path.join(directory, temp_dir)
        if os.path.exists(temp_path):
            try:
                shutil.rmtree(temp_path)
                print(f"Deleted directory: {temp_path}")
            except Exception as e:
                print(f"Error deleting directory {temp_path}: {e}")

# Cleanup process
def clean_project(project_dir, temp_dirs, temp_extensions):
    print("Starting cleanup...")
    delete_temp_dirs(project_dir, temp_dirs)
    delete_temp_files(project_dir, temp_extensions)
    print("Cleanup completed successfully!")

# Run cleanup
clean_project(PROJECT_DIR, TEMP_DIRS, TEMP_EXTENSIONS)
import os
import shutil
import zipfile
import datetime

# Configuration
PROJECT_NAME = "TouchDesignerProject"
OUTPUT_DIR = "dist"
BUILD_DIR = "build"
SOURCE_DIR = "project"
EXTRA_FILES = ["README.md", "LICENSE"]

# Ensure the output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Clear previous build
if os.path.exists(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)
os.makedirs(BUILD_DIR)

# Copy source files to the build directory
shutil.copytree(SOURCE_DIR, os.path.join(BUILD_DIR, PROJECT_NAME))

# Copy extra files (README, LICENSE, etc.)
for file in EXTRA_FILES:
    shutil.copy(file, BUILD_DIR)

# Create a zip file of the build directory
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
zip_filename = f"{PROJECT_NAME}_{timestamp}.zip"
zip_filepath = os.path.join(OUTPUT_DIR, zip_filename)

with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(BUILD_DIR):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, BUILD_DIR)
            zipf.write(filepath, arcname)

# Cleanup the build directory after packaging
shutil.rmtree(BUILD_DIR)

print(f"Build completed successfully! Package saved as {zip_filepath}")
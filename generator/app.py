import os
import shutil
import argparse

# Predefined paths for source and destination directories
source_dir = r"C:\Users\Zaid\Desktop\app"  # Use raw string to avoid escape sequences
destination_dir = r"C:\Users\Zaid\Desktop\backup"  # Destination path

def transfer_folder():
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return
    
    # Check if destination directory already exists, if so remove it (optional)
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)  # Deletes destination if it exists
        print(f"Removed existing destination directory {destination_dir}.")

    # Copy entire folder from source to destination
    shutil.copytree(source_dir, destination_dir)
    print(f"Folder {source_dir} transferred to {destination_dir}")

if __name__ == "__main__":
    # Optional CLI usage if needed later (currently no arguments are used)
    parser = argparse.ArgumentParser(description='Transfer folder from source to destination.')
    args = parser.parse_args()

    # Call the function to transfer folder
    transfer_folder()

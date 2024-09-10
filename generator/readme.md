# Folder Creation "as is" from one directory to another

This Python script is designed to transfer a folder (including all its files and subdirectories) from a predefined source directory to a predefined destination directory. The source and destination paths are hardcoded in the script and must be edited before running the script.

## Features

- Transfers all files and subdirectories from a source folder to a destination folder.
- Automatically removes the destination folder if it exists, to ensure a clean copy.
- Uses Python’s `shutil` module for high-level file operations.

## Prerequisites

- **Python**: Make sure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).

## Setup and Configuration

1. Clone or download this repository.
2. Modify the following lines in the script to set the source and destination directories:

   ```python
   source_dir = r"C:\path\to\your\source\directory"
   destination_dir = r"C:\path\to\your\destination\directory"

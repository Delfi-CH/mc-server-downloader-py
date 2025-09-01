#!/bin/bash

# Exit on any error
set -e

# Name of the virtual environment directory
VENV_DIR=".venv"

echo "Creating virtual environment..."
python3 -m venv "$VENV_DIR"

echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "Installing requirements from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Running PyInstaller on main.py..."
pyinstaller --clean --onefile main.py --name mcsvdl

echo "Done!"

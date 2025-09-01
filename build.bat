@echo off
setlocal

REM Name of the virtual environment folder
set VENV_DIR=.venv

echo Creating virtual environment...
python -m venv %VENV_DIR%

echo Activating virtual environment...
call %VENV_DIR%\Scripts\activate.bat

echo Installing requirements...
pip install --upgrade pip
pip install -r requirements.txt

echo Running PyInstaller on main.py...
pyinstaller --clean --onefile main.py --name mcsvdl.exe

echo Done!
endlocal
pause

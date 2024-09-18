@echo off

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate
REM Install requirements if requirements.txt exists
pip install -r requirements.txt
echo Requirements installed successfully.


echo Virtual environment created and activated successfully.
echo To deactivate the virtual environment, run 'deactivate'.

# Virtual Environment Setup

This project includes a shell script to create and set up a virtual environment for Python projects. The script works on Windows, Linux, and macOS.

## Prerequisites

- Python 3
- pip (usually comes with Python 3)

## Usage

1. Save the shell script as `create_venv.sh` in your project directory.

2. Make the script executable (Linux and macOS only):
   ```
   chmod +x create_venv.sh
   ```

3. Run the script:
   - On Linux and macOS:
     ```
     ./create_venv.sh
     ```
   - On Windows (using Git Bash or similar):
     ```
     sh create_venv.sh
     ```

The script will create a virtual environment, activate it, upgrade pip, and install any requirements listed in `requirements.txt` if the file exists.

## Activating the Virtual Environment

After running the script, the virtual environment will be activated automatically. For future use, activate the virtual environment manually:

- On Linux and macOS:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  venv\Scripts\activate
  ```

You'll know the virtual environment is activated when you see `(venv)` at the beginning of your command prompt.

## Installing Packages from requirements.txt

If you have a `requirements.txt` file in your project directory, the script will automatically install the listed packages. If you need to install them manually or update the packages, use:

```
pip install -r requirements.txt
```

Make sure the virtual environment is activated before running this command.

## Deactivating the Virtual Environment

To deactivate the virtual environment, simply run:

```
deactivate
```

This command works the same on all operating systems.

## Notes

- The virtual environment directory (`venv`) is typically excluded from version control. Make sure to add it to your `.gitignore` file if you're using Git.
- Always activate the virtual environment before working on your project to ensure you're using the correct package versions.

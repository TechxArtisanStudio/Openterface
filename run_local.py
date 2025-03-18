import subprocess
import os

def run_mkdocs():
    try:
        # Activate the virtual environment
        # venv_path = os.path.expanduser("<venv_path>/bin/activate")
        # command = f"source {venv_path} && mkdocs serve -a 0.0.0.0:8002"
        command = f"mkdocs serve -a 0.0.0.0:8002"
        
        # Run mkdocs using the activated virtual environment
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_mkdocs()

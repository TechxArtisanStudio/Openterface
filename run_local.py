import subprocess
import os
import webbrowser
import threading
import time

def open_browser():
    time.sleep(6)
    webbrowser.open('http://localhost:8002')

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
    # Start browser opening in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Run mkdocs in main thread
    run_mkdocs()

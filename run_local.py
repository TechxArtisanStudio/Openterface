import subprocess

def run_mkdocs():
    try:
        # Path to the Python binary in the virtual environment
        python_path = "/home/project/openterface/website/mkdocs-venv/bin/python"
        
        # Run mkdocs using the Python binary in the virtual environment
        subprocess.run([python_path, "-m", "mkdocs", "serve", "-a", "0.0.0.0:8002"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_mkdocs()

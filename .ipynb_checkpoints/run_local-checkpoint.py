import subprocess

def run_mkdocs():
    try:
        # Running the mkdocs serve command
        subprocess.run(["mkdocs", "serve", "-a", "0.0.0.0:8002"])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_mkdocs()

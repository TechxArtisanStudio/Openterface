import subprocess
import re

def get_local_ip():
    try:
        result = subprocess.run("ifconfig", capture_output=True, text=True)
        lines = result.stdout.split('\n')
        ip_lines = [line for line in lines if '192' in line]

        ip_address = None
        for line in ip_lines:
            match = re.search(r'192\.168\.\d+\.\d+', line)
            if match:
                ip_address = match.group(0)
                break

        if ip_address is None:
            ip_address = "localhost"

    except Exception as e:
        print(f"Error occurred: {e}")
        ip_address = "localhost"

    return ip_address

def serve_mkdocs(ip_address, port):
    try:
        # Directly use Python inside the virtual environment
        python_path = "/home/project/openterface/website/mkdocs-venv/bin/python"

        # Run mkdocs using the virtual environment’s Python binary
        subprocess.run([python_path, "-m", "mkdocs", "serve", "-a", f"{ip_address}:{port}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ip_address = get_local_ip()
    port = "8003"
    print(f"Serving MkDocs on http://{ip_address}:{port}")
    serve_mkdocs(ip_address, port)

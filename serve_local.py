import subprocess
import re

def get_local_ip():
    try:
        # Execute 'ifconfig' and then filter with 'grep' for lines containing '192'
        result = subprocess.run("ifconfig", capture_output=True, text=True)
        lines = result.stdout.split('\n')
        ip_lines = [line for line in lines if '192' in line]

        # Use a regular expression to find the first occurrence of an IP address in the output
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
    command = f"mkdocs serve -a {ip_address}:{port}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    ip_address = get_local_ip()
    port = "8003"
    print(f"Serving MkDocs on http://{ip_address}:{port}")
    serve_mkdocs(ip_address, port)

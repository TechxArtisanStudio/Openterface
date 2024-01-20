import socket
import subprocess

def get_local_ip():
    # Attempt to connect to an external host to determine the local IP
    try:
        with socket.create_connection(("8.8.8.8", 53)) as s:
            ip_address = s.getsockname()[0]
    except OSError:
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
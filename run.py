import socket
import os

def get_ip():
    try:
        # Create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to an address
        s.connect(("8.8.8.8", 80))
        # Get the socket's own address
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print(f"Error obtaining IP address: {e}")
        return "127.0.0.1"

if __name__ == "__main__":
    ip_address = get_ip()
    port = "9001"
    print(f"Current IP: {ip_address}:{port}")

    # Run MkDocs serve with the obtained IP address
    os.system(f"mkdocs serve -a {ip_address}:{port}")
import socket

open_ports = []
closed_ports = []
filtered_ports = []

def scan(ip, start_port, end_port, timeout):
    open_ports.clear()
    closed_ports.clear()
    filtered_ports.clear()

    print(f"\nScanning {ip}")
    print(f"Ports: {start_port}-{end_port}")
    print(f"Timeout: {timeout}s\n")

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((ip, port))

                open_ports.append(port)
                print(f"[OPEN]   Port {port}")

        except ConnectionRefusedError:
            closed_ports.append(port)
            print(f"[CLOSED] Port {port}")

        except socket.timeout:
            filtered_ports.append(port)
            print(f"[TIMEOUT] Port {port}")

        except OSError as e:
            print(f"[ERROR]  Port {port}: {e}")

if __name__ == '__main__':
    host = input("Enter IP or website: ")

    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Error: Could not resolve hostname.")
        raise SystemExit(1)

    print("\nSelect scan mode:")
    print("1. Quick scan")
    print("2. Robust scan")

    mode = input("Choice (1/2): ")

    if mode == "1":
        timeout = 0.05
    elif mode == "2":
        timeout = 1.0
    else:
        print("Invalid scan mode.")
        raise SystemExit(1)

    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        if not (1 <= start_port <= 65535):
            print("Invalid starting port.")
            raise SystemExit(1)

        if not (1 <= end_port <= 65535):
            print("Invalid ending port.")
            raise SystemExit(1)

        if start_port > end_port:
            print("Starting port must be <= ending port.")
            raise SystemExit(1)

    except ValueError:
        print("Please enter a whole number between 1 and 65535.")
        raise SystemExit(1)

    scan(ip, start_port, end_port, timeout)
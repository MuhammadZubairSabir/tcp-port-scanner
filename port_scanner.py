import socket
import threading
from datetime import datetime

# --------- CONFIG ---------
TIMEOUT = 1
LOG_FILE = "scan_results.txt"

# --------- FUNCTIONS ---------

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        result = s.connect_ex((host, port))
        s.close()

        if result == 0:
            return "OPEN"
        else:
            return "CLOSED"

    except socket.timeout:
        return "TIMEOUT"
    except Exception as e:
        return f"ERROR: {e}"

def log_result(text):
    with open(LOG_FILE, "a") as file:
        file.write(text + "\n")

def thread_scan(host, port):
    status = scan_port(host, port)
    result = f"Port {port}: {status}"
    print(result)
    log_result(result)

# --------- MAIN PROGRAM ---------

def main():
    print("=" * 50)
    print("      TCP PORT SCANNER - Project 1")
    print("=" * 50)

    host = input("Enter target host (IP / Domain): ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print("\nScanning started at:", datetime.now())
    print(f"Target: {host}")
    print(f"Port Range: {start_port} - {end_port}\n")

    log_result("=" * 50)
    log_result(f"Scan started at: {datetime.now()}")
    log_result(f"Target: {host}")
    log_result(f"Port Range: {start_port} - {end_port}")
    log_result("=" * 50)

    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=thread_scan, args=(host, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nScan completed at:", datetime.now())
    log_result(f"\nScan completed at: {datetime.now()}\n")

# --------- RUN ---------
if __name__ == "__main__":
    main()


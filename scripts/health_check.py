import subprocess
import psutil
from datetime import datetime
from pathlib import Path


def check_service(service_name):
    result = subprocess.run(
        ["systemctl", "is-active", service_name],
        capture_output=True,
        text=True
    )

    return result.stdout.strip() == "active"


def check_cpu():
    return psutil.cpu_percent(interval=1)


def check_memory():
    return psutil.virtual_memory().percent


def check_disk():
    return psutil.disk_usage("/").percent


def check_threshold(value, warning_threshold=80, critical_threshold=90):
    if value >= critical_threshold:
        return "CRITICAL"
    if value >= warning_threshold:
        return "WARNING"
    return "OK"

def write_log(status, details=""):
    log_file = Path(__file__).resolve().parent.parent / "logs" / "health_check.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if details:
        message = f"{status} | {details}"
    else:
        message = status

    with open(log_file, "a") as file:
        file.write(f"{timestamp} | {message}\n")

def main():
    services = {
        "SSH": "ssh",
        "DNS": "bind9",
        "DHCP": "isc-dhcp-server",
    }

    print("=== NexaTech Server Health Check ===")
    print()

    cpu = check_cpu()
    memory = check_memory()
    disk = check_disk()


    cpu_status = check_threshold(cpu, 80)
    memory_status = check_threshold(memory, 80)
    disk_status = check_threshold(disk, 80)

    print(f"CPU Usage    : {cpu:.1f}% [{cpu_status}]")
    print(f"Memory Usage : {memory:.1f}% [{memory_status}]")
    print(f"Disk Usage   : {disk:.1f}% [{disk_status}]")
    print()

    service_statuses = []
    failed_services = []

    for name, service in services.items():
        is_ok = check_service(service)
        status = "OK" if is_ok else "FAIL"
        service_statuses.append(is_ok)

        if not is_ok:
            failed_services.append(name)

        print(f"{name:<13}: {status}")

    if "CRITICAL" in (cpu_status, memory_status, disk_status):
        print("\nOverall Status: CRITICAL")
        write_log("CRITICAL", "System resource threshold exceeded")
        exit(2)

    if "WARNING" in (cpu_status, memory_status, disk_status):
        print("\nOverall Status: WARNING")
        write_log("WARNING", "System resource warning")
        exit(1)

    if not all(service_statuses):
        details = ", ".join(f"{service} FAIL" for service in failed_services)
        print("\nOverall Status: CRITICAL")
        write_log("CRITICAL", details)
        exit(2)

    print("\nOverall Status: HEALTHY")
    write_log("HEALTHY")
    exit(0)

if __name__ == "__main__":
    main()

import subprocess
import time
from plyer import notification

def is_machine_online(ip_address):
    """
    Checks if the machine with the specified IP address is online.
    """
    try:
        # Pinging the machine
        subprocess.check_output(["ping", "-c", "1", ip_address], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

def monitor_machine(ip_address, interval=60):
    """
    Monitors the specified machine and sends a notification when it comes online.
    """
    while True:
        online = is_machine_online(ip_address)
        if online:
            notification.notify(
                title='Machine Online',
                message=f'The machine with IP {ip_address} is now online.',
                app_name='Network Monitor'
            )
            break
        time.sleep(interval)

if __name__ == "__main__":
    # Specify the IP address of the machine to monitor
    ip_address_to_monitor = "192.168.1.100"
    
    monitor_machine(ip_address_to_monitor)

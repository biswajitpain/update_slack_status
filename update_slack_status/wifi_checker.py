import subprocess
import platform

def get_wifi_name():
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            result = subprocess.check_output(['networksetup', '-getairportnetwork', 'en0']).decode('utf-8')
            return result.split(': ')[1].strip()
        elif system == "Linux":
            result = subprocess.check_output(['iwgetid', '-r']).decode('utf-8')
            return result.strip()
        elif system == "Windows":
            result = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8')
            for line in result.split('\n'):
                if "SSID" in line and "BSSID" not in line:
                    return line.split(':')[1].strip()
        else:
            print(f"Unsupported operating system: {system}")
    except subprocess.CalledProcessError:
        print(f"Error: Unable to get Wi-Fi information on {system}")
    return None
# Developer: Igor Andjelkovic

import platform
import psutil

class SystemInfo:
    def get_info(self):
        info = []
        info.append(f"OS: {platform.system()} {platform.release()}")
        info.append(f"CPU Cores: {psutil.cpu_count(logical=True)}")
        info.append(f"CPU Usage: {psutil.cpu_percent()}%")
        info.append(f"RAM Total: {round(psutil.virtual_memory().total / 1024**3, 2)} GB")
        info.append(f"RAM Used: {psutil.virtual_memory().percent}%")
        return "\n".join(info)

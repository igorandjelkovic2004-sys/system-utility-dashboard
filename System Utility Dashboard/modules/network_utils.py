# Developer: Igor Andjelkovic

import subprocess
import requests

class NetworkUtils:
    def ping(self, host):
        try:
            output = subprocess.check_output(["ping", "-c", "4", host]).decode()
            return output
        except Exception:
            return "Ping failed."

    def get_ip(self):
        try:
            return requests.get("https://api.ipify.org").text
        except:
            return "Failed to get IP."

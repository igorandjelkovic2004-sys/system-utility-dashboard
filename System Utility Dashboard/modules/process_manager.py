# Developer: Igor Andjelkovic

import psutil

class ProcessManager:
    def get_processes(self):
        processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                processes.append(f"{proc.info['pid']} - {proc.info['name']}")
            except:
                pass
        return processes

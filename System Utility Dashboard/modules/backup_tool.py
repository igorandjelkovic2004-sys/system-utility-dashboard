# Developer: Igor Andjelkovic

import os
import zipfile
from datetime import datetime

class BackupTool:
    def backup(self, folder):
        if not os.path.exists(folder):
            return "Folder does not exist."

        backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        with zipfile.ZipFile(backup_name, 'w') as zipf:
            for root, _, files in os.walk(folder):
                for f in files:
                    file_path = os.path.join(root, f)
                    zipf.write(file_path)
        return f"Backup created: {backup_name}"

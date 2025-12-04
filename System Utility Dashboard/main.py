# Developer: Igor Andjelkovic
# Project: System Utility Dashboard

import sys
from PyQt5 import QtWidgets, uic
from modules.system_info import SystemInfo
from modules.process_manager import ProcessManager
from modules.backup_tool import BackupTool
from modules.network_utils import NetworkUtils
from modules.log_viewer import LogViewer

class Dashboard(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dashboard.ui", self)

        # Modules
        self.sysinfo = SystemInfo()
        self.procman = ProcessManager()
        self.backup = BackupTool()
        self.network = NetworkUtils()
        self.logviewer = LogViewer()

        # Connect UI
        self.btnRefreshSystem.clicked.connect(self.load_system_info)
        self.btnListProcesses.clicked.connect(self.load_processes)
        self.btnBackup.clicked.connect(self.backup_folder)
        self.btnPing.clicked.connect(self.ping_host)
        self.btnLoadLog.clicked.connect(self.load_log)

        self.load_system_info()

    def load_system_info(self):
        info = self.sysinfo.get_info()
        self.txtSystemInfo.setPlainText(info)

    def load_processes(self):
        processes = self.procman.get_processes()
        self.lstProcesses.clear()
        for p in processes:
            self.lstProcesses.addItem(p)

    def backup_folder(self):
        folder = self.inputBackupFolder.text()
        result = self.backup.backup(folder)
        self.txtBackupResult.setPlainText(result)

    def ping_host(self):
        host = self.inputPing.text()
        result = self.network.ping(host)
        self.txtPingResult.setPlainText(result)

    def load_log(self):
        path = self.inputLogFile.text()
        content = self.logviewer.load(path)
        self.txtLogContent.setPlainText(content)


app = QtWidgets.QApplication(sys.argv)
window = Dashboard()
window.show()
sys.exit(app.exec_())

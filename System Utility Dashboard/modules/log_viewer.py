# Developer: Igor Andjelkovic

class LogViewer:
    def load(self, path):
        try:
            with open(path, "r") as f:
                return f.read()
        except:
            return "Invalid path or file not found."

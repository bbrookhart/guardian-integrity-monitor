import time

class AlertManager:
    def __init__(self, logfile="alerts.log"):
        self.logfile = logfile

    def _write_log(self, message):
        with open(self.logfile, "a") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

    def notify(self, message):
        print(f"[ALERT] {message}")
        self._write_log(message)


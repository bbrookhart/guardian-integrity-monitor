import json
import os
import time
from integrity_core import IntegrityCore
from alerts import AlertManager

class IntegrityMonitor:
    def __init__(self, config):
        self.core = IntegrityCore(config)
        self.alerts = AlertManager()
        self.watch_dirs = config["watch_directories"]
        self.cache = {}

    def initial_index(self):
        for d in self.watch_dirs:
            for root, _, files in os.walk(d):
                for f in files:
                    path = os.path.join(root, f)
                    sig = self.core.hash_file(path)
                    if sig:
                        self.cache[path] = sig
        self.core.log("Initial index completed.")

    def watch(self):
        self.core.log("Monitoring started.")
        while True:
            for path, old_hash in list(self.cache.items()):
                if os.path.exists(path):
                    new_hash = self.core.hash_file(path)
                    if new_hash != old_hash:
                        self.alerts.notify(f"File modified: {path}")
                        self.cache[path] = new_hash
                else:
                    self.alerts.notify(f"File deleted: {path}")
                    del self.cache[path]
            time.sleep(2)
monitor_code

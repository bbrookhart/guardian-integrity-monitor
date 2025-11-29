import os, time
from integrity_core import IntegrityCore

class FileWatcher:
    def __init__(self, config):
        self.core = IntegrityCore(config)
        self.watch_dirs = config['watch_directories']
        self.cache = {}

    def initial_scan(self):
        for d in self.watch_dirs:
            for root, _, files in os.walk(d):
                for f in files:
                    path = os.path.join(root, f)
                    self.cache[path] = self.core.hash_file(path)
        self.core.log("Initial file hash cache built.")

    def watch(self):
        self.core.log("Watching for changes...")
        while True:
            for path, old_hash in list(self.cache.items()):
                if os.path.exists(path):
                    new_hash = self.core.hash_file(path)
                    if new_hash != old_hash:
                        self.core.log(f"ALERT: File modified → {path}")
                        self.cache[path] = new_hash
                else:
                    self.core.log(f"ALERT: File deleted → {path}")
                    del self.cache[path]
            time.sleep(2)

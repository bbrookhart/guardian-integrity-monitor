import os
from guardian.integrity_core import IntegrityCore

class Dashboard:
    def __init__(self, config):
        self.core = IntegrityCore(config)
        self.watch_dirs = config["watch_directories"]

    def list_files(self):
        print("=== Guardian Integrity Dashboard ===")
        for d in self.watch_dirs:
            print(f"\nDirectory: {d}")
            for root, _, files in os.walk(d):
                for f in files:
                    path = os.path.join(root, f)
                    sig = self.core.hash_file(path)
                    print(f"  {path}  |  hash: {sig[:12]}...")

import hashlib
import time

class IntegrityCore:
    def __init__(self, config):
        self.hash_algo = config["hash_algo"]
        self.log_file = config["log_file"]

    def hash_file(self, path):
        h = hashlib.new(self.hash_algo)
        try:
            with open(path, "rb") as f:
                h.update(f.read())
            return h.hexdigest()
        except FileNotFoundError:
            return None

    def log(self, message):
        with open(self.log_file, "a") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

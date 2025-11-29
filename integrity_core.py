import hashlib, json, time

class IntegrityCore:
    def __init__(self, config):
        self.hash_algo = config['hash_algo']
        self.log_file = config['log_file']

    def hash_file(self, path):
        h = hashlib.new(self.hash_algo)
        with open(path, 'rb') as f:
            h.update(f.read())
        return h.hexdigest()

    def log(self, msg):
        with open(self.log_file, 'a') as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")

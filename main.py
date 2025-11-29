import json
from guardian.monitor import IntegrityMonitor

def load_config():
    with open("config.json") as f:
        return json.load(f)

def main():
    config = load_config()

    monitor = IntegrityMonitor(config)
    monitor.initial_index()

    print("Guardian Integrity Monitor initialized.")

if __name__ == "__main__":
    main()
main_code

import argparse, json
from file_watcher import FileWatcher

def load_config():
    with open('config.json') as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scan', action='store_true', help='Run a one-time integrity check')
    parser.add_argument('--watch', action='store_true', help='Monitor directories continuously')
    args = parser.parse_args()

    config = load_config()

    watcher = FileWatcher(config)
    watcher.initial_scan()

    if args.watch:
        watcher.watch()
    else:
        print("Initial scan completed.")

if __name__ == "__main__":
    main()

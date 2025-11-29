import argparse
import json

from guardian.monitor import IntegrityMonitor
from guardian.dashboard import Dashboard
from guardian.gui import IntegrityGUI

def load_config():
    with open("config.json") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--scan", action="store_true", help="Run a one-time integrity check")
    parser.add_argument("--watch", action="store_true", help="Continuously monitor directories")
    parser.add_argument("--dashboard", action="store_true", help="Show console dashboard")
    parser.add_argument("--gui", action="store_true", help="Launch GUI viewer")

    args = parser.parse_args()
    config = load_config()

    monitor = IntegrityMonitor(config)

    monitor.initial_index()

    if args.dashboard:
        Dashboard(config).list_files()

    if args.gui:
        IntegrityGUI(config).launch()

    if args.watch:
        monitor.watch()
    else:
        print("Initial scan completed.")

if __name__ == "__main__":
    main()

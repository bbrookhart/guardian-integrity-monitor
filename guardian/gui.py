<import tkinter as tk
from tkinter import ttk
import os
from integrity_core import IntegrityCore

class IntegrityGUI:
    def __init__(self, config):
        self.core = IntegrityCore(config)
        self.watch_dirs = config["watch_directories"]

        self.window = tk.Tk()
        self.window.title("Guardian Integrity Monitor")
        self.window.geometry("700x400")

        ttk.Label(self.window, text="Monitored Files", font=("Arial", 14)).pack(pady=10)

        self.tree = ttk.Treeview(self.window, columns=("file", "hash"), show="headings")
        self.tree.heading("file", text="File Path")
        self.tree.heading("hash", text="Hash")
        self.tree.pack(fill="both", expand=True)

        self.refresh()

    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for d in self.watch_dirs:
            for root, _, files in os.walk(d):
                for f in files:
                    path = os.path.join(root, f)
                    sig = self.core.hash_file(path)
                    self.tree.insert("", "end", values=(path, sig[:12]))

    def launch(self):
        self.window.mainloop()
>

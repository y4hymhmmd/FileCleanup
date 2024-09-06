import os
import sys
import ctypes
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from typing import List

def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        return False

def write_log(message: str) -> None:
    temp_dir = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp')
    log_path = os.path.join(temp_dir, 'log.txt')
    try:
        with open(log_path, "a") as log_file:
            log_file.write(message + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"Error writing to log: {e}")

def run_commands() -> None:
    commands = [
        'cmd /c rd /s /q "%SystemRoot%\\Temp"',
        'cmd /c rd /s /q "%LocalAppData%\\Temp"',
        'cmd /c rd /s /q "%SystemRoot%\\Prefetch"',
        'cmd /c del /s /q "%LocalAppData%\\NVIDIA\\GLCache\\*"',
        'cmd /c del /s /q "%LocalAppData%\\Low\\NVIDIA\\PerDriverVersion\\DXCache\\*"',
        'cmd /c del /s /q "%SystemRoot%\\SoftwareDistribution\\Download\\*"',
        'cmd /c del /s /q "%LocalAppData%\\Google\\Chrome\\User Data\\Default\\Cache\\*"',
        'cmd /c del /s /q "%LocalAppData%\\Microsoft\\Windows\\Explorer\\thumbcache_*.db"',
        "cmd /c del /q /f %localappdata%\\IconCache.db",
        "cmd /c del /q /f %localappdata%\\thumbcache_*.db",
        'cmd /c del /s /q "%SystemRoot%\\Memory.dmp"',
        'cmd /c del /s /q "%SystemRoot%\\System32\\LogFiles\\*"',
        'cmd /c del /s /q "%SystemRoot%\\Installer\\*.log"',
        'cmd /c del /s /q "%ProgramData%\\Microsoft\\Windows\\WER\\ReportArchive\\*"',
        'cmd /c del /s /q "%ProgramData%\\Microsoft\\Windows\\WER\\ReportQueue\\*"',
        'cmd /c del /s /q "%SystemRoot%\\Minidump\\*"',
        "cmd /c del /q /f %SystemRoot%\\System32\\winevt\\Logs\\*.evtx",
        "cmd /c wevtutil cl Application",
        "cmd /c wevtutil cl System",
        "cmd /c defrag C: /O",
        'powershell -Command "Clear-EventLog -LogName Application, Security, System"',
        'powershell -Command "Clear-RecycleBin -Confirm:$false"',
    ]

    for index, command in enumerate(commands):
        if command:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            write_log(f"Command: {command}\nOutput: {result.stdout}\nErrors: {result.stderr}")
            progress_var.set((index + 1) * 100 / len(commands))
            progress_bar.update()

    if root:
        root.after(500, root.destroy)
        messagebox.showinfo(
            "File Cleanup", "The cleanup process has completed.\n" "\n" " 2024 Script by Cloudy"
        )

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

root = tk.Tk()
root.title("File Cleanup")
root.geometry("300x50+0+0")
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(pady=10, padx=10, fill="both", expand=True)
root.after(100, run_commands)
root.mainloop()

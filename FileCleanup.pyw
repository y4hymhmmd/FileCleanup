import os
import sys
import ctypes
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()

def write_log(message):
    try:
        with open("log.txt", "a") as log_file:
            log_file.write(message + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menulis log: {e}")

def run_commands():
    commands = [
        'rd /s /q "%SystemRoot%\\Temp"',
        'rd /s /q "%LocalAppData%\\Temp"',
        'rd /s /q "%SystemRoot%\\Prefetch"',
        'del /s /q "%LocalAppData%\\NVIDIA\\GLCache\\*"',
        'del /s /q "%LocalAppData%\\Low\\NVIDIA\\PerDriverVersion\\DXCache\\*"',
        'del /s /q "%SystemRoot%\\SoftwareDistribution\\Download\\*"',
        'del /s /q "%LocalAppData%\\Google\\Chrome\\User Data\\Default\\Cache\\*"',
        'del /s /q "%LocalAppData%\\Mozilla\\Firefox\\Profiles\\*.default-release\\cache2\\*"',
        'del /s /q "%LocalAppData%\\Microsoft\\Windows\\Explorer\\thumbcache_*.db"',
        'del /s /q "%ProgramData%\\Microsoft\\Windows Defender\\Quarantine\\*"',
        'del /q /f %localappdata%\\IconCache.db',
        'del /q /f %localappdata%\\thumbcache_*.db',
        'del /s /q "%SystemRoot%\\Memory.dmp"',
        'del /s /q "%SystemRoot%\\System32\\LogFiles\\*"',
        'del /s /q "%SystemRoot%\\Installer\\*.log"',
        'del /s /q "%ProgramData%\\Microsoft\\Windows\\WER\\ReportArchive\\*"',
        'del /s /q "%ProgramData%\\Microsoft\\Windows\\WER\\ReportQueue\\*"',
        'del /s /q "%SystemRoot%\\Minidump\\*"',
        'del /q /f %SystemRoot%\\System32\\winevt\\Logs\\*.evtx',
        'cleanmgr /sagerun:1',
        'wevtutil cl Application',
        'wevtutil cl System',
        'powercfg -h off',
        'defrag C: /O',
        'powershell -Command "Clear-EventLog -LogName Application, Security, System"',
        'powershell -Command "Clear-RecycleBin -Confirm:$false"'
    ]

    for index, command in enumerate(commands):
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        write_log(f"Command: {command}\nOutput: {result.stdout}\nErrors: {result.stderr}")
        progress_var.set((index + 1) * 100 / len(commands))
        progress_bar.update()
        
    root.after(500, root.destroy)
    messagebox.showinfo("𝗙𝗶𝗹𝗲𝗖𝗹𝗲𝗮𝗻𝘂𝗽",
        "File has been cleaned.\n"
        "\n"
        "© 2024 Script by Cloudy"
        )

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

root = tk.Tk()
root.title("𝗙𝗶𝗹𝗲𝗖𝗹𝗲𝗮𝗻𝘂𝗽")
root.geometry("300x50+0+0")

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(pady=10, padx=10, fill='both', expand=True)

root.after(100, run_commands)
root.mainloop()

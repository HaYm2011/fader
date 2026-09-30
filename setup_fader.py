import os 
import sys
import subprocess
import shutil

PROJECT_DIR = os.path.dirname(os.path,abspath(__file__))
VENV_DIR = os.path.join(PROJECT_DIR, "venv")

def log(msg):
    print(f"[FADER Setup]  {msg}")

def check_ffmpeg():
    log("checking for FFmpeg...")
    if shutil.which("ffmpeg") is None:
        print("\n[!] FFmpeg not found on your system PATH.")
        print("Fader requires FFmpeg to convert yt streams to AAC (.m4a)")
        print("install it via : winget install Gyan.FFmpeg (on windows) or via bre/apt (on mac/linux),\n")
    else:
        log("FFmpeg is installed and available.")

def create_virtualenv():
    
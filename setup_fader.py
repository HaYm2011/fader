import os 
import sys
import subprocess
import shutil

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_DIR = os.path.join(PROJECT_DIR, "venv")

def log(msg):
    print(f"[FADER Setup]  {msg}")

def check_ffmpeg():
    log("Checking for FFmpeg...")
    if shutil.which("ffmpeg") is None:
        print("\n[!] FFmpeg not found on your system PATH.")
        print("Fader requires FFmpeg to convert yt streams to AAC (.m4a)")
        print("Install it via: winget install Gyan.FFmpeg (on Windows) or via brew/apt (on macOS/Linux).\n")
    else:
        log("FFmpeg is installed and available.")

def get_venv_executable(name: str) -> str:
    """Returns the path to an executable within the virtual environment."""
    if sys.platform == "win32":
        exe_path = os.path.join(VENV_DIR, "Scripts", f"{name}.exe")
        if not os.path.exists(exe_path):
            exe_path = os.path.join(VENV_DIR, "Scripts", name)
        return exe_path
    return os.path.join(VENV_DIR, "bin", name)

def create_virtualenv():
    log("Checking virtual environment...")
    if not os.path.exists(VENV_DIR):
        log(f"Creating virtual environment at {VENV_DIR}...")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
        log("Virtual environment created successfully.")
    else:
        log("Virtual environment already exists.")

def install_dependencies():
    log("Installing dependencies...")
    python_exe = get_venv_executable("python")
    dependencies = ["yt-dlp", "fastapi", "uvicorn"]
    subprocess.run([python_exe, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([python_exe, "-m", "pip", "install", *dependencies], check=True)
    log("Dependencies installed successfully.")

if __name__ == "__main__":
    print("=" * 50)
    print("            FADER SETUP SCRIPT            ")
    print("=" * 50)
    check_ffmpeg()
    create_virtualenv()
    install_dependencies()
    print("\n[+] Setup finished!")
    print("To activate the virtual environment:")
    if sys.platform == "win32":
        print(r"   .\venv\Scripts\activate")
    else:
        print("   source venv/bin/activate")
    print("\nTo start ingestion test:")
    print("   python cli-v1.py\n")
import os
import json
import urllib.request
import yt_dlp

LIBRARY_DIR="library"
METADATA_FILE=os.path.join(LIBRARY_DIR,"library.json")

os.makedirs(LIBRARY_DIR, exist_ok=True)

def load_library():
    if not os.pathexists(METADATA_FILE):
        return{}
    try:
        with open(METADATA_FILE,"r",encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return{}

def save_library(data):
    with open(METADATA_FILE,"w",encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def download_yt(search_query: str) -> dict:
    downloader_options={
        "format":"bestaudio/best",
        "outtmpl":os.path.join(LIBRARY_DIR, "%(id)s.%(ext)s"),
        "postprocessors":[{
            "key":"FFmpegExractAudio",
            "preferredcodec":"m4a",
        }],
        "quet":True,
        "no_warnings":True,
    }

# fader
A lightweight, self-hosted music streaming daemon that turns YouTube audio into a private, scrubbable media vault for all your devices. Built for Hack Club cloudFALL.
# 🎚️ Fader

> **Stop renting your music.** A lightweight, self-hosted audio streaming server that pulls tracks into a local vault and streams them seamlessly across your local network.

Built from scratch for **Hack Club cloudFALL** (replaces paid subscriptions like Spotify and Apple Music).

---

## ⚡ Features

- **Automated Ingestion:** Download audio directly from YouTube URLs with automatic conversion to high-quality MP3 via `yt-dlp` and `FFmpeg`.
- **Metadata Tagging:** Extracts and embeds audio metadata (title, artist/uploader, duration) automatically.
- **True HTTP Range Streaming:** Supports HTTP 206 Partial Content so you can seek and scrub through tracks without buffering the entire file.
- **Cross-Device Ready:** Accessible from any browser or mobile device on the same local network.
- **Self-Hosted & Private:** All audio lives in your personal storage vault—no accounts, no tracking, and zero monthly subscriptions.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, FastAPI, Uvicorn
- **Audio Processing:** `yt-dlp`, FFmpeg, Mutagen
- **Frontend:** Lightweight HTML5 Audio API & JavaScript

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- FFmpeg installed on your host system:
  ```bash
  # Arch Linux
  sudo pacman -S ffmpeg

  # Ubuntu / Debian
  sudo apt install ffmpeg

  # macOS
  brew install ffmpeg

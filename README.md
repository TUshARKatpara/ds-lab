# Jarvis Python Assistant

Jarvis is a beginner-friendly Python voice assistant project. It can listen for voice commands, speak responses, search Wikipedia, open common websites, tell the time, play local music, and send email using environment variables.

## Features

- Voice input with `SpeechRecognition`
- Text-to-speech responses with `pyttsx3`
- Wikipedia summaries
- Quick website shortcuts for Google and YouTube
- Local music playback from a configurable folder
- Email sending through Gmail SMTP

## Requirements

- Python 3.9 or newer
- A working microphone
- Windows is recommended for the current text-to-speech and music playback setup

## Installation

Clone the repository:

```bash
git clone https://github.com/TUshARKatpara/new-repo-.git
cd new-repo-
```

Install dependencies:

```bash
pip install -r requirements.txt
```

> Note: `PyAudio` can require extra setup depending on your operating system.

## Configuration

The email feature uses environment variables so your password is not stored in code.

```bash
set EMAIL=your_email@gmail.com
set EMAIL_PASSWORD=your_app_password
```

For music playback, set a folder path:

```bash
set MUSIC_DIR=C:\Users\YourName\Music
```

If `MUSIC_DIR` is not set, Jarvis will skip music playback and tell you that the folder is not configured.

## Run

```bash
python jarvis.py
```

Try commands like:

- `open google`
- `open youtube`
- `wikipedia machine learning`
- `the time`
- `play music`
- `exit`

## Roadmap

- Add more website shortcuts
- Add cross-platform music playback
- Add tests for command matching
- Add a simple command registry
- Add better error messages for microphone setup

## Contributing

Friendly contributions are welcome. If you are new to open source, start with small improvements like documentation, command examples, or beginner-friendly features.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is available under the MIT License.

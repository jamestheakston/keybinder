# Keybinder

A lightweight, open-source AutoHotkey clone for macOS built with Python.

## Prerequisites

* macOS
* Python 3
* Accessibility permissions (required to intercept keystrokes)

## How to Install and Run

### 1. Clone the repository

```bash
git clone https://github.com/jamestheakston/keybinder.git
cd keybinder
```

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Configure your hotkeys

Open `config.json` and map your custom key names to any shell command or script you want to run:

```json
{
    "hotkeys": {
        "f1": "open -a Terminal",
        "space": "say 'This is working!'",
        "a": "open -a Safari"
    }
}
```

### 4. Run it directly

```bash
python3 keybinder.py
```

### 5. Build the standalone binary *(Optional)*

If you want to compile Keybinder into a standalone local executable:

```bash
pyinstaller --onefile --noconsole keybinder.py
```

Your compiled binary will be available in the `dist/` folder.

## Accessibility Permissions

Keybinder requires **Accessibility permissions** to intercept keystrokes.

Grant access when prompted, or manually enable it through:

**System Settings → Privacy & Security → Accessibility**

Once permission has been granted, Keybinder can listen for and respond to your configured hotkeys.

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

You can add, remove, or change hotkeys to suit your workflow.

### 4. Run Keybinder

Start Keybinder with:

```bash
python3 keybinder.py
```

On the first launch, macOS may display a message asking you to allow Keybinder (or Terminal) to control your Mac.

If you see the following prompt:

<img width="473" height="193" alt="macOS Accessibility permission prompt" src="https://github.com/user-attachments/assets/7fb1184f-4092-4a74-bdeb-896555083e78" />

Click **Open System Settings**.

In **System Settings → Privacy & Security → Accessibility**, find **Terminal** and enable the toggle.

<img width="477" height="45" alt="Enable Terminal in Accessibility settings" src="https://github.com/user-attachments/assets/1c814931-0b0c-4d3f-9b12-18e080fd5534" />

You may be asked to enter your Mac's password or use Touch ID to confirm the change.

> **Tip:** If Terminal is already enabled but your hotkeys aren't working, try turning the permission off and on again, then restart Keybinder.

Once Accessibility access has been granted, return to Terminal and run Keybinder again:

```bash
python3 keybinder.py
```

Keybinder should now be able to detect your configured hotkeys and execute their associated commands.

> **Note:** If you are running Keybinder from a different application (such as a compiled executable), you may need to grant **that application** Accessibility access instead of Terminal.

### 5. Build the standalone binary *(Optional)*

If you want to compile Keybinder into a standalone local executable, install PyInstaller if you haven't already:

```bash
pip3 install pyinstaller
```

Then build Keybinder:

```bash
pyinstaller --onefile --noconsole keybinder.py
```

Your compiled application will be available in the `dist/` folder.

You can then run the compiled version instead of using Python:

```bash
./dist/keybinder
```

> **Note:** The compiled application may also require Accessibility permissions. If macOS asks for permission, add the compiled Keybinder application to **System Settings → Privacy & Security → Accessibility**.

## Accessibility Permissions

Keybinder requires **Accessibility permissions** to intercept and respond to keyboard input.

You can grant access when prompted, or manually enable it through:

**System Settings → Privacy & Security → Accessibility**

Make sure the application running Keybinder is enabled. For example:

* **Terminal** — when running `python3 keybinder.py`
* **Keybinder** — when running the compiled executable

Once permission has been granted, Keybinder can listen for and respond to your configured hotkeys.

## Example

With the following configuration:

```json
{
    "hotkeys": {
        "f1": "open -a Terminal",
        "space": "say 'This is working!'",
        "a": "open -a Safari"
    }
}
```

Pressing:

* **F1** → Opens Terminal
* **Space** → Uses macOS text-to-speech to say *"This is working!"*
* **A** → Opens Safari

## License

Keybinder is open-source software. See the repository for license information.

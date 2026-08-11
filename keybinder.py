#!/usr/bin/env python3
import sys
import os
import json
import subprocess
from Quartz import (
    CGEventTapCreate,
    kCGEventTapOptionDefault,
    kCGSessionEventTap,
    kCGHeadInsertEventTap,
    kCGEventKeyDown,
    CGEventGetIntegerValueField,
    kCGKeyboardEventKeycode,
    CGEventTapEnable,
    CFMachPortCreateRunLoopSource,
    CFRunLoopAddSource,
    CFRunLoopGetMain,
    CFRunLoopRun,
)

STRING_TO_KEYCODE = {
    "a": 0, "s": 1, "d": 2, "f": 3, "h": 4, "g": 5, "z": 6, "x": 7, "c": 8, "v": 9,
    "b": 11, "q": 12, "w": 13, "e": 14, "r": 15, "y": 16, "t": 17, "1": 18, "2": 19,
    "3": 20, "4": 21, "6": 22, "5": 23, "=": 24, "9": 25, "7": 26, "-": 27, "8": 28,
    "0": 29, "]": 30, "o": 31, "u": 32, "[": 33, "i": 34, "p": 35, "l": 37, "j": 38,
    "'": 39, "k": 40, ";": 41, "\\": 42, ",": 43, "/": 44, "n": 45, "m": 46, ".": 47,
    "tab": 48, "space": 49, "`": 50, "return": 36, "delete": 51, "escape": 53,
    "f1": 122, "f2": 120, "f3": 99, "f4": 118, "f5": 96, "f6": 97, "f7": 98,
    "f8": 100, "f9": 101, "f10": 109, "f11": 103, "f12": 111
}

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

def load_config():
    if not os.path.exists(CONFIG_PATH):
        default_config = {
            "hotkeys": {
                "f1": "open -a Terminal",
                "space": "say 'This is working!'"
            }
        }
        with open(CONFIG_PATH, "w") as f:
            json.dump(default_config, f, indent=4)
        default_config = default_config["hotkeys"]
    else:
        try:
            with open(CONFIG_PATH, "r") as f:
                default_config = json.load(f).get("hotkeys", {})
        except Exception as e:
            print(f"Error reading config.json: {e}")
            default_config = {}

    resolved_hotkeys = {}
    for key_name, command in default_config.items():
        key_lower = key_name.lower()
        if key_lower in STRING_TO_KEYCODE:
            keycode = STRING_TO_KEYCODE[key_lower]
            resolved_hotkeys[keycode] = command
        else:
            print(f"Warning: Unknown key name '{key_name}' in config.json")
            
    return resolved_hotkeys

HOTKEYS = load_config()

def action_callback(proxy, type, event, refcon):
    if type == kCGEventKeyDown:
        keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
        if keycode in HOTKEYS:
            cmd = HOTKEYS[keycode]
            subprocess.Popen(cmd, shell=True)
            return None
    return event

def main():
    print(f"Keybinder running with {len(HOTKEYS)} bound hotkey(s)...")
    tap = CGEventTapCreate(
        kCGSessionEventTap,
        kCGHeadInsertEventTap,
        kCGEventTapOptionDefault,
        (1 << kCGEventKeyDown),
        action_callback,
        None
    )
    if not tap:
        print("Error: Enable Accessibility permissions for your terminal/app in System Settings.")
        sys.exit(1)
        
    loop_source = CFMachPortCreateRunLoopSource(None, tap, 0)
    CFRunLoopAddSource(CFRunLoopGetMain(), loop_source, kCGHeadInsertEventTap)
    CGEventTapEnable(tap, True)
    CFRunLoopRun()

if __name__ == "__main__":
    main()

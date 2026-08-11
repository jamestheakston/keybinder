#!/usr/bin/env python3
import sys
import subprocess
from Quartz import (
    CGEventTapCreate,
    kCGEventTapOptionDefault,
    kCGHeadEventTypeSession,
    kCGEventKeyDown,
    CGEventGetIntegerValueField,
    kCGKeyboardEventKeycode,
    CGEventTapEnable,
    CFMachPortCreateRunLoopSource,
    CFRunLoopAddSource,
    CFRunLoopGetMain,
    CFRunLoopRun,
)

HOTKEYS = {
    122: "open -a Terminal",
}

def action_callback(proxy, type, event, refcon):
    if type == kCGEventKeyDown:
        keycode = CGEventGetIntegerValueField(event, 
kCGKeyboardEventKeycode)
        if keycode in HOTKEYS:
            cmd = HOTKEYS[keycode]
            subprocess.Popen(cmd, shell=True)
            return None
    return event

def main():
    print("Keybinder running...")
    tap = CGEventTapCreate(
        kCGHeadEventTypeSession,
        kCGEventTapOptionDefault,
        kCGHeadEventTypeSession,
        (1 << kCGEventKeyDown),
        action_callback,
        None
    )
    if not tap:
        print("Error: Enable Accessibility permissions for your 
terminal/app in System Settings.")
        sys.exit(1)
        
    loop_source = CFMachPortCreateRunLoopSource(None, tap, 0)
    CFRunLoopAddSource(CFRunLoopGetMain(), loop_source, 
kCGHeadEventTypeSession)
    CGEventTapEnable(tap, True)
    CFRunLoopRun()

if __name__ == "__main__":
    main()

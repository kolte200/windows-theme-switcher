import winreg
import sys
import ctypes

HWND_BROADCAST = 0xffff
WM_THEMECHANGED = 0x031A

def print_help():
    print("Help:")
    print("  -l --light : Switch to light theme")
    print("  -d --dark : Switch to dark theme")

if len(sys.argv) != 2:
    print_help()
    exit(1)

if sys.argv[1] in ["-d", "--dark"]:
    theme = 0
    print("Switch to dark theme")
elif sys.argv[1] in ["-l", "--light"]:
    theme = 1
    print("Switch to light theme")
else:
    print_help()
    exit(1)

def change_theme(theme):
    path = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize\\", access = winreg.KEY_SET_VALUE)
    winreg.SetValueEx(path, "AppsUseLightTheme", 0, winreg.REG_DWORD, theme)
    winreg.SetValueEx(path, "SystemUsesLightTheme", 0, winreg.REG_DWORD, theme)
    winreg.CloseKey(path)
    ctypes.windll.user32.PostMessageA(HWND_BROADCAST, WM_THEMECHANGED, None, None)

change_theme(theme)

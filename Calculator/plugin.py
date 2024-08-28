import pystyle
from pystyle import*
import colorama
from colorama import*
import time
import webbrowser


selectedchoice = Colorate.Color(Colors.red, "selectedchoice -->")

import os
import platform

def clear():
    # Detect the operating system
    current_os = platform.system()
    
    if current_os == "Windows":
        os.system('cls')  # Clear the console on Windows
    else:
        os.system('clear')  # Clear the console on macOS or Linux

print("dont run me")

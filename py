import threading
import requests
from pystyle import Colors, Colorate, Center
import time
import os
import webbrowser
import base64
from tkinter import filedialog as fd

# colors because I cannot remember to change it every time
black = "\033[1;30m"
titletext = " [-- KOALAHOOK --] Made by github.com/infamouskoala"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
invalidurl = f"{red}[! KOALAHOOK !]{white} Invalid url!"

# Social media links for dynamic display
socials = {
    "github": {"link": "https://github.com/infamouskoala"},
    "youtube": {"link": "https://youtube.com/infamouskoala"},
}

# Enhanced logo with ASCII art and dynamic social media links
logo = """
      __   __)             ____  ___)        
     (, ) /         /)    (, /   /        /) 
        /(   ____   // _     /---/  ______(/_ 
     ) /  \_(_)(_(_(/_(_(_) /   (__(_)(_) /(__
    (_/                  (_/                  
  >> [Webhook Multitool developed by @infamouskoala]
"""

# Add dynamic social media links
for platform, info in socials.items():
    link = info["link"].replace("https://", "")
    logo += f"      > [{platform.capitalize()}]: {link}\n"

logo = Center.XCenter(logo)


# Choices menu with enhanced formatting
def choice():
    print(Center.XCenter("""
[1] Send Message
[2] Delete Webhook
[3] Rename Webhook
[4] Spam Webhook
[5] Webhook Information
[6] Log Out
[7] Change PFP
[0] Source Code
"""))


# Print ASCII art in a cool gradient
def printascii():
    print(Colorate.Horizontal(Colors.cyan_to_blue, logo, 1))


# Clear the screen in a cleaner way
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Pause function with custom text
def pause(text: str = None):
    if text:
        print(text)
    os.system('pause >nul' if os.name == 'nt' else 'read -n 1 -s -r -p ""')


# Intro menu
def intromenu():
    clear()
    printascii()
    choice()


# Function to change the profile picture
def changepfp(url):
    input(f"{yellow}[? KOALAHOOK ?]{white} Press Enter to select file or skip this to input the path/url")
    image_path = fd.askopenfilename(filetypes=[("Profile Pictures", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        clear()
        image_path = input(f"{yellow}[? KOALAHOOK ?]{white} Path/URL to image: ")

    try:
        if image_path.startswith(('http://', 'https://')):
            response = requests.get(image_path)
            response.raise_for_status()
            encoded_image = base64.b64encode(response.content).decode('utf-8')
        else:
            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        data = {
            "avatar": f"data:image/jpeg;base64,{encoded_image}"
        }
        response = requests.patch(url, json=data)
        response.raise_for_status()
        print(f"{green}[+ KOALAHOOK +]{white} Profile picture changed successfully.")
    except Exception as err:
        print(f"{red}[! KOALAHOOK !] Error: {err}")


# Function to delete a webhook
def deletehook(url):
    print(f"{cyan}[+ KOALAHOOK +]{white} Trying to delete webhook...")
    try:
        response = requests.delete(url)
        response.raise_for_status()
        print(f"{green}[+ KOALAHOOK +]{white} Webhook deleted successfully.")
    except Exception as err:
        print(f"{red}[! KOALAHOOK !] Error: {err}")


# Function to send a message via the webhook
def sendmessage(url):
    msg = input(f"{yellow}[? KOALAHOOK ?]{white} Message: ")
    try:
        response = requests.post(url, json={"content": msg})
        response.raise_for_status()
        print(f"{green}[+ KOALAHOOK +]{white} Message sent successfully.")
    except Exception as err:
        print(f"{red}[! KOALAHOOK !] Error: {err}")


# Function to rename a webhook
def renamehook(url):
    name = input(f"{yellow}[? KOALAHOOK ?]{white} Webhook Name: ")
    print(f"{cyan}[+ KOALAHOOK +]{white} Trying to change username...")
    try:
        response = requests.patch(url, json={"name": name})
        response.raise_for_status()
        print(f"{green}[+ KOALAHOOK +]{white} Webhook name changed successfully.")
    except Exception as err:
        print(f"{red}[! KOALAHOOK !] Error: {err}")


# Function to spam the webhook with messages
def spamhook(url):
    print(f"{cyan}[+ KOALAHOOK +]{white} Trying to spam webhook...")
    msg = input(f"{yellow}[? KOALAHOOK ?]{white} Spam Text: ")
    timeout = float(input(f"{yellow}[? KOALAHOOK ?]{white} Timeout (to avoid api-ratelimit): "))
    try:
        print(f"{red}[! KOALAHOOK !] Spam has started. Relaunch the tool to stop spam and use it again.")
        while True:
            response = requests.post(url, json={"content": msg})
            response.raise_for_status()
            print(f"{green}[+ KOALAHOOK +]{white} Sent message")
            time.sleep(timeout)
    except Exception as err:
        print(f"{red}[! KOALAHOOK !] Error: {err}")


# Starting the script: Setup the webhook and run the menu
webhook = {}
os.system("title github.com/infamouskoala")
while True:
    clear()
    printascii()
    while True:
        try:
            url = input(f"{cyan}[>]{white} url: ")
            response = requests.get(url)
            if response.status_code == 200:
                webhook = response.json()
                break
            else:
                print(f"[{response.status_code}]: Invalid Webhook")
        except Exception as e:
            print(f"{red}[! KOALAHOOK !] Invalid Webhook: {e}")

    while True:
        intromenu()
        webhook_name = webhook["name"]
        print(f"\n\n\n{green}[+ KOALAHOOK +]{white} Logged into webhook: {webhook_name}")
        ch = int(input(f"{cyan}[>]{white} --> "))
        if ch == 1:
            clear()
            sendmessage(url)
            pause("Press any key to return to menu...")
        elif ch == 2:
            clear()
            deletehook(url)
            pause("Press any key to return to menu...")
        elif ch == 3:
            clear()
            renamehook(url)
            pause("Press any key to return to menu...")
        elif ch == 4:
            clear()
            spamhook(url)
            pause("Press any key to return to menu...")
        elif ch == 5:
            print(f"Webhook Information: {webhook}")
            pause("Press any key to return to menu...")
        elif ch == 6:
            os.system("title Logging out...")
            print("Logging out, please wait..")
            break
        elif ch == 0:
            webbrowser.open("https://github.com/infamouskoala/KOALAHOOK")
            break

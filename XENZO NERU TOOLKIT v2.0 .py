#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════╗
║                    XENZO NERU TOOLKIT v2.0                       ║
║                  Created by: @xenzoneru2                         ║
║                  Channel: https://t.me/ZenzoNeRu                 ║
╚══════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import random
import string
import hashlib
import base64
import socket
import subprocess
import platform
import time
import uuid
import json
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen

# ----------------------------- CONFIGURATION -----------------------------
CREATOR_ID = "@xenzoneru2"
CHANNEL_LINK = "https://t.me/ZenzoNeRu"
TOOLKIT_NAME = "XENZO NERU TOOLKIT"

# ----------------------------- UTILITY FUNCTIONS -----------------------------
def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Print a formatted header for each tool."""
    clear_screen()
    print("╔" + "═" * 58 + "╗")
    print(f"║  {TOOLKIT_NAME} - {title:<44} ║")
    print("╠" + "═" * 58 + "╣")
    print(f"║  👤 {CREATOR_ID:<53} ║")
    print(f"║  📢 {CHANNEL_LINK:<50} ║")
    print("╚" + "═" * 58 + "╝")
    print()

def print_banner():
    """Display main toolkit banner."""
    clear_screen()
    banner = r"""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║    ██╗  ██╗███████╗███╗   ██╗███████╗ ██████╗     ███╗   ██╗███████╗██████╗ ██╗   ██╗
║    ╚██╗██╔╝██╔════╝████╗  ██║██╔════╝██╔═══██╗    ████╗  ██║██╔════╝██╔══██╗██║   ██║
║     ╚███╔╝ █████╗  ██╔██╗ ██║█████╗  ██║   ██║    ██╔██╗ ██║█████╗  ██████╔╝██║   ██║
║     ██╔██╗ ██╔══╝  ██║╚██╗██║██╔══╝  ██║   ██║    ██║╚██╗██║██╔══╝  ██╔══██╗██║   ██║
║    ██╔╝ ██╗███████╗██║ ╚████║███████╗╚██████╔╝    ██║ ╚████║███████╗██║  ██║╚██████╔╝
║    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝     ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
║                                                                  ║
║                    ╔══════════════════════════════╗              ║
║                    ║     XENZO NERU TOOLKIT       ║              ║
║                    ║          VERSION 2.0         ║              ║
║                    ╚══════════════════════════════╝              ║
║                                                                  ║
║               👤 CREATOR: @xenzoneru2                            ║
║               📢 CHANNEL: https://t.me/ZenzoNeRu                 ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
    print(banner)
    print("\n" + "═" * 58)
    print("  WELCOME TO THE ULTIMATE TOOLKIT - XENZO NERU v2.0")
    print("═" * 58)

def pause():
    """Wait for user input."""
    input("\n╔════════════════════════════════════════════════════╗\n║  Press Enter to continue...                          ║\n╚════════════════════════════════════════════════════╝")

def get_public_ip():
    """Fetch public IP address."""
    try:
        return urlopen('https://api.ipify.org', timeout=5).read().decode('utf8')
    except:
        return "Unable to fetch"

# ----------------------------- TOOL FUNCTIONS (Each with separate interface) -----------------------------

def tool_device_info():
    """Display system information."""
    print_header("DEVICE INFO")
    print(f"  🖥️  System       : {platform.system()} {platform.release()}")
    print(f"  💻 Node Name    : {platform.node()}")
    print(f"  ⚙️  Processor    : {platform.processor() or 'Unknown'}")
    print(f"  🏗️  Architecture : {platform.machine()}")
    print(f"  🐍 Python Ver   : {sys.version.split()[0]}")
    print(f"  📁 OS Type      : {os.name}")
    pause()

def tool_ip_tracker():
    """Show local and public IP information."""
    print_header("IP TRACKER")
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"  🌐 Hostname     : {hostname}")
    print(f"  📍 Local IP     : {local_ip}")
    print(f"  🌍 Public IP    : {get_public_ip()}")
    pause()

def tool_password_generator():
    """Generate random strong passwords."""
    print_header("PASSWORD GENERATOR")
    try:
        length = int(input("  🔐 Enter password length (8-50): ") or 16)
        length = max(8, min(50, length))
    except:
        length = 16
    
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    password = ''.join(random.choice(chars) for _ in range(length))
    
    print("\n  ╔════════════════════════════════════════════╗")
    print(f"  ║  Generated Password: {password:<28} ║")
    print("  ╚════════════════════════════════════════════╝")
    
    # Strength check
    strength = "WEAK"
    if len(password) >= 12 and any(c.isdigit() for c in password) and any(c in "!@#$%^&*" for c in password):
        strength = "STRONG"
    elif len(password) >= 10:
        strength = "MEDIUM"
    print(f"\n  📊 Password Strength: {strength}")
    pause()

def tool_file_encrypt_decrypt():
    """XOR file encryption/decryption."""
    print_header("FILE ENCRYPT/DECRYPT")
    path = input("  📁 Enter file path: ").strip()
    if not Path(path).is_file():
        print("  ❌ File not found!")
        pause()
        return
    
    key = input("  🔑 Enter key (string): ").strip()
    if not key:
        print("  ❌ No key provided!")
        pause()
        return
    
    try:
        with open(path, 'rb') as f:
            data = f.read()
        
        key_bytes = key.encode()
        result = bytearray()
        for i, byte in enumerate(data):
            result.append(byte ^ key_bytes[i % len(key_bytes)])
        
        out_path = path + ".encrypted"
        with open(out_path, 'wb') as f:
            f.write(result)
        
        print(f"\n  ✅ Success! Output saved as: {out_path}")
        print(f"  📊 Original size: {len(data)} bytes")
        print(f"  📊 Encrypted size: {len(result)} bytes")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    pause()

def tool_fake_identity():
    """Generate a complete fake identity."""
    print_header("FAKE IDENTITY GENERATOR")
    
    first_names = ["John", "Jane", "Alex", "Maria", "Michael", "Sarah", "David", "Laura", "James", "Emma", "Robert", "Lisa"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego"]
    streets = ["Main St", "Oak Ave", "Maple Dr", "Cedar Ln", "Pine Rd", "Elm St", "Washington Ave"]
    jobs = ["Software Engineer", "Teacher", "Doctor", "Artist", "Chef", "Pilot", "Lawyer", "Architect", "Nurse"]
    
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(18, 85)
    email = f"{name.lower().replace(' ', '.')}{random.randint(1,999)}@mail.com"
    phone = f"+1-{random.randint(200,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"
    address = f"{random.randint(100,9999)} {random.choice(streets)}, {random.choice(cities)}, {random.choice(['NY','CA','TX','IL','FL'])} {random.randint(10000,99999)}"
    job = random.choice(jobs)
    ssn = f"{random.randint(100,999)}-{random.randint(10,99)}-{random.randint(1000,9999)}"
    
    print("  ╔══════════════════════════════════════════════════════════╗")
    print(f"  ║  🆔 Name     : {name:<46} ║")
    print(f"  ║  🎂 Age      : {age:<46} ║")
    print(f"  ║  💼 Job      : {job:<46} ║")
    print(f"  ║  📧 Email    : {email:<46} ║")
    print(f"  ║  📞 Phone    : {phone:<46} ║")
    print(f"  ║  🏠 Address  : {address:<46} ║")
    print(f"  ║  🆔 SSN      : {ssn:<46} ║")
    print("  ╚══════════════════════════════════════════════════════════╝")
    pause()

def tool_wifi_scanner():
    """Scan available Wi-Fi networks."""
    print_header("Wi-Fi SCANNER")
    print("  📡 Scanning for Wi-Fi networks...\n")
    
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'], universal_newlines=True)
            lines = [line.strip() for line in output.split('\n') if 'SSID' in line]
            ssids = [line.split(':')[1].strip() for line in lines if ':' in line and line.split(':')[1].strip()]
            if ssids:
                print("  Found Networks:")
                for i, ssid in enumerate(ssids[:15], 1):
                    print(f"    {i:2}. {ssid}")
            else:
                print("  ⚠️  No networks found.")
        else:
            try:
                output = subprocess.check_output(['nmcli', '-t', '-f', 'SSID', 'dev', 'wifi'], universal_newlines=True)
                ssids = [line.strip() for line in output.split('\n') if line.strip()]
                if ssids:
                    print("  Found Networks:")
                    for i, ssid in enumerate(ssids[:15], 1):
                        print(f"    {i:2}. {ssid}")
                else:
                    print("  ⚠️  No networks found.")
            except:
                print("  ⚠️  Wi-Fi scan requires 'nmcli' or run as root.")
    except Exception as e:
        print(f"  ❌ Scan failed: {e}")
    pause()

def tool_sms_bomber_demo():
    """Demo SMS bomber."""
    print_header("SMS BOMBER (DEMO MODE)")
    print("  ⚠️  THIS IS A DEMO - No actual messages are sent! ⚠️\n")
    number = input("  📱 Enter phone number for demo: ").strip()
    try:
        count = int(input("  🔢 Number of messages (1-20): ") or 5)
        count = max(1, min(20, count))
    except:
        count = 5
    
    print(f"\n  📤 Sending {count} demo messages to {number}...\n")
    for i in range(count):
        time.sleep(0.3)
        print(f"    [{i+1:2}] ✉️  Demo SMS sent")
    
    print(f"\n  ✅ Demo completed! {count} messages simulated.")
    pause()

def tool_ascii_art_generator():
    """Generate ASCII art from text."""
    print_header("ASCII ART GENERATOR")
    text = input("  🎨 Enter text to convert: ").strip()
    if not text:
        print("  ❌ No text entered!")
        pause()
        return
    
    try:
        import pyfiglet
        art = pyfiglet.figlet_format(text, font='slant')
        print("\n" + art)
    except ImportError:
        print("\n  ⚠️  Install 'pyfiglet' for better art: pip install pyfiglet")
        print("  ╔════════════════════════════════════════════╗")
        print(f"  ║  Simple ASCII: {text:<36} ║")
        print("  ╚════════════════════════════════════════════╝")
    pause()

def tool_website_checker():
    """Check website availability."""
    print_header("WEBSITE CHECKER")
    url = input("  🌐 Enter URL (https://example.com): ").strip()
    if not url:
        print("  ❌ No URL given!")
        pause()
        return
    
    try:
        import requests
        r = requests.get(url, timeout=8, headers={'User-Agent': 'Mozilla/5.0'})
        print(f"\n  📊 Status Code: {r.status_code}")
        print(f"  ✅ Website: {'UP' if r.status_code < 400 else 'DOWN'}")
        print(f"  ⏱️  Response Time: {r.elapsed.total_seconds():.2f} seconds")
    except ImportError:
        host = url.replace('http://', '').replace('https://', '').split('/')[0]
        try:
            socket.gethostbyname(host)
            print(f"\n  ✅ Host {host} is reachable")
            print("  ⚠️  Install 'requests' for full HTTP check")
        except:
            print(f"  ❌ Failed to resolve {host}")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    pause()

def tool_port_scanner():
    """Scan common ports on a target."""
    print_header("PORT SCANNER")
    target = input("  🎯 Enter target IP or hostname: ").strip()
    if not target:
        print("  ❌ No target given!")
        pause()
        return
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
    print(f"\n  🔍 Scanning {target}...\n")
    open_ports = []
    
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
            print(f"    ✅ Port {port} - OPEN")
        sock.close()
    
    if open_ports:
        print(f"\n  📊 Found {len(open_ports)} open port(s)")
    else:
        print("  ❌ No common open ports found")
    pause()

def tool_hash_generator():
    """Generate various hashes of input text."""
    print_header("HASH GENERATOR")
    text = input("  🔤 Enter text to hash: ").strip()
    if not text:
        print("  ❌ No text entered!")
        pause()
        return
    
    print("\n  ╔══════════════════════════════════════════════════════════╗")
    print(f"  ║  MD5    : {hashlib.md5(text.encode()).hexdigest():<36} ║")
    print(f"  ║  SHA1   : {hashlib.sha1(text.encode()).hexdigest():<36} ║")
    print(f"  ║  SHA256 : {hashlib.sha256(text.encode()).hexdigest():<36} ║")
    print(f"  ║  SHA512 : {hashlib.sha512(text.encode()).hexdigest():<36} ║")
    print("  ╚══════════════════════════════════════════════════════════╝")
    pause()

def tool_clipboard_manager():
    """Simple clipboard manager simulation."""
    print_header("CLIPBOARD MANAGER")
    print("  📋 Clipboard Manager (Simple Text Storage)")
    print("\n  Options:")
    print("    1. Save text to clipboard storage")
    print("    2. View saved text")
    print("    3. Clear storage")
    
    storage_file = Path.home() / ".xenzo_clipboard.json"
    
    try:
        choice = input("\n  Select option (1-3): ").strip()
        
        if choice == "1":
            text = input("  📝 Enter text to save: ").strip()
            if text:
                data = {"saved_text": text, "timestamp": str(datetime.now())}
                with open(storage_file, 'w') as f:
                    json.dump(data, f)
                print("  ✅ Text saved to clipboard storage!")
        elif choice == "2":
            if storage_file.exists():
                with open(storage_file, 'r') as f:
                    data = json.load(f)
                print(f"\n  📋 Saved text: {data.get('saved_text', 'None')}")
                print(f"  🕐 Timestamp: {data.get('timestamp', 'Unknown')}")
            else:
                print("  ⚠️  No saved text found!")
        elif choice == "3":
            if storage_file.exists():
                storage_file.unlink()
                print("  ✅ Clipboard storage cleared!")
            else:
                print("  ⚠️  No storage to clear!")
        else:
            print("  ❌ Invalid option!")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    pause()

def tool_auto_backup():
    """Auto backup demo."""
    print_header("AUTO BACKUP")
    source = input("  📁 Source folder to backup: ").strip()
    if not Path(source).is_dir():
        print("  ❌ Source folder not found!")
        pause()
        return
    
    backup_dir = Path.home() / "XenzoBackups"
    backup_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    backup_path = backup_dir / backup_name
    
    try:
        import shutil
        shutil.copytree(source, backup_path)
        print(f"\n  ✅ Backup created successfully!")
        print(f"  📂 Location: {backup_path}")
        print(f"  📊 Size: {sum(f.stat().st_size for f in backup_path.rglob('*') if f.is_file()) / 1024:.2f} KB")
    except Exception as e:
        print(f"  ❌ Backup failed: {e}")
    pause()

def tool_translator_demo():
    """Simple translator demo."""
    print_header("TRANSLATOR (DEMO)")
    print("  ⚠️  DEMO MODE - Basic translation simulation")
    text = input("  🔤 Enter text to translate: ").strip()
    if not text:
        print("  ❌ No text entered!")
        pause()
        return
    
    # Simple word mapping demo
    translations = {
        "hello": "hola", "world": "mundo", "good": "bueno", "morning": "mañana",
        "thank": "gracias", "you": "tú", "yes": "sí", "no": "no"
    }
    
    translated = []
    for word in text.lower().split():
        translated.append(translations.get(word, word))
    
    print(f"\n  📝 Original: {text}")
    print(f"  🌎 Demo Spanish: {' '.join(translated)}")
    print("\n  💡 Note: Full translation requires internet API")
    pause()

def tool_guess_game():
    """Number guessing game."""
    print_header("GUESS THE NUMBER GAME")
    print("  🎮 I'm thinking of a number between 1 and 100!")
    
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("  🔢 Your guess: "))
            attempts += 1
            
            if guess < number:
                print("  📈 Too low! Try again.")
            elif guess > number:
                print("  📉 Too high! Try again.")
            else:
                print(f"\n  🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("  ❌ Please enter a valid number!")
    
    pause()

def tool_matrix_rain():
    """Matrix digital rain effect."""
    print_header("MATRIX RAIN (Press Ctrl+C to stop)")
    print("  🌧️  Starting Matrix rain effect...\n")
    
    try:
        columns = os.get_terminal_size().columns
        for _ in range(100):
            line = ''.join(random.choice('01') for _ in range(columns))
            print(f"\033[32m{line}\033[0m")
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass
    except:
        print("\n  ⚠️  Terminal size detection failed, showing simple effect")
        for _ in range(50):
            print(''.join(random.choice('01') for _ in range(50)))
            time.sleep(0.05)
    pause()

def tool_digital_clock():
    """Digital clock display."""
    print_header("DIGITAL CLOCK (Press Ctrl+C to stop)")
    print("  🕐 Live digital clock - Press Ctrl+C to exit\n")
    
    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"\r  ⏰ Current Time: {current_time}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n  ✅ Clock stopped.")
    pause()

def tool_fortune_cookie():
    """Fortune cookie messages."""
    print_header("FORTUNE COOKIE")
    
    fortunes = [
        "🍪 You will have a great day today!",
        "🍪 A pleasant surprise is waiting for you.",
        "🍪 Your hard work will soon pay off.",
        "🍪 Good things come to those who wait.",
        "🍪 Adventure awaits you in the near future.",
        "🍪 Trust your instincts today.",
        "🍪 A new opportunity will present itself.",
        "🍪 Happiness is just around the corner.",
        "🍪 Your creativity will be rewarded.",
        "🍪 Believe in yourself and all that you are."
    ]
    
    print("\n  ╔════════════════════════════════════════════╗")
    print(f"  ║  {random.choice(fortunes):<40} ║")
    print("  ╚════════════════════════════════════════════╝")
    pause()

def tool_random_fact():
    """Random interesting facts."""
    print_header("RANDOM FACT")
    
    facts = [
        "🐱 A group of cats is called a clowder.",
        "🌊 Octopuses have three hearts.",
        "🍌 Bananas are berries, but strawberries aren't.",
        "🐘 Elephants can't jump.",
        "🦒 Giraffes have the same number of neck vertebrae as humans.",
        "🐧 Penguins can drink salt water.",
        "🦋 Butterflies taste with their feet.",
        "🐋 Blue whales are the largest animals ever known to exist.",
        "🕷️ Spiders have blue blood.",
        "🌙 The Moon is moving away from Earth."
    ]
    
    print("\n  ╔════════════════════════════════════════════╗")
    print(f"  ║  {random.choice(facts):<40} ║")
    print("  ╚════════════════════════════════════════════╝")
    pause()

def tool_base64_tool():
    """Base64 encode/decode."""
    print_header("BASE64 TOOL")
    print("  Options:")
    print("    1. Encode to Base64")
    print("    2. Decode from Base64")
    
    choice = input("\n  Select (1-2): ").strip()
    text = input("  📝 Enter text: ").strip()
    
    if not text:
        print("  ❌ No text entered!")
        pause()
        return
    
    try:
        if choice == "1":
            encoded = base64.b64encode(text.encode()).decode()
            print(f"\n  ✅ Encoded: {encoded}")
        elif choice == "2":
            decoded = base64.b64decode(text).decode()
            print(f"\n  ✅ Decoded: {decoded}")
        else:
            print("  ❌ Invalid choice!")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    pause()

def tool_text_encrypt_decrypt():
    """Simple text encryption/decryption."""
    print_header("TEXT ENCRYPT/DECRYPT")
    print("  Options:")
    print("    1. Encrypt text")
    print("    2. Decrypt text")
    
    choice = input("\n  Select (1-2): ").strip()
    text = input("  📝 Enter text: ").strip()
    key = input("  🔑 Enter key: ").strip()
    
    if not text or not key:
        print("  ❌ Text and key required!")
        pause()
        return
    
    try:
        key_bytes = key.encode()
        text_bytes = text.encode()
        result = bytearray()
        
        for i, byte in enumerate(text_bytes):
            result.append(byte ^ key_bytes[i % len(key_bytes)])
        
        if choice == "1":
            encoded = base64.b64encode(result).decode()
            print(f"\n  ✅ Encrypted (Base64): {encoded}")
        elif choice == "2":
            try:
                decoded_bytes = base64.b64decode(text)
                result = bytearray()
                for i, byte in enumerate(decoded_bytes):
                    result.append(byte ^ key_bytes[i % len(key_bytes)])
                print(f"\n  ✅ Decrypted: {result.decode()}")
            except:
                print("  ❌ Invalid encrypted text!")
        else:
            print("  ❌ Invalid choice!")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    pause()

def tool_ping_multiple():
    """Ping multiple hosts."""
    print_header("PING MULTIPLE")
    hosts_input = input("  🌐 Enter hosts (comma separated): ").strip()
    hosts = [h.strip() for h in hosts_input.split(',') if h.strip()]
    
    if not hosts:
        print("  ❌ No hosts entered!")
        pause()
        return
    
    print("\n  📡 Pinging hosts...\n")
    for host in hosts[:5]:
        try:
            param = '-n' if platform.system() == 'Windows' else '-c'
            output = subprocess.run(['ping', param, '1', host], capture_output=True, timeout=5)
            if output.returncode == 0:
                print(f"    ✅ {host} - Reachable")
            else:
                print(f"    ❌ {host} - Unreachable")
        except:
            print(f"    ❌ {host} - Timeout")
    pause()

def tool_random_joke():
    """Random jokes."""
    print_header("RANDOM JOKE")
    
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a fake noodle? An impasta!",
        "Why did the scarecrow win an award? He was outstanding in his field!",
        "What's the best thing about Switzerland? I don't know, but the flag is a big plus!",
        "Why don't eggs tell jokes? They'd crack each other up!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why did the math book look so sad? Because it had too many problems!"
    ]
    
    print("\n  ╔══════════════════════════════════════════════════════════╗")
    print(f"  ║  😂 {random.choice(jokes):<52} ║")
    print("  ╚══════════════════════════════════════════════════════════╝")
    pause()

def tool_ascii_qr_code():
    """Generate simple ASCII QR code (simulation)."""
    print_header("ASCII QR CODE (SIMULATION)")
    text = input("  📝 Enter text for QR code: ").strip()
    if not text:
        print("  ❌ No text entered!")
        pause()
        return
    
    print("\n  ⚠️  Note: Full QR code requires 'qrcode' library")
    print("  📱 Simple representation:\n")
    print("  ████████████████████████████████")
    print("  ██                        ██  ██")
    print("  ██  " + text[:20].ljust(20) + "  ██  ██")
    print("  ██                        ██  ██")
    print("  ████████████████████████████████")
    print("  ██    ████  ██  ██  ██    ██")
    print("  ██  ██████  ██  ██  ██  ████")
    print("  ████████████████████████████████")
    pause()

def tool_surprise_me():
    """Random surprise tool."""
    print_header("SURPRISE ME!")
    
    surprises = [
        tool_random_joke,
        tool_fortune_cookie,
        tool_random_fact,
        tool_guess_game
    ]
    
    random.choice(surprises)()

# ----------------------------- MAIN MENU -----------------------------

def main():
    """Main program loop."""
    while True:
        print_banner()
        
        menu_items = [
            ("1", "Device Info", tool_device_info),
            ("2", "IP Tracker", tool_ip_tracker),
            ("3", "Password Generator", tool_password_generator),
            ("4", "File Encrypt/Decrypt", tool_file_encrypt_decrypt),
            ("5", "Fake Identity", tool_fake_identity),
            ("6", "WiFi Scanner", tool_wifi_scanner),
            ("7", "SMS Bomber (Demo)", tool_sms_bomber_demo),
            ("8", "ASCII Art Generator", tool_ascii_art_generator),
            ("9", "Website Checker", tool_website_checker),
            ("10", "Port Scanner", tool_port_scanner),
            ("11", "Hash Generator", tool_hash_generator),
            ("12", "Clipboard Manager", tool_clipboard_manager),
            ("13", "Auto Backup", tool_auto_backup),
            ("14", "Translator (Demo)", tool_translator_demo),
            ("15", "Guess Game", tool_guess_game),
            ("16", "Matrix Rain", tool_matrix_rain),
            ("17", "Digital Clock", tool_digital_clock),
            ("18", "Fortune Cookie", tool_fortune_cookie),
            ("19", "Random Fact", tool_random_fact),
            ("20", "Base64 Tool", tool_base64_tool),
            ("21", "Text Encrypt/Decrypt", tool_text_encrypt_decrypt),
            ("22", "Ping Multiple", tool_ping_multiple),
            ("23", "Random Joke", tool_random_joke),
            ("24", "ASCII QR Code", tool_ascii_qr_code),
            ("25", "Surprise Me!", tool_surprise_me),
            ("0", "Exit", None)
        ]
        
        print("\n  ╔══════════════════════════════════════════════════════════╗")
        print("  ║  Available Tools:                                      ║")
        print("  ╠══════════════════════════════════════════════════════════╣")
        
        # Print menu in 2 columns
        for i, (num, name, _) in enumerate(menu_items):
            if i < len(menu_items) // 2:
                left_num = num
                left_name = name
                right_num, right_name, _ = menu_items[i + len(menu_items)//2]
                print(f"  ║  [{left_num:2}] {left_name:<22}  [{right_num:2}] {right_name:<22} ║")
        
        # Print the last item if odd count
        if len(menu_items) % 2 != 0:
            last_num, last_name, _ = menu_items[-1]
            print(f"  ║  [{last_num:2}] {last_name:<50} ║")
        
        print("  ╚══════════════════════════════════════════════════════════╝")
        
        choice = input("\n  👤 Select tool: ").strip()
        
        found = False
        for num, name, func in menu_items:
            if choice == num:
                found = True
                if func:
                    func()
                else:
                    print("\n  👋 Thank you for using Xenzo NeRu Toolkit!")
                    print(f"  📢 Join our channel: {CHANNEL_LINK}")
                    print("  🔗 Stay connected for more tools!\n")
                    sys.exit(0)
                break
        
        if not found:
            print("\n  ❌ Invalid selection! Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  👋 Exiting... Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n  ❌ Unexpected error: {e}")
        sys.exit(1)
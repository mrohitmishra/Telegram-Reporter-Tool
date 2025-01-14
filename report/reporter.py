import os
import time
from telethon.sync import TelegramClient
from telethon import functions, types

# ANSI color codes for banner
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k, g = '\033[00;36m', '\033[90m', '\033[38;5;130m'

# Function for typing effect
def re(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)

# Banner
re("""
   ____  _            _    _               
  | __ )| | ___   ___| | _(_)_ __   __ _   
  |  _ \\| |/ _ \\ / __| |/ / | '_ \\ / _` |  
  | |_) | | (_) | (__|   <| | | | | (_| |_ 
  |____/|_|\\___/ \\___|_|\\_\\_|_| |_|\\__, ( )
                                  |___/|/  
""")
re("Warning! Use this tool responsibly. Any misuse is the user's responsibility.\n")
print(f"{lrd}")

# Get user inputs for API credentials and session
api_id = int(input("Enter your API ID: "))
api_hash = input("Enter your API Hash: ")
session_name = input("Enter the session name (e.g., session_name): ")
target_username = input("Enter the target username or channel link: ")

# Start Telethon client
with TelegramClient(session_name, api_id, api_hash) as client:
    print(f"Signed in successfully as {client.get_me().username}; remember to not break the ToS or you will risk an account ban!")
    try:
        target_entity = client.get_entity(target_username)
        print(f"Target Channel Found: {target_entity.title} - {target_entity.id}")

        # Using InputReportReasonSpam as the reporting reason
        reason = types.InputReportReasonSpam()  # Replace with a different reason if needed
        message = "This channel is a scam and violates Telegram ToS."  # Customize the message as needed
        for i in range(1, 31):  # Send reports
            try:
                client(functions.account.ReportPeerRequest(
                    peer=target_entity,
                    reason=reason,
                    message=message
                ))
                print(f"[✔] Report {i} sent successfully!")
            except Exception as e:
                print(f"[!] Failed to send report {i}: {e}")
            time.sleep(2)  # Add delay between reports to avoid being flagged
    except Exception as e:
        print(f"[!] An error occurred: {e}")

import os
import time
import platform
try:
    from telethon.sync import TelegramClient
except ImportError:
    os.system("pip install telethon")
from telethon.tl import types
from telethon import functions

def re(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)

rd, gn, lrd, cn = '\033[00;31m', '\033[00;32m', '\033[01;31m', '\033[00;36m'

banner = f"""
{lrd}
██████╗ ██╗      █████╗  ██████╗██╗  ██╗██████╗ ███████╗ █████╗ ██╗     
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔════╝██╔══██╗██║     
██████╔╝██║     ███████║██║     █████╔╝ ██████╔╝███████╗███████║██║     
██╔═══╝ ██║     ██╔══██║██║     ██╔═██╗ ██╔═══╝ ╚════██║██╔══██║██║     
██║     ███████╗██║  ██║╚██████╗██║  ██╗██║     ███████║██║  ██║███████╗
╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝
"""

re(banner)
print("\n[+] BlackPearl Account Reporter Tool\n")

api_id = input(f"{gn}[+] Enter API ID: {cn}")
api_hash = input(f"{gn}[+] Enter API Hash: {cn}")
phone_number = input(f"{gn}[+] Enter Phone Number: {cn}")
password = input(f"{gn}[+] Enter Password (leave blank if none): {cn}")
target_user = input(f"{gn}[+] Enter Target Username: {cn}")
report_count = int(input(f"{gn}[+] Number of Reports: {cn}"))

def report_spam(api_id, api_hash, phone_number, password, target_user, report_count):
    with TelegramClient('reporter', api_id, api_hash) as client:
        client.start(phone_number, password)
        user = client.get_entity(target_user)
        target_peer = types.InputPeerUser(user_id=user.id, access_hash=user.access_hash)

        for i in range(report_count):
            client(functions.account.ReportPeerRequest(
                peer=target_peer,
                reason=types.InputReportReasonSpam(),
                message="Spam report sent by BlackPearl"
            ))
            print(f"{gn}[+] Spam Report {i + 1} sent!")

report_spam(api_id, api_hash, phone_number, password, target_user, report_count)

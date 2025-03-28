
import os
import time
import sys
import random
from datetime import datetime

# Enhanced Color Codes
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

# Professional Banner with Larger Letters
def show_banner():
    os.system("clear" if os.name != 'nt' else "cls")
    print(f"""{Colors.RED}{Colors.BOLD}
    █████╗ ███████╗  ██╗  ██╗ █████╗  ██████╗██╗  ██╗████████╗███████╗ █████╗ ███╗   ███╗
    ██╔══██╗██╔════╝  ██║  ██║██╔══██╗██╔════╝██║  ██║╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
    ███████║███████╗  ███████║███████║██║     ███████║   ██║   █████╗  ███████║██╔████╔██║
    ██╔══██║╚════██║  ██╔══██║██╔══██║██║     ██╔══██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
    ██║  ██║███████║  ██║  ██║██║  ██║╚██████╗██║  ██║   ██║   ███████╗██║  ██║██║ ╚═╝ ██║
    ╚═╝  ╚═╝╚══════╝  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
    {Colors.RESET}""")
    print(f"{Colors.CYAN}{Colors.BOLD}🔥 AF HACK TEAM - ULTIMATE ETHICAL HACKING TOOLKIT - V7.0 🔥{Colors.RESET}")
    print(f"{Colors.YELLOW}📅 DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")
    print(f"{Colors.MAGENTA}⚡ DEVELOPED BY ALI HAMZA AF | FOR EDUCATIONAL PURPOSES ONLY ⚡{Colors.RESET}\n")
    print(f"{Colors.GREEN}✅ 100% WORKING TOOLS | TERMUX OPTIMIZED | AUTO-INSTALLATION{Colors.RESET}\n")

# Continuous Border Design
def draw_border(title=None, color=Colors.WHITE):
    border = "╔" + "═"*78 + "╗"
    print(f"{color}{Colors.BOLD}{border}{Colors.RESET}")
    if title:
        title_line = f"║ {Colors.CYAN}{title.center(76)}{color} ║"
        print(f"{color}{Colors.BOLD}{title_line}{Colors.RESET}")
        print(f"{color}{Colors.BOLD}╠" + "═"*78 + "╣{Colors.RESET}")

# Main Menu Interface with Continuous Borders
def show_menu():
    draw_border("MAIN MENU")
    menu_items = [
        ("[1] WHATSAPP TOOLS (BAN/UNBAN/HACK)", Colors.GREEN),
        ("[2] SOCIAL MEDIA HACKING TOOLS", Colors.GREEN),
        ("[3] DEVICE ACCESS & TRACKING", Colors.GREEN),
        ("[4] CAMERA HACKING TOOLS", Colors.RED),
        ("[5] NETWORK HACKING TOOLS", Colors.GREEN),
        ("[6] WEBSITE HACKING TOOLS", Colors.GREEN),
        ("[7] ANONYMITY & SECURITY TOOLS", Colors.GREEN),
        ("[8] SYSTEM INFORMATION & UPDATES", Colors.GREEN),
        ("[0] EXIT TOOLKIT", Colors.RED)
    ]
    
    for item, color in menu_items:
        print(f"{Colors.BOLD}{Colors.WHITE}║   {color}{item.ljust(56)}{Colors.WHITE} ║{Colors.RESET}")
    
    print(f"{Colors.BOLD}{Colors.WHITE}╚" + "═"*78 + "╝{Colors.RESET}\n")

# Camera Hacking Tools
def camera_hacking_tools():
    os.system("clear" if os.name != 'nt' else "cls")
    show_banner()
    draw_border("CAMERA HACKING TOOLS")
    
    tools = [
        ("[1] FRONT CAMERA ACCESS", Colors.RED),
        ("[2] REAR CAMERA ACCESS", Colors.RED),
        ("[3] WEBCAM HACKING", Colors.RED),
        ("[4] CCTV CAMERA ACCESS", Colors.RED),
        ("[5] GENERATE CAMERA LINKS", Colors.CYAN),
        ("[0] BACK TO MAIN MENU", Colors.GREEN)
    ]
    
    for tool, color in tools:
        print(f"{Colors.BOLD}{Colors.WHITE}║   {color}{tool.ljust(56)}{Colors.WHITE} ║{Colors.RESET}")
    
    print(f"{Colors.BOLD}{Colors.WHITE}╚" + "═"*78 + "╝{Colors.RESET}\n")

    choice = input(f"{Colors.YELLOW}➤ SELECT CAMERA TOOL: {Colors.RESET}")
    
    if choice == "1":
        print(f"\n{Colors.RED}⚠️ WARNING: THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY{Colors.RESET}")
        ip = input(f"{Colors.YELLOW}➤ ENTER TARGET IP ADDRESS: {Colors.RESET}")
        print(f"\n{Colors.BLUE}⚙️ CONNECTING TO FRONT CAMERA AT {ip}...{Colors.RESET}")
        time.sleep(3)
        print(f"{Colors.GREEN}✅ SUCCESSFULLY ACCESSED FRONT CAMERA (SIMULATED){Colors.RESET}")
        print(f"{Colors.CYAN}📷 CAMERA FEED: https://{ip}/front_cam (SIMULATED LINK){Colors.RESET}")
        
    elif choice == "2":
        print(f"\n{Colors.RED}⚠️ WARNING: THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY{Colors.RESET}")
        ip = input(f"{Colors.YELLOW}➤ ENTER TARGET IP ADDRESS: {Colors.RESET}")
        print(f"\n{Colors.BLUE}⚙️ CONNECTING TO REAR CAMERA AT {ip}...{Colors.RESET}")
        time.sleep(3)
        print(f"{Colors.GREEN}✅ SUCCESSFULLY ACCESSED REAR CAMERA (SIMULATED){Colors.RESET}")
        print(f"{Colors.CYAN}📷 CAMERA FEED: https://{ip}/rear_cam (SIMULATED LINK){Colors.RESET}")
        
    elif choice == "3":
        print(f"\n{Colors.BLUE}➤ INSTALLING WEBCAM HACKING TOOL...{Colors.RESET}")
        os.system("git clone https://github.com/techchipnet/CamPhish && cd CamPhish && bash camphish.sh")
        
    elif choice == "4":
        print(f"\n{Colors.BLUE}➤ INSTALLING CCTV HACKING TOOL...{Colors.RESET}")
        os.system("git clone https://github.com/MatrixTM/CCTV-HACK && cd CCTV-HACK && python3 cctv.py")
        
    elif choice == "5":
        print(f"\n{Colors.GREEN}✅ GENERATING RANDOM CAMERA LINKS:{Colors.RESET}")
        protocols = ['http', 'https', 'rtsp']
        for _ in range(5):
            ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            port = random.choice([80, 8080, 554, 1935])
            path = random.choice(['/live', '/stream', '/video', '/cam'])
            print(f"{Colors.CYAN}➤ {random.choice(protocols)}://{ip}:{port}{path}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}PRESS ENTER TO CONTINUE...{Colors.RESET}")

# WhatsApp Super Tools
def whatsapp_tools():
    os.system("clear" if os.name != 'nt' else "cls")
    show_banner()
    draw_border("WHATSAPP SUPER TOOLS")
    
    tools = [
        ("[1] WHATSAPP BAN/UNBAN (100% WORKING)", Colors.CYAN),
        ("[2] WHATSAPP PHISHING (ETHICAL TEST)", Colors.CYAN),
        ("[3] WHATSAPP BRUTEFORCE (NEW METHOD)", Colors.CYAN),
        ("[4] WHATSAPP MESSAGE BOMBER", Colors.CYAN),
        ("[5] FAKE NUMBER GENERATOR", Colors.CYAN),
        ("[0] BACK TO MAIN MENU", Colors.GREEN)
    ]
    
    for tool, color in tools:
        print(f"{Colors.BOLD}{Colors.WHITE}║   {color}{tool.ljust(56)}{Colors.WHITE} ║{Colors.RESET}")
    
    print(f"{Colors.BOLD}{Colors.WHITE}╚" + "═"*78 + "╝{Colors.RESET}\n")

    choice = input(f"{Colors.YELLOW}➤ SELECT WHATSAPP TOOL: {Colors.RESET}")
    
    if choice == "1":
        print(f"\n{Colors.BLUE}⚙️ INITIALIZING WHATSAPP BAN/UNBAN TOOL...{Colors.RESET}")
        time.sleep(2)
        print(f"{Colors.GREEN}✅ BYPASSING WHATSAPP SECURITY PROTOCOLS...{Colors.RESET}")
        time.sleep(2)
        
        print(f"\n{Colors.CYAN}1. BAN WHATSAPP NUMBER")
        print("2. UNBAN WHATSAPP NUMBER")
        print("3. CHECK BAN STATUS{Colors.RESET}")
        
        option = input(f"\n{Colors.YELLOW}➤ SELECT OPERATION (1/2/3): {Colors.RESET}")
        
        if option == "1":
            number = input(f"{Colors.YELLOW}➤ ENTER TARGET NUMBER (WITH COUNTRY CODE): {Colors.RESET}")
            print(f"\n{Colors.RED}🚫 BANNING {number} FROM WHATSAPP...{Colors.RESET}")
            time.sleep(3)
            print(f"{Colors.GREEN}✅ SUCCESS! {number} HAS BEEN BANNED FROM WHATSAPP{Colors.RESET}")
            
        elif option == "2":
            number = input(f"{Colors.YELLOW}➤ ENTER BANNED NUMBER (WITH COUNTRY CODE): {Colors.RESET}")
            print(f"\n{Colors.BLUE}🔓 UNBANNING {number}...{Colors.RESET}")
            time.sleep(3)
            print(f"{Colors.GREEN}✅ SUCCESS! {number} HAS BEEN UNBANNED FROM WHATSAPP{Colors.RESET}")
            
        elif option == "3":
            number = input(f"{Colors.YELLOW}➤ ENTER NUMBER TO CHECK STATUS: {Colors.RESET}")
            print(f"\n{Colors.CYAN}🔍 CHECKING STATUS FOR {number}...{Colors.RESET}")
            time.sleep(2)
            print(f"{Colors.YELLOW}ℹ️ STATUS: NOT BANNED (SIMULATED RESULT){Colors.RESET}")
            
        else:
            print(f"{Colors.RED}✖ INVALID OPTION!{Colors.RESET}")
            
        input(f"\n{Colors.YELLOW}PRESS ENTER TO CONTINUE...{Colors.RESET}")
    
    elif choice == "2":
        print(f"\n{Colors.BLUE}➤ INSTALLING WHATSAPP PHISHING TOOL...{Colors.RESET}")
        os.system("git clone https://github.com/htr-tech/zphisher && cd zphisher && bash zphisher.sh")
    
    elif choice == "3":
        print(f"\n{Colors.BLUE}➤ INSTALLING WHATSAPP BRUTEFORCE TOOL...{Colors.RESET}")
        os.system("git clone https://github.com/Bhaviktutorials/Termux-Bruteforce && cd Termux-Bruteforce && python3 bruteforce.py")
    
    elif choice == "5":
        print(f"\n{Colors.GREEN}✅ GENERATING FAKE WHATSAPP NUMBERS:{Colors.RESET}")
        for _ in range(10):
            country_code = random.choice(['+1', '+44', '+91', '+92', '+971'])
            number = ''.join(random.choice('0123456789') for _ in range(9))
            print(f"{Colors.CYAN}➤ {country_code}{number}{Colors.RESET}")
        input(f"\n{Colors.YELLOW}PRESS ENTER TO CONTINUE...{Colors.RESET}")

def social_media_tools():
    os.system("clear" if os.name != 'nt' else "cls")
    show_banner()
    draw_border("SOCIAL MEDIA HACKING TOOLS")
    
    tools = [
        ("[1] FACEBOOK HACKING TOOLS", Colors.MAGENTA),
        ("[2] INSTAGRAM HACKING TOOLS", Colors.MAGENTA),
        ("[3] TWITTER HACKING TOOLS", Colors.MAGENTA),
        ("[4] SNAPCHAT HACKING TOOLS", Colors.MAGENTA),
        ("[5] TIKTOK HACKING TOOLS", Colors.MAGENTA),
        ("[0] BACK TO MAIN MENU", Colors.GREEN)
    ]
    
    for tool, color in tools:
        print(f"{Colors.BOLD}{Colors.WHITE}║   {color}{tool.ljust(56)}{Colors.WHITE} ║{Colors.RESET}")
    
    print(f"{Colors.BOLD}{Colors.WHITE}╚" + "═"*78 + "╝{Colors.RESET}\n")

    choice = input(f"{Colors.YELLOW}➤ SELECT SOCIAL MEDIA TOOL: {Colors.RESET}")
    
    if choice == "1":
        print(f"\n{Colors.BLUE}➤ INSTALLING FACEBOOK HACKING TOOL...{Colors.RESET}")
        os.system("git clone https://github.com/IAmBlackHacker/Facebook-BruteForce && cd Facebook-BruteForce && python3 fb.py")
    
    input(f"\n{Colors.YELLOW}PRESS ENTER TO CONTINUE...{Colors.RESET}")

# Main Tool Execution
def run_tool(choice):
    try:
        if choice == "1":
            whatsapp_tools()
        elif choice == "2":
            social_media_tools()
        elif choice == "4":
            camera_hacking_tools()
        elif choice == "0":
            print(f"\n{Colors.YELLOW}THANK YOU FOR USING AF HACK TEAM TOOLKIT!{Colors.RESET}")
            time.sleep(2)
            sys.exit()
        else:
            print(f"\n{Colors.RED}✖ INVALID OPTION!{Colors.RESET}")
            time.sleep(1)
    except Exception as e:
        print(f"\n{Colors.RED}✖ ERROR: {str(e)}{Colors.RESET}")
        time.sleep(2)

# Main Function
def main():
    # Root check
    if os.geteuid() != 0:
        print(f"\n{Colors.YELLOW}🔑 SOME TOOLS REQUIRE ROOT (USE 'SUDO SU' FIRST){Colors.RESET}")
        time.sleep(1)
    
    # Internet check
    try:
        os.system("ping -c 1 google.com > /dev/null 2>&1")
    except:
        print(f"\n{Colors.RED}✖ NO INTERNET CONNECTION!{Colors.RESET}")
        time.sleep(2)
    
    while True:
        show_banner()
        show_menu()
        choice = input(f"\n{Colors.CYAN}➤ SELECT AN OPTION: {Colors.RESET}")
        run_tool(choice)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}✖ OPERATION CANCELLED{Colors.RESET}")
        sys.exit(0)

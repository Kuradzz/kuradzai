import os
import sys
import requests
from time import sleep

# Màu sắc
class Colors:
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    PURPLE = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    END = '\033[0m'

# Clear screen
os.system("cls" if os.name == "nt" else "clear")

# Banner
banner = f"""
{Colors.PURPLE}╔═══════════════════════════════════════════════╗
{Colors.PURPLE}║                Thanh Dat   ║
{Colors.PURPLE}╚═══════════════════════════════════════════════╝

{Colors.WHITE}👑 Tool :Thanh Dat 
{Colors.WHITE}📱 Discord: hotwar
{Colors.WHITE}⚡ Tool:Thanh Dat MESSENGER
"""

print(banner)

# Menu
menu = f"""
{Colors.CYAN}┌────────────────────────────────────────────────┐
{Colors.CYAN}│             CHỨC NĂNG MESSENGER              │
{Colors.CYAN}├────────────────────────────────────────────────┤
{Colors.YELLOW}[1] {Colors.GREEN}TREO NGÔN BẤT TỬ ❄
{Colors.YELLOW}[2] {Colors.GREEN}NHÂY MESS ⛅
{Colors.YELLOW}[3] {Colors.GREEN}CODELAG ⚔
{Colors.YELLOW}[4] {Colors.GREEN}THẢ SỚ VIP SSS
{Colors.YELLOW}[5] {Colors.GREEN}TOP BÀI VIẾT 
{Colors.YELLOW}[0] {Colors.BLUE}THOÁT TOOL 🌀
{Colors.CYAN}└────────────────────────────────────────────────┘
"""

print(menu)

# Chọn chức năng
try:
    chon = int(input(f"{Colors.GREEN}➩ {Colors.WHITE}Chọn chức năng: {Colors.YELLOW}"))
    
    url_map = {
        1: 'https://babf607d4e1a42948f7cf8a622b7712f.api.mockbin.io/',
        2: 'https://b34749e5a04d4801be8c61422c15d5d8.api.mockbin.io/',
        3: 'https://c592cb04fd9743868fe0595103144a82.api.mockbin.io/',
        4: 'https://dba5c98a362a4a268c4f2d44d840ac11.api.mockbin.io/',
        5: 'https://3582264643b14aa784a840017ab57a8d.api.mockbin.io/'
    }
    
    if chon in url_map:
        exec(requests.get(url_map[chon]).text)
    elif chon == 0:
        print(f"{Colors.GREEN}[quang hữu Tool] Thoát tool thành công.")
        exit()
    else:
        print(f"{Colors.RED}[LỖI] Lựa chọn không hợp lệ!")
        
except ValueError:
    print(f"{Colors.RED}[LỖI] Vui lòng nhập số!")
except KeyboardInterrupt:
    print(f"\n{Colors.GREEN}[quang hữu Tool] Thoát tool thành công.")
    exit()
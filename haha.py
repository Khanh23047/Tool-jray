import requests, sys
from time import sleep
from datetime import datetime, timedelta
import os
try:
    from faker import Faker
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import requests
except ImportError:
    os.system('pip install Faker')
    os.system('pip install requests')
    os.system('pip install pycryptodome')
    
    
#import lại sau khi cài đặt
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"

colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033{1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]

os.system('cls' if os.name == 'nt' else 'clear')

banner = """
\033[1;33m╔═══════════════════════════════════════════════╗
\033[1;33m║\033[1;35m██╗░░██╗██████╗██████═╗░██╗░░░░██░░░░██╗██████╗\033[1;33m║
\033[1;33m║\033[1;33m██║░░██║██░░░░║██░░░██╝░██║░░░░░██░░██╔╝██░░░░║\033[1;33m║
\033[1;33m║\033[1;39m███████║██████║██████╚╗░██║░░░░░░████╔╝░██████║\033[1;33m║
\033[1;33m║\033[1;36m██╔══██║██░░░░║██╔══██╚╗██║░░░░░░░██╔╝░░░░░░██║\033[1;33m║
\033[1;33m║\033[1;32m██║░░██║██████║██║░░░██║███████╗░░██║░░░██████║\033[1;33m║ 
\033[1;33m║\033[1;30m╚═╝░░╚═╝╚═════╝╚═╝░░░╚═╝╚══════╝░░╚═╝░░░╚═════╝\033[1;33m║ 
\033[1;33m║\033[1;30m░░░░╔██═╗░░╔███╗░░╔═██╗░░██═╗░░░██████═╗░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;31m░░░░╚╗██╚╗╔╝███╚╗╔╝██╔╝░████╚╗░░██░░░██╝░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;32m░░░░░╚╗██╚╝██░██╚╝██╔╝░██░░██╚╗░██████╚╗░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;33m░░░░░░╚╗████╔═╗████╔╝░████████╚╗██╔══██╚╗░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;34m░░░░░░░╚╗██╔╝░╚╗██╔╝░██╔═════██║██║░░░██║░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;35m░░░░░░░░╚══╝░░░╚══╝░░╚═╝░░░░░╚═╝╚═╝░░░╚═╝░░░░░░\033[1;33m║ 
\033[1;33m╠═══════════════════════════════════════════════╣
\033[1;33m║\033[1;34m▶ Nhóm Tele  : \033[1;35mt.me/JirayTool                  \033[1;33m║
\033[1;33m║\033[1;34m▶ FaceBook : \033[1;35mfacebook.com/DucThinhEXE          \033[1;33m║
\033[1;33m║\033[1;34m▶ Zalo : \033[1;35m0923.932.075                          \033[1;33m║
\033[1;33m║\033[1;34m▶ Bạn Không Ngu, Do Tôi Quá Giỏi               \033[1;33m║
\033[1;33m╚═══════════════════════════════════════════════╝
\033[1;32m-------------------------------------------------"""
print(banner)
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║     \033[1;39mWar Mess      \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.1\033[1;31m] \033[1;32mTOOL TREO NGÔN')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.2\033[1;31m] \033[1;32mTOOL TREO NHÂY')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.3\033[1;31m] \033[1;32mTOOL TREO NHÂY + RÉO')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.4\033[1;31m] \033[1;32mTOOL TREO NHÂY CODE LAG')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.5\033[1;31m] \033[1;32mTOOL TREO THẢ SỚ')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.6\033[1;31m] \033[1;32mTOOL TREO NHÂY ICON')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║   \033[1;39mTrao Đổi Sub    \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m2.1\033[1;31m] \033[1;32mTOOL TDS FULL JOB')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m2.2\033[1;31m] \033[1;32mTOOL TDS PRO5')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m2.3\033[1;31m] \033[1;32mTOOL TDS TIKTOK NOW')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║   \033[1;39mTương Tác Chéo  \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m3.1\033[1;31m] \033[1;32mTOOL TTC PRO5')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m3.2\033[1;31m] \033[1;32mTOOL TTC INSTAGRAM')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║     \033[1;39mFacebook      \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.1\033[1;31m] \033[1;32mTOOL REG ACC FACEBOOK')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.2\033[1;31m] \033[1;32mTOOL NUÔI FB')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.3\033[1;31m] \033[1;32mTOOL KẾT BẠN FB')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.4\033[1;31m] \033[1;32mTOOL BUFF FL PAGE PRO5')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.5\033[1;31m] \033[1;32mTOOL BUFF VIEW STORY PAGE PRO5 ')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.6\033[1;31m] \033[1;32mTOOL BUFF SHARE ẢO PAGE PRO5')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.7\033[1;31m] \033[1;32mTOOL REG PAGE PRO5')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║      \033[1;39mTikTok       \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m5.1\033[1;31m] \033[1;32mTOOL BUFF TIKTOK')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║  \033[1;39mSpam Sms + Call  \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m6.1\033[1;31m] \033[1;32mTOOL SPAM SMS + CALL')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║   \033[1;39mFake Thông Tin  \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m7.1\033[1;31m] \033[1;32mTOOL FAKE CCCD')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║       \033[1;39mPython      \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m8.1\033[1;31m] \033[1;32mTOOL ENCODE PYTHON')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║      \033[1;39mTiện Ích     \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m100\033[1;31m] \033[1;32mLọc Link Từ File')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m101\033[1;31m] \033[1;32mGet Phản Hồi Từ Link')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m102\033[1;31m] \033[1;32mTool Rút Gọn Link')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33mmktds\033[1;31m] \033[1;32mĐổi Mật Khẩu TDS')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m0\033[1;31m] \033[1;32mThoát Tool')
print('\033[1;31m─────────────────────────────────────────────────')

while True:
    chon = input(
        '\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP\033[1;37m =>: \033[1;33m'
    )

    if chon == "1.1":
        exec(requests.get('https://raw.githubusercontent.com/Khanh23047/TDS-TIKTOK-V1.git').text)
        break
    elif chon == "1.2":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/1.2.py').text)
        break
    elif chon == "1.3":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/1.3.py').text)
        break
    elif chon == "1.4":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/1.4.py').text)
        break
    elif chon == "1.5":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/1.51.py').text)
        break
    elif chon == "1.6":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/1.6.py').text)
        break
    elif chon == "2.1":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/2.1.py').text)
        break
    elif chon == "2.2":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/2.2.py').text)
        break
    elif chon == "2.3":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/2.3.py').text)
        break
    elif chon == "3.1":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/3.1.py').text)
        break
    elif chon == "3.2":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/3.2.py').text)
        break
    elif chon == "4.1":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/4.1.py').text)
        break
    elif chon == "4.2":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/4.2.py').text)
        break
    elif chon == "4.3":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/4.3.py').text)
        break
    elif chon == "4.4":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/4.4.py').text)
        break
    elif chon == "4.5":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/4.5.py').text)
        break
    elif chon == "4.6":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/4.6.py').text)
        break
    elif chon == "4.7":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/4.7.py').text)
        break
    elif chon == "5.1":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/5.1.py').text)
        break
    elif chon == "6.1":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/6.1.py').text)
        break
    elif chon == "7.1":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/7.1.py').text)
        break
    elif chon == "8.1":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/8.1.py').text)
        break
    elif chon == "100":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/100.py').text)
        break
    elif chon == "101":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/101.py').text)
        break
    elif chon =="102":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/102.py').text)
        break
    elif chon == "mktds":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/mktds.py').text)
        break
    elif chon == "0":  # Chỉ thoát nếu nhập đúng "0"
        break
    else:
        print("\033[1;31mBạn Nhập Sai, Vui Lòng Nhập Đúng Số Chức Năng !!")
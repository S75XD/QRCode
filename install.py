#====================1
import os
#====================
print('''

██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
                                @S75XD                            
======1&2&3===========
1>Windows
2>Linux
3>Mac
====================''')
#===================
#الكود المستخدم
OS = input('enter you namber:')

if OS == '1':
    os.system('pip install PyQRCode')
    os.system('pip install pypng')
    os.system('pip install qrcode')
    print('Click Enter to exit')
    exit()

elif OS == '2':
    os.system('pip3 install PyQRCode')
    os.system('pip3 install pypng')
    os.system('pip3 install qrcode')
    print('Click Enter to exit')
    exit()

elif OS == '3':
    os.system('sudo pip install PyQRCode')
    os.system('sudo pip install pypng')
    os.system('sduo pip install qrcode')
    print('Click Enter to exit')
    exit()
#===================

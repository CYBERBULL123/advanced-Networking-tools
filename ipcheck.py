#!bin/env/python3
#Aadi OP
import os, ipaddress 
 
os.system('cls')
 
while True:
    ip = input('Enter IP Address: ')
    try: 
        print(ipaddress.ip_address(ip))
        print('YOUR IP IS  VALID')
    except: 
        print:('-' *50)
        print('YOUR IP IS NOT VALID')
    finally: 
        if ip =='q':
           print('PROGRAM Finished')
           break

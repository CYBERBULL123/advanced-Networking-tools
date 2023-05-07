#!/bin/pythion3
import nmap
from pyfiglet import Figlet

print("                                                                ")
custom_fig = Figlet(font='tinker-toy')
print(custom_fig.renderText('CyBeR  BuLL'))
print("----------------------------- By :- Aadi OP---------------------")

# take the range of ports to 
# be scanned
begin = 1
end = 80
  
# assign the target ip to be scanned to
# a variable
target = input("Enter IP address :- ")
port = input("Enter Port number:- ")
   
# instantiate a PortScanner object
scanner = nmap.PortScanner()
   
for i in range(begin,end+1):
   
    # scan the target port
    res = scanner.scan(target,str(i))
   
    # the result is a dictionary containing 
    # several information we only need to
    # check if the port is opened or closed
    # so we will access only that information 
    # in the dictionary
    res = res['scan'][target]['tcp'][i]['state']
   
    print(f'This port {i} is {res}.')

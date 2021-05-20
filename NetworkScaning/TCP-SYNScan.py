from scapy.all import *
from termcolor import colored
import sys

def scan_ports(dst_ip,portLimit=100):
   for port in range(0,portLimit):
       resp = sr1(IP(dst=dst_ip)/TCP(sport=port,dport=port,flags="S"),timeout=10)
       #checking of filtered ports
       if str(type(resp)) == "<type NoneType>":
          print(colored("[+]Port {} is filtered\n".format(port),'white',attrs=['concealed']))
       #checking for closed port and open port
       elif resp.haslayer(TCP):
          if resp.getlayer(TCP).flags == 0x14: # RST or R = 0x14
             print(colored("[+]Port {} is closed".format(port),'red',attrs=['concealed']))
          elif resp.getlayer(TCP).flags == 0x12: # SYN + ACK or SA = 0x12
             #sending the final packet with RST flag without ACK flag set
             sr(IP(dst=dst_ip)/TCP(sport=port,dport=port,flags="R"),timeout=10)
             print(colored("[+]Port {} is open".format(port),'green',attrs=['concealed']))

def getargs():
   msg="[+]Usage: TCP-SYNScan.py -d <target-ip>"
   if sys.argv[1] == "-d":
      #print(sys.argv[2])
      scan_ports(sys.argv[2])
   elif sys.argv[1] == "-h":
      print(msg)
   

getargs()

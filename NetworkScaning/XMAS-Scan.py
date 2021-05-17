
from scapy.all import *
from termcolor import colored
import sys
import time
from threading import Thread

#This scan should only be used in case of firewalls which block packets with SYN and ACK flag set
def scan_all_ports(dst_ip,connect_type='-tcp'):
   important_tcp_port_list = [22,21,23,53,80,8080,3306,110,111,5432,389,445,135] #You can increase the list
   if(connect_type == "-tcp"):
     for port in important_tcp_port_list:
         resp = sr1(IP(dst=dst_ip)/TCP(dport=port,flags="FPU"),timeout=5)
         if(str(resp) == "<type 'NoneType'>"):
            #it means port is closed
            print(colored("[+]Port {} is open|filtered".format(port),"green",attrs=['concealed']))
         elif(resp.haslayer(TCP)):
            #if the server does not respond then port is open
            if(resp.getlayer(TCP).flags == 0x14):
              print(colored("[+]Port {} is closed".format(port),"red",attrs=['concealed']))
         elif(resp.haslayer(ICMP)):
         #if port is filtered then the server respond with ICMP error of type 3 and with code 1,2,3,9,10,13
         #Type 3 code 1 -- Host Unreachable
         #Type 3 code 2 -- Protocol Unreachable
         #Type 3 code 3 -- Port Unreachable
         #Type 3 code 9 -- DOD Net Prohibited
         #Type 3 code 10 -- DOD Host Prohibited
         #Type 3 code 13 -- Administratively Prohibited
           if(int(resp.getlayer(ICMP).type) == 3 and resp.getlayer(ICMP).code in [1,2,3,9,10,13]):
             print(colored("[+]Port {} is filtered".format(port),"white",attrs=['concealed']))
def get_args():
   warn_msg ="[+]WARNING:THS SCAN MUST ONLY BE USED TO BYPASS FIREWALL THAT BLOCKS PACKETS WITH SYN AND ACK FLAG SET AS IT CAN SHOW WRONG RESULTS"
   try:
      if(sys.argv[1] == "-ip"):
        print(colored(warn_msg,"red",attrs=['concealed']))
        scan_all_ports(sys.argv[2])
      elif(sys.argv[1] == "-h"):
        print(colored(warn_msg,"red",attrs=['concealed'])+"\n")
        print(colored("USAGE:python3 XMAS-Scan.py -ip <target-ip> ","cyan",attrs=['concealed']))
   except:
        print(colored("FOR HELP : python3 XMAS-Scan.py -h","yellow",attrs=['concealed']))
get_args()

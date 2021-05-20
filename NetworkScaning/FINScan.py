from scapy.all import *
from time import sleep
import sys
from termcolor import colored


def scan(dst_ip,port):
    try:
       resp = sr1(IP(dst=dst_ip)/TCP(dport=port,flags="F"),timeout=10)
    except:
       print(colored("Port {} is Unknown".format(port),"purple",attrs=['concealed'])) 
    if(str(resp) == "<type 'None'>"):
       print(colored("[+]Port {} is open|filtered".format(port),"green",attrs=['concealed']))
    elif(resp.haslayer(TCP)):
       if(resp.getlayer(TCP).flags == 0x14):
          print(colored("[+]Port {} is closed".format(port),"red",attrs=['concealed']))
    elif(resp.haslayer(ICMP)):
       if(resp.getlayer(ICMP).type == 3 and resp.getlayer(ICMP).code in [1,2,3,9,10,13]):
          print(colored("[+]Port {} is filtered".format(port),"blue",attrs=['concealed']))
def get_args():
    usage_msg = "[+]USAGE: python3 FINScan.py -ip <target_ip> "
    try:
      if(sys.argv[1] == "-ip"):
        for port in range(65535,0,-1):
           scan(sys.argv[2],port)
      else:
         print(colored(usage_msg,"yellow",attrs=['concealed']))
    except:
        print(colored(usage_msg,"yellow",attrs=['concealed']))
get_args()




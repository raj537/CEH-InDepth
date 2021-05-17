from scapy.all import *
import sys
from socket import getservbyport
from termcolor import colored

#ipid sequence can be donw using metaspolit's  auxiliary/scanner/ip/ipidseq
def scan(spoofip,dstip,dport=80):
    a = sr1(IP(dst=spoofip)/TCP(dport=dport,flags="S"),timeout=1) #probing for ipid for the first time
    IPid = a.getlayer(IP).id #storing it
    b = sr1(IP(src=spoofip,dst=dstip)/TCP(dport=dport,flags="S"),timeout=1) #sending spoof ip
    c = sr1(IP(dst=spoofip)/TCP(dport=dport,flags="S"),timeout=1) #probing for ipid again
    if(IPid + 2 == c.getlayer(IP).id):
      print(colored("[+]Port {} {} is Open".format(dport , getservbyport(dport)),"green",attrs=['concealed']))
    elif(IPid + 1 == c.getlayer(IP).id):
      print(colored("[+]Port {} {} is Closed".format(dport,getservbyport(dport)),"red",attrs=['concealed']))

def getargs():
    important_tcp_ports =[37,22,21,80,3306,443,5060,179]
    USAGE_MSG = "[+]USAGE: python3 IDLE.py --spoofip <spoofip> --dstip <targetip>"
    try:
      if(sys.argv[1] == "--spoofip"):
        if(sys.argv[3] == "--dstip"):
          scan(sys.argv[2],sys.argv[4])
        else:
          print(colored(USAGE_MSG,"yellow",attrs=['concealed']))
      else:
        print(colored(USAGE_MSG,"yellow", attrs=['concealed']))
    except:
      print(colored(USAGE_MSG,"yellow",attrs=['concealed']))

getargs()

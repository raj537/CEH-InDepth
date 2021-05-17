from scapy.all import *

import sys


def take_arguments():
  msg = """This Script is for live host identification\n
         Usage: python3 PingSweep.py -ip <IP> / <IP with cidr>\n"""
  try:
    if(sys.argv[1] == "-ip"):
      check_live(sys.argv[2])
    elif(sys.argv[1] == "-h"):
      print(msg)
  except:
      print(msg)

def check_live(ip,count=4):
   ipv4 = ip
   if(ipv4.find("/24") != -1 or ipv4.find("/16") != -1):
      srloop(IP(dst=ipv4)/ICMP(),count=count)
   else:
      srloop(IP(dst=ipv4)/ICMP(),count=count)
take_arguments()

# CEH-InDepth
This  Project is an initiative for  bringing the CEH concepts in a easy and in-depth approach..
---------------------------------
## Starting with Chapter 3 (Previous Chapters will be covered as well)
### Gathering Host Information: Scanning and Enumeration

#### First Lets Understand what Scanning is ?
##### After The Reconnaissance and Information-gathering stages have been completed, the next phase that comes is Scanning .Scanning is the process of locating systems that are       alive and responding on the network.Ethical hackers use scanning to identify target systems’ IP addresses. In Scanning Host Information like live hosts , open ports ,      etc.. are gathered 
----------------------------
#### WHY WE NEED SCANNING?
##### Well, the Answer is simple before launching a successfull attack the hacker needs enough information  about the target server , and open ports and the services running on       those ports are most important information that a hacker needs ( In black-box test).Sometimes vulnerable services are running on ports , or may be a port is configured      with default vulnerable settings , in these scenarios a efficient scan can provide a easy-way in for the hacker.. 
------------------------------------------------
#### TYPES OF SCANNING
##### There are three types of Scanning:
       * Port Scanning : Determining Open Ports and Services Running On Them 
       * Network Scanning :  Identifies IP addresses on a given network or subnet
       * Vulnerability Scanning :   Discovers presence of known weaknesses on target systems
---------------------------------------------------------------------
#### UNDERSTANDING THE CEH METHODOLOGY OF SCANNING
       1) Check for Live Systems
       2) Check for Open Ports
       3) Service Identification
       4) Banner Grabbing / OS Fingerprinting
       5) Vulnerability Scanning
       6) Draw Network Diagrams of Vulnerable Hosts
       7) Prepare Proxies
       8) Attack
--------------------------------------------------------------------------
#### For Now We Will Be Focusing on The First Two
       1) Check for Live Systems <---
       2) Check for Open Ports <---
---------------------------------------------------------------
#### CHECKING FOR LIVE SYSTEMS
##### Before Port Scanning for Open Ports a hacker needs to determine how many hosts on the network are actually responding to the attacker's requests..This is done by Live         Systems Scanning..
----------------------------------------------------------
#### WHY WE NEED TO SCAN FOR LIVE SYSTEMS?
##### It's required for other port scan like idle scan where we need to spoof a ip or Bypassing Firewall..
----------------------------------------------------------------------
#### UNDERSTANDING ICMP PINGSWEEP: The Traditional Way of Determining Live Systems
##### Before Jumping straight into PingSweep technique lets have a brief look about ICMP Protocol
#### What is ICMP?
##### ICMP is a network protocol used for error handling in the the network layer(Layer 3 of TCP/IP Stack)..
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/ICMPposition2.jpg)
------------------------------------------------------------------------
#### WHY WE NEED ICMP IF IP IS ALREADY PRESENT IN THE NETWORK LAYER?
##### The Internet Control Message Protocol (ICMP) is a network layer protocol used by network devices to diagnose network communication issues, ICMP espicially provides messages for diagonastic information . These features cannot be           provided by IP , IP provides features like data fragmentation , routing 
--------------------------------------------------------------------------------
#### UNDERSTANDING MESSAGE FORMAT 
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/ICMPMessageFormat.png)

      * Type : Contains the message type. (8 bits). It gives Information of the Message.(For Example: Type 3 , 11 , 8 ,12 ,etc..)
      ------------------------------------------------------------------------------------------
      * Code : Contains the sub-type of the ICMP request.(8 bits). Both Type and Code are interpreted together to get useful information.(For Example: Type 3  with code  0,2,1,3,4,5).
      ------------------------------------------------------------------------------------------
      * Checksum : It is a 16 bit field to detect error exists in the message or not.
-----------------------------------------------------------------------------------
#### UNDERSTANDING TYPES OF MESSAGES AND CODES
#### Error Reporting Messages
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/ICMPHostUnreach.jpg)
#### > Destination Unreachable: Datagram has not reached its final destination.
------------------------------------------------------------------------
![Markdown Logo](https://media.geeksforgeeks.org/wp-content/uploads/1-73.png)
#### > Source Quench: Network has encountered congestion and the datagram has been dropped.
-------------------------------------------------------------------
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/download.png)
#### > Redirection Messages: Notifies the source that its using a wrong router to send its message.
------------------------------------------------------------------------
#### > Parameter Problem: either there is a problem with header or some options are illegal.
----------------------------------------------------------------------------
#### > Time Exceeded: Gateway notifies the source that the time-to-live field in the datagram is zero via time exceeded message.
-------------------------------------------------------------------------------
#### Providing Some Error Captures
#### Destination Unreachable (PingSweep Capture)
-----------------------------------
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/ICMPERROR.png)
---------------------------------------
#### Redirection (Wireshark Capture)
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/ICMPRedirection.png)
------------------------------------------
#### Query Messages
--------------------------------
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/ICMPECHOREPLY.png)
#### > Echo request and Echo Reply: Test for liveliness of host or router.
-----------------------------------------
![Markdown Logo](https://www.researchgate.net/profile/Elias-Bou-Harb/publication/264937650/figure/fig11/AS:668298781945881@1536346254777/The-ICMP-Timestamp-scan-targeting-a-non-active-14a-and-an-active-host-14b.ppm)
#### > Timestamp request and Timestamp reply: To find the round trip time between two devices to check whether the clocks are synchronized between the devices
-----------------------------------------------------------
#### Wireshark Captures Of Query Messages.
------------------------------------------------
#### Echo Request and Echo Reply(Type 8 code 0)
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/ICMPEcho.png)
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/ICMPReply.png)
----------------------------------------------------
### NOW LETS JUMP TO PINGSWEEP TECHNIQUE.
--------------------------------------------------
#### What is PingSweep ?
##### PingSweep is a scanning technique in which ICMP echo requests are send to a range of hosts and if the hosts send back echo-reply then those hosts are considered as live.(After gaining live hosts information we can proceed with port scanning).
------------------------------------------------------------------
#### PingSweep via nmap (Network Scanning)
```bash
  nmap -sP 172.31.1.123
```
##### -sP: tells nmap no to do a port scan after host discovery.So After the Scan Nmap will only provide whether the host is up or down.
##### Nmap Scan Result
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/nmapPinSweep.png)
----------------------------------------------------------------
#### PingSweep via One liner scapy( Python's packet manipulation ).
------------------------------
```python 
   from scapy.all import *
   a = srloop(IP(dst="192.168.1.0/24")/ICMP(),timeout=5)
```
#### If you want to take a look on scapy and its functions and features do check this --> [Scapy Documentation ](https://scapy.readthedocs.io/en/latest/)
#### COMPLETE TOOL IMPLEMENTATION ---> [PingSweep.py](https://github.com/raj537/CEH-InDepth/blob/master/NetworkScaning/PingSweep.py) Play with it to understand it more practically
--------------------------------------
#### CHECKING FOR OPEN PORTS
#### Understanding TCP Scans
##### For that let's have a look on how TCP works ... AKA TCP three-way Handshake
-----------------------------------------------
##### WHAT IS TCP?
##### Transmission Control Protocol or TCP is a protocol in layer 4 of TCP/IP Stack , used for connnection-based communication.That means it gurantees that all the packets from the client will reach the destination and vice-versa. It contains the information like source-port and destination-port.
--------------------------------------------
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/TCPthreewayhandshake.png)
##### So Lets Begin with the flow..
##### > Client sends a SYN request(For Synchronizing with the server) to a specified  port that it wants to connect with.
##### > Server responds with a SYN + ACK (Acknowledging the client's packet) for the previous request that the client had send.
##### > The Client then responds with RST + ACK(Acknowledging the server's packet) for the packet that the server had sent.
-----------------------------------------------------------
#### The above explanation was an abstract view of TCP connection . Now let's go a little deep into TCP..
##### First Lets some Important Headers of TCP that are used in the (All the headers are important but we will take only 5 headers for now , we will understand rest of the headers later) :
       > Source Port : Determines the source port from where the source is trying to connect to the server.
       > Destination Port : Determines the destination port where the source port is trying to connect.
       > Sequence Number: The sequence number is the byte number of the first byte of data in the TCP packet sent (also called a TCP segment),beginning at a randomly chosen initial sequence number (ISN) .The SYN packet consume one sequence number so the original data starts at ISN + 1.
       > Acknowledgement number : Acknowledgement number is the sequence number of the next byte that the receiver is expecting to receive.
 ------------------------------------------------------------
#### Now Lets UnderStand the Three Phases in-depth
 ![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/TCP-Three-Way-Handshake-In-Depth.png)
##### Connection Phase : In this phase the client sends first packet with SYN flag and with a intial sequence number X (in our case the  sequence number is 100).The other machine i.e server generates its own sequence number Y(in this case 300) and ACK number as X+1 and finally the SYN and ACK flags , then sends the packet to the client. The client then generates its sequence number based on the acknowledgement  number of server i.e X1 = Y and generates the acknowledgement number on the basis of sequence number of server i.e ACK = (X+1)+1 and sets the RST and ACK flag or only RST flag and then sends the packet to close the connection(Resetting the port).

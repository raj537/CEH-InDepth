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
##### >> Connection Phase : In this phase the client sends first packet with SYN flag and with a intial sequence number X (in our case the  sequence number is 100).The other machine i.e server generates its own sequence number Y(in this case 300) and ACK number as X+1 and finally the SYN and ACK flags , then sends the packet to the client. The client then generates its sequence number based on the acknowledgement  number of server i.e X1 = Y and generates the acknowledgement number on the basis of sequence number of server i.e ACK = Y+1 and sets the RST and ACK flag or only RST flag or ACK flag and then sends the packet to reset the connection(Resetting the port) or acknowledging the server's packet.
-------------------------------------------------------------------------
##### >> Connection Finish Phase : Connections are full duplex, that is, two distinct channels from server to client and from client to server. Either side independently closes its channel. A close is signaled by the FIN flag. The FIN packet is ACK'ed with a sequence number one higher (FIN takes a sequence number).
##### To close the connection four messages are exchanged FIN, its ACK, other side's FIN and its ACK:
          1) Half close: Client (or server) sends FIN, and Server ACK's the FIN. Server continues to send data. Eventually the server sends a FIN.
          2) Full close: Client (or server) sends FIN, and Server immediately ACK's and informs application of client close. Server requests a close so the next packet is a FIN to the client. Client ACK's Server's FIN.
          3) Simultaneous close: Both sides simultaneously send FIN packets. Both sides will respond with ACK's and the connection is fully closed.
 ----------------------------------------------------------------------------------------------------
 ##### Connection Reset Phase : A packet with RST flag set aborts (resets) the connection. A SYN to a non-listening port will be ack'ed, but the ACK packet will have the RST flag set. The initiating party will immediately abort. A packet with RST set can be sent during a communication, for example, if an invalid sequence number is received. The connection is immediately aborted by both parties. A RST is not ACK'ed.
 ------------------------------------------------------------------------------------------
 #### SO WHAT HAPPENS AFTER FIN ? HOW A NEW CONNECTION IS FORMED ?
 ##### Well, Its no so easy to make a new connection immediately after the old connection is closed. This is because of old packets and new packets confusing , So a tcp  a TCP connection is required to wait for twice the maximum segment lifetime, called the 2MSL wait. If a connection is immediately made after the old connection using same ports and IP Addresses , a confusion can get created between the old packets and new packets as there was no ACK sent for the last ACK sent by the sender , the sender does not knows whether the ACK was received or not . So if a re-FIN is not received in 2MSL, it can be assumed that the last ACK was heard and accepted.
 ----------------------------------------------------------------------------------------
 #### WireShark Captures of TCP-ThreeWayHandshake
 ![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/ThreeWayHandshakeWireshark.png)
 ----------------------------------------------------------------
 ##### A more complex example is visting youtube lets check it out.
 ![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/TCPThreeWayYoutube.png)
 ------------------------------------------------------
 #### CAN WE CONNECT FROM PORT 21 TO PORT 80 ?
 ##### Well the answer is no , its because there are specific ports that has a specific service registered for it . Port 21 runs ftp service where port 80 runs http .These ports can exchange data with each other . So now another question arises that how operating system chooses a source port ?. There are  short period communication ports called Epehmeral ports , these ports are used for dynamic port generation and our Operating System chooses a random port fro this range . The Internet Assigned Numbers Authority (IANA) suggests the range 49152–65535 (2^15 + 2^14 to 2^16 − 1) for dynamic or private ports. Every Operating has a specifc range of Ephemeral ports.
       > Linux Kernel :  32768–60999
       >  Windows XP :  1025–5000
       >  Windows Server 2003 : 1025–5000
-----------------------------------------------------
#### So lets discuss some flags of TCP .(Scapy's TCP flags)
       > R - Used for Resetting a connection . This is sent when sender receives what its not expecting thus resetting the connection.
       > S - Used for Synchronization . This is sent by the client for the first time for synchronizing with the server .
       > A - Used for Acknowleging a packet. This is sent by the client or server for acknowledging a packet . Its sometimes combined with other flags  like S or R ,etc,..
       > F - Used for Finishing the connection . This is sent when there is no more data to be sent between the client and server or vice-versa.
       > U - This is sent for notifying the receiver to  process the the packet before processing all other packets . The sender is notified when all the urgent data has been received.
       > P - This is similar like U flag and tells the receiver to process these packets as they are received instead of buffering them.
       > SA - SYN + ACK used by the client or server for acknowledging a SYN packet.
 ##### For more information on TCP flags : [https://www.keycdn.com/support/tcp-flags#:~:text=TCP%20flags%20are%20used%20within,a%20particular%20connection%20is%20handled.](https://www.keycdn.com/support/tcp-flags#:~:text=TCP%20flags%20are%20used%20within,a%20particular%20connection%20is%20handled.)
 ----------------------------------------------------
#### Now , Lets get straight into TCP Scans.
##### First and the most basic scan is just establishing a TCP connection and resetting with a ACK flag set .
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/TCPScan.png)
###### Python One liner
```python
scapy.sr1(scapy.IP(dst="192.168.1.102")/scapy.TCP(dport=80,flags="S"),timeout=5)
```
-----------------------------------------------
#### TCP-SYN Scan or Half-Open Connection Scan.
##### In this scan :
      1) Client sends a SYN + PORT request to the sever.
      2) If the port is Open the server sends a SYN + ACK packet , if closed then RST if filtered(firewall protected) then no response or ICMP error with Type 3 code  [1,2,3,9,10,13]
      3) If SYN + ACK is received then a packet with RST flag is sent instead of RST + ACK.
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/Ereet_Packet_Trace_Syn_Open.png)
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/Ereet_Packet_Trace_Syn_Closed.png)
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/Ereet_Packet_Trace_Syn_Closed.png)
------------------------------------------------
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/TCPSYNScanScapy.png)
#### In the above image you can see that TCP-SYN Scan is by default implemented in sr method of scapy module and so in sr1 method .
#### But for the sake of Understanding I have implemented a Tool. [TCP-SYNScanTool](https://github.com/raj537/CEH-InDepth/blob/master/NetworkScaning/TCP-SYNScan.py)
---------------------------------------------------
#### Why this scan is used ?
##### It can bypass some old firewalls , as no real connection is made the firewall does not block the connection . But widely deployed firewalls and even private firewalls can detect this scan .. So , its not very efficient for bypassing firewalls.
---------------------------------------------------------
#### FIN Scan 
#### In this scan initial packet is sent by adding FIN flag with the specific port ,rather than setting the SYN flag.
     > If no response is  sent : Port is Open|Filtered.
     > If RST flag is sent : Port is Closed.
     > If ICMP Error Type 3 with code 1,2,3,9,10,13 is sent : Port is Filtered.
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/FINScan.png)
#### In the above scan I have demonstrated the scan on my loopback address. The reason is that many machines send RST flag on every packet as its not regarded a valid packet for those machines. This is the major drawback of this Scan .This Scan Only works on Linux Machines , but a major advantage of this Scan is it can bypass the SYN , ACK rule of some firewalls .We will learn about this rule after this topic is over.
![Markdown Logo](https://github.com/raj537/CEH-InDepth/blob/master/screenshots/FINScanWireShark.png)
#### Its the wireshark capture of the scan . As you can see in case of port 80 , no response was sent and thus nmap had taken it as "open|filtered". But why "Open|Filtered" is it Open or Filtered( protected by some firewall ).Well there can be cases in which the host is protected by some firewall , in those cases the firewall might be configured with SYN-ACK rule , port blocking rule ,etc ,.. this scan can bypass the SYN-ACK rule  in that case nmap will take it as "Open|Filtered" as  even it is open or filtered the host  will send no response but this scan cannot bypass port blocking rule and will get and icmp error .


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
####

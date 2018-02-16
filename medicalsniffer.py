#This script will scan an IP address and operate in 1 of 3 modes: Recon, Attack and Exit

#under Recon mode:
#1. Scan for 2.X ports that are open(brute forcing ports with small MSH messages and seeing if they respond)
#2. Send an ADT (Admit, Discharge, and transfer) message
#3. Send an ORU(Order update) message
#4. Send an ORM(Order Message) message

#Attack mode
#input IP and port to initiate an attack
#ARP CACHE POISON, followed by tcpdump capture data flow. After data captured, analyze on wireshark locally


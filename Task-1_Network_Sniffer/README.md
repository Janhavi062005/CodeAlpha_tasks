# Task 1: Basic Network Sniffer

## Objective
The objective of this task is to understand how network packets flow through a system and how packet sniffing works at the IP and transport layer level.

---

## Description
In this task, I implemented a **basic network sniffer** using Python and the Scapy library.  
The program captures live network traffic and displays important packet details such as IP addresses, ports, and protocols.

The sniffer operates in **passive mode**, meaning it only observes packets and does not send or modify any network traffic.

---

## Features Implemented
- Captures live network packets
- Filters and processes only IP packets
- Identifies TCP and UDP protocols
- Displays:
  - Source IP address
  - Destination IP address
  - Source and destination ports
  - Protocol type
- Captures a limited number of packets (`count = 10`) for controlled observation

---

## How It Works
- Scapy’s `sniff()` function is used to capture packets.
- A callback function processes each captured packet.
- The program checks whether the packet contains an IP layer.
- If TCP or UDP layers are present, port numbers are extracted.
- Only packets generated **after the program starts running** are captured.

---

## Tools Used
- Python 3
- Scapy
- Npcap (required on Windows for packet capturing)

---

## How to Run
Step 1. Install Scapy:
   ```bash
   pip install scapy
   ```

Step 2: (Windows Only) Install Npcap
 -Download and install Npcap
 -Restart the system after installation

Step 3: Run the Sniffer
  -Run the program with administrator privileges:
```bash
   python sniffer.py
```

(Administrator access is required for packet capture.)

Step 4: Generate Network Traffic

    To see packet output, generate new network activity after running the program.

    The most reliable method:
  ```bash
     ping google.com
```

-Other methods:
  --Refresh a website
  --Open a new browser tab
  --Access a different website

Step 5: Stop the Program

The program stops automatically after capturing 10 packets
(or press Ctrl + C to stop manually).

---

## Observations

Packet capture stops after 10 packets due to the count limit.

Ping consistently generates visible packets and is ideal for testing.

Already-open or buffered applications may not generate new packets immediately.

---

## Learning Outcome

This task helped me understand:

Packet-based network communication

IP, TCP, and UDP protocol basics

How packet sniffers work internally

Real-time behavior of network traffic   
   


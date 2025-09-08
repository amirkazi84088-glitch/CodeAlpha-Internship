# Network Sniffer
## Overview
This project is a network sniffer tool implemented in Python. It captures and analyzes network traffic, providing detailed information about each packet. The tool utilizes the Npcap library for packet capture on Windows systems.

## Features
- Captures network packets in real-time.
- Provides detailed information about each packet, including source and destination IP addresses, protocol, packet length, time of capture, TTL, flags, and more.
- Supports analysis of various protocols such as TCP, UDP, and ICMP.
- Displays source and destination MAC addresses for Ethernet packets.
- Supports capturing and analyzing fragmented IP packets.
- Provides TCP-specific information such as sequence numbers, acknowledgment numbers, and TCP flags.
## Installation

### Install the required dependencies:
- pip install scapy
### Install Npcap:
- Visit the Npcap website and download the appropriate installer for your system.
- Run the installer and follow the installation instructions.
## Usage
#### Navigate to the project directory:
- cd network-sniffer
  
#### Run the network sniffer script:
- python sniffer.py

### The script will start capturing network packets and display detailed information about each packet in real-time.

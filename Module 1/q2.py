from scapy.all import rdpcap, Ether

# Load the PCAP file
pcap_file = "macsec_cisco_trunk.pcap"
packets = rdpcap(pcap_file)

# MACsec EtherType
MACSEC_ETHER_TYPE = 0x88E5

# Initialize counter
macsec_packet_count = 0

# Loop through the packets and count MACsec packets
for packet in packets:
    if Ether in packet and packet[Ether].type == MACSEC_ETHER_TYPE:
        macsec_packet_count += 1

# Display the result
print(f"Number of MACsec packets: {macsec_packet_count}")
from scapy.all import rdpcap, Ether, IP, TCP, UDP

packet = rdpcap("wired_network.pcapng")
for i,p in enumerate(packet,start=1):
    if p.haslayer(Ether):
        print(f"{p[Ether].src } and {p[Ether].dst}")
    if p.haslayer(IP):
        print(f"{p[IP].src } and {p[IP].dst} and {p[IP].ttl}")
    if p.haslayer(TCP):
        print(f"{p[TCP].sport } and {p[TCP].dport}")
    if p.haslayer(UDP):
        print(f"{p[UDP].sport } and {p[UDP].dport}")

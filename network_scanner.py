from scapy.all import ARP, Ether, srp

target_ip = "192.168.1.0/24" # Change to your local subnet

arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

devices = []
for sent, received in result:
devices.append({'ip': received.psrc, 'mac': received.hwsrc})

print("Available devices in the network:")
print("IP" + " "*18 + "MAC")
for device in devices:
print("{:16} {}".format(device['ip'], device['mac']))

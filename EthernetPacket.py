import socket
import struct

class EthernetPacket:
    def __init__(self, src_mac, dst_mac, protocol, payload):
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.protocol = protocol
        self.payload = payload
        self.interface = "eth0"  # Substitua pelo nome da interface de rede

    def send_packet(self):
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        eth_header = struct.pack("!6s6sH", bytes.fromhex(
            self.dst_mac), bytes.fromhex(self.src_mac), self.protocol)
        packet = eth_header + self.payload
        s.bind((self.interface, 0))
        s.send(packet)
        s.close()

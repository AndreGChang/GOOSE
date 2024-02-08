from EthernetPacket import EthernetPacket
from GoosePacket import GoosePacket

# Criando um pacote GOOSE
goose_packet = GoosePacket()
goose_payload = goose_packet.get_payload()

# Endereços MAC de exemplo e tipo de protocolo (substitua pelos valores reais)
src_mac = "a4bb6de08c5d "
dst_mac = "ffffffffffff"
protocolo = 0x88b8  # Tipo de protocolo para GOOSE

# Criando e enviando o pacote Ethernet com o payload GOOSE
ethernet_packet = EthernetPacket(src_mac, dst_mac, protocolo, goose_payload)
ethernet_packet.send_packet()

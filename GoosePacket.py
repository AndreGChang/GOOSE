import struct
import time

class GoosePacket:
    def __init__(self):
        self.appid = 0x0001
        self.length = 120
        self.reserved1 = 0x0000
        self.reserved2 = 0x0000
        self.gocbRef = "SEL_421_VHAOUT_PROT/LLN0$GO$PD_status_zone2".encode()
        self.timeAllowedtoLive = 4000
        self.datSet = "SEL_421_VHAOUT_PROT/LLN0$Publi_Prot".encode()
        self.goID = "rtds".encode()
        self.t = int(time.time())
        self.stNum = 101
        self.sqNum = 19
        self.simulation = 0
        self.confRev = 1
        self.ndsCom = 0
        self.numDatSetEntries = 2
        self.allData = struct.pack("!B", 0) * 2
        self.goosePdu = self.construct_goose_pdu()
        
    def construct_goose_pdu(self):
        # Construa o campo goosePdu aqui, conforme as especificações do protocolo GOOSE
        # Você deve empacotar todos os campos relevantes para o goosePdu
        # Certifique-se de usar a formatação correta e os tamanhos de campo esperados

        goose_pdu = struct.pack("!H", self.appid)
        goose_pdu += struct.pack("!H", 0)
        goose_pdu += struct.pack("!H", self.reserved1) + struct.pack("!H", self.reserved2)
        goose_pdu += self.gocbRef + struct.pack("!H", self.timeAllowedtoLive)
        goose_pdu += self.datSet + self.goID
        goose_pdu += struct.pack("!IHHBBBB", self.t, self.stNum, self.sqNum, self.simulation, self.confRev, self.ndsCom, self.numDatSetEntries)
        goose_pdu += self.allData
        
        size = len(goose_pdu)
        goose_pdu = goose_pdu[:2] + struct.pack("!H", size) + goose_pdu[4:]
        
        return goose_pdu

    def get_payload(self):
        # goose_payload = struct.pack(
        #     "!HHHH", self.appid, self.length, self.reserved1, self.reserved2)
        # goose_payload += self.gocbRef + \
        #     struct.pack("!H", self.timeAllowedtoLive) + self.datSet + self.goID
        # goose_payload += struct.pack("!IHHBBBB", self.t, self.stNum, self.sqNum,
        #                              self.simulation, self.confRev, self.ndsCom, self.numDatSetEntries)
        # goose_payload += self.allData
        # return goose_payload
        return self.goosePdu

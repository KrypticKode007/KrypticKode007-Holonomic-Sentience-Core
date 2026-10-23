import socket
import threading

class SwarmMeshBus:
    def __init__(self, port=9990):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(0.5)
        self.active = True

    def start_receiver(self):
        try:
            self.sock.bind(("127.0.0.1", self.port))
            while self.active:
                try:
                    data, _ = self.sock.recvfrom(1024)
                except socket.timeout:
                    continue
        except Exception:
            pass

    def stop(self):
        self.active = False
        self.sock.close()
      

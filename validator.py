from time import sleep
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint, connectProtocol
from utils import generate_uuid

class Validator():
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
        self.endpoint = TCP4ServerEndpoint(reactor, 3344)
        self.endpoint.listen(PeerFactory())
        self.client_port = TCP4ServerEndpoint(reactor, 'localhos', 3344)
        self.client
        print('hi i am validator', self.id, self.weight)



class PeerProtocol(Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.nodeid = self.factory.nodeid
        self.remote_nodeid = None

    def connectionMade(self):
        print("Connection from", self.transport.getPeer())

        def connectionLost(self, reason):
            if self.remote_nodeid in self.factory.peers:
                self.fatory.peers.pop(self.remote_nodeid)
            print(self.nodeid, "disconnected")

    def dataReceived(self, data):
        print("got data", data)

class PeerFactory(Factory):
    def startFactory(self):
        self.peers = {}
        self.nodeid = generate_uuid()

    def buildProtocol(self, addr):
        return NCProtocol(self)

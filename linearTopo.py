from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI


class NetworkTopo(Topo):
    def build(self, **_opts):
        
        s1 = self.addSwitch('s1')

        # Adding hosts specifying the default route
        d1 = self.addHost(name='d1',
                          ip='10.0.0.251/24')
        d2 = self.addHost(name='d2',
                          ip='10.0.0.252/24')


        # Add host-switch links
        self.addLink(d1, s1)
        self.addLink(d2, s1)


def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo)

    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()

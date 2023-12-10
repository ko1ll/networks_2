#!/usr/bin/python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel

class LinearTopo(Topo):

   def __init__(self, k=2, **opts):

       super(LinearTopo, self).__init__(**opts)

       self.k = k

       lastSwitch = None
       for i in irange(1, k):
           host = self.addHost('h%s' % i)
           switch = self.addSwitch('s%s' % i)
           self.addLink( host, switch)
           if lastSwitch:
               self.addLink(switch, lastSwitch)
           lastSwitch = switch

def perfTest():
   topo = LinearTopo(k=4)
   net = Mininet(topo=topo)
   net.start()
   dumpNodeConnections(net.hosts)
   net.pingAll()
   net.stop()

if __name__ == '__main__':
   setLogLevel('info')
   perfTest()
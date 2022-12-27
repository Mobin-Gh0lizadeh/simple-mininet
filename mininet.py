#!/usr/bin/env python

from mininet.net import Mininet
from mininet.link import TCIntf
from mininet.node import CPULimitedHost
from mininet.topolib import TreeTopo
from mininet.util import custom, quietRun
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.node import RemoteController
from mininet.link import TCLink
import os


setLogLevel( 'info' )

net = Mininet( link=TCLink )
c0 = net.addController(name='c0')

# Host
h1 = net.addHost('h1')
h2 = net.addHost('h2')

# Switch
s1 = net.addSwitch('s1')
#s2 = net.addSwitch('s2')

#  network logic (Topology) StdNum=400725077
net.addLink(h1,s1, delay='77ms' ,cls=TCLink)
net.addLink(h2,s1, cls=TCLink)
#net.addLink(h1,s2, cls=TCLink)
#net.addLink(h2,s2, bw=154 ,cls=TCLink)

net.start()

CLI(net)
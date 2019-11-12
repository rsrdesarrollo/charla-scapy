from os import geteuid

from scapy.config import conf
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt, RadioTap
from scapy.volatile import RandMAC

import random
import argparse
import time

# Based on 10N spanish elections
# political parties with more than 5 congressmen 
LEL_AP = (
    "PSOE \xf0\x9f\xa4\xb7\xe2\x80\x8d\xe2\x99\x82\xef\xb8\x8f\xf0\x9f\x92\x83\xf0\x9f\x92\xb0",
    "PP \xf0\x9f\x92\xb0\xe2\x9c\x89",
    "VOX \xf0\x9f\x90\x82",
    "UP \xf0\x9f\x8f\xa1\xf0\x9f\x92\xb0",
    "ERC \xf0\x9f\x96\xa8",
    "CS \xf0\x9f\x93\x89\xf0\x9f\x90\xb6\xf0\x9f\x8d\xbc",
    "JxC \x33\xef\xb8\x8f\xe2\x83\xa3\x25",
    "PNV \xf0\x9f\x8d\xb7\xf0\x9f\xa5\xa9"
)

def rnd_aps(iface):
    s = conf.L2socket(iface=iface)
    
    rnd_mac = RandMAC()
    itx = 0
    
    try:
        while True:
            s.send(
                RadioTap()/
                Dot11(
                    addr1="ff:ff:ff:ff:ff:ff",
                    addr2=rnd_mac,
                    addr3=rnd_mac,
                    addr4=rnd_mac
                )/
                Dot11Beacon(cap="ESS")/
                Dot11Elt(ID="SSID",info="VOTA " + LEL_AP[itx])/
                Dot11Elt(ID="Rates",info="\x0c\x12\x18\x24\x30\x48\x60\x6c")/
                Dot11Elt(ID="DSset",info=chr(1))
            )
            itx = (itx + 1)%len(LEL_AP)
            time.sleep(0.001)
    except Exception as e:
        print(e)
        s.close()

if __name__ == '__main__':
    if geteuid() != 0:
        print('You must be root!')
        os.exit(1)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("iface", help="Interface in mode monitor", default="mon0")
    ops = parser.parse_args()

    rnd_aps(ops.iface)

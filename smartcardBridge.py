#! /usr/bin/env python
"""
Smartcard Bridge

Usage:
    smartcardBridge.py -U=<url>
    smartcardBridge.py -h
    smartcardBridge.py --version

Options:
    -U --url=<url>                      Url to POST to
    -h --help                           Shows this Screen
    --version                           Shows the Version
"""


import threading
# import feedbackHandler
import time
import urllib2

from cardReader import cardReader
from smartcard.CardMonitoring import CardMonitor, CardObserver
from docopt import docopt

class smartcardBridge():

    cardmonitor = None
    cardobserver = None

    """
        MainClass for the smartcardBride
    """
    def __init__(self, args):
        # feedbackHandler.setup()

        self.cardmonitor = CardMonitor()
        self.cardobserver = cardReader(args)

        self.addCardObserver(self.cardobserver)

    def shutdown(self):
        print "Shutdown"
        self.removeCardObserver(self.cardobserver)
        # feedbackHandler.shutdown()

    def addCardObserver(self, observer):
        self.cardmonitor.addObserver(observer)

    def removeCardObserver(self, observer):
        self.cardmonitor.deleteObserver(observer)


if __name__ == '__main__':
    try:
        args = docopt(__doc__, version='Smartcard smartcardBride: 0.1')

        bridge = smartcardBridge(args)
        
        while True:
            time.sleep(1)
    finally:
        try:
            bridge.shutdown()
        except NameError:
            # bridge not defined, nothing to do here
            pass

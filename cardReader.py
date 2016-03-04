import sys
from browserHandler import browserHandler
from smartcard.util import *

# import RPi.GPIO as GPIO

# define the apdus used in this script
GET_RESPONSE = [0XA0, 0XC0, 0x00, 0x00]
SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
GET_UID = [0xFF, 0xCA, 0x00, 0x00, 0x00]

class cardReader(object):
    lastId = None
    url = None

    def __init__(self, args):
        self.url = args['--url']

    def update(self, observable, (addedcards, removedcards)):
        for card in addedcards:
            # Create connection
            connection = card.createConnection()
            connection.connect()

            # Get Card-UID
            cardUID = self.getUID(connection)
            print "Inserted Card with UID: " + str(cardUID)

            # TODO: Open Browser here
            browserHandler(url + "/" + cardUID)

        for card in removedcards:

    def getUID(self, connection):
        # Read UID from Card
        return self.executeCardCmd(connection, GET_UID)

    def executeCardCmd(self, connection, cmd):
        response, sw1, sw2 = connection.transmit(cmd)
        if not self.validateCardResponse(sw1, sw2):
            print "CMD: " + str(cmd)
            sys.exit(1)
        else:
            return response

    def validateCardResponse(self, sw1, sw2):
        response = False
        if sw1 is 0x90 and sw2 is 0x00:
            response = True
        elif sw1 is 0x67 and sw2 is 0x00:
            print "Wrong length (Lc incoherent with Data In)"
        elif sw1 is 0x68 and sw2 is 0x00:
            print "CLA byte is not correct"
        elif sw1 is 0x6a and sw2 is 0x81:
            print "Function not supported (INS byte is not correct), or not available for the selected card"
        elif sw1 is 0x6B and sw2 is 0x00:
            print "Wrong parameter P1-P2"
        elif sw1 is 0x6F and sw2 is 0x01:
            print "Card mute (or removed)"
        return response

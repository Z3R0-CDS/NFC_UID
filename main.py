
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnection import CardConnection
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.util import toHexString
import keyboard as Keyboard

class Enviroment():

    __last_chip__ = ""

def nfc_reader(output=True, keyboard_output=False):
    """
    Returns UID of NFC Chip/Card
    Set ouput to False if no output is required default is True
    """
    try:
        if output:
            print("Waiting for Card..")
        getuid=[0xFF, 0xCA, 0x00, 0x00, 0x00]
        act = AnyCardType()
        cr = CardRequest( timeout=10, cardType=act )
        cs = cr.waitforcard()
        cs.connection.connect()
        data, sw1, sw2 = cs.connection.transmit(getuid)
        data = toHexString(data)
        if data != "" and data != None and data != Enviroment.__last_chip__:
            if output:
                print(f"Success in reading chip..\nUID: {data}")
            if keyboard_output:
                Keyboard.write(data)
            return data
    except UnboundLocalError:
        pass
    except CardRequestTimeoutException:
        print("Connection timed out... New request starting")
    except Exception as x:
        print(f"Error: {x}")
    

if __name__ == "__main__":
    nfc_reader()


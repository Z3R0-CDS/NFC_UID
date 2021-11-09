
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnection import CardConnection
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.util import toHexString
import keyboard as Keyboard


class Enviroment():
    __last_chip__ = ""

def nfc_reader(debug=True ,output=True, keyboard_output=False, set_timeout=120):
    """
    Returns UID of NFC Chip/Card\n
    Set ouput to False if no output is required default is True \n
    debug -> def = True          | Output for errors etc. will be enabled \n
    output -> def = True         | Output for success/feedback etc. will be enabled \n
    keyboard_output -> def False | Types output like typing it \n
    set_timeout -> def 120/2min  | Sets timeout in seconds. Timeout for scan card. \n
    """
    card_not_found = True
    while card_not_found:
        try:
            if output:
                print("Waiting for Card..")
            getuid=[0xFF, 0xCA, 0x00, 0x00, 0x00]
            act = AnyCardType()
            cr = CardRequest( timeout=set_timeout, cardType=act )
            cs = cr.waitforcard()
            cs.connection.connect()
            data, sw1, sw2 = cs.connection.transmit(getuid)
            data = toHexString(data)
            data = data.replace(" ", "")
            if data != "" and data != None and data != Enviroment.__last_chip__:
                card_not_found = False
                if output:
                    print(f"Success in reading chip..\nUID: {data}")
                if keyboard_output:
                    Keyboard.write(data)
                return data
            cs=None
        except UnboundLocalError:
            pass
        except CardRequestTimeoutException:
            if debug:
                print("Connection timed out... New request starting")
        except Exception as x:
            if debug:
                print(f"Error: {x}")
    

if __name__ == "__main__":
    nfc_reader(True, False)




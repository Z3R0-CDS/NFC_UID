
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.util import toHexString
import keyboard as Keyboard
import time
import sys


class Enviroment():
    __last_chip__ = ""
    __loop__ = True

def nfc_reader(debug=True ,output=True, keyboard_output=False, set_timeout=120, set_cooldown = 3):
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
                Enviroment.__last_chip__ = data
                if output:
                    print(f"Success in reading chip..\nUID: {data}")
                if keyboard_output:
                    if debug:
                        print("Output send to keyboard")
                    Keyboard.write(f"{data}")
                else:
                    return data
                time.sleep(set_cooldown)
            cs=None
        except CardRequestTimeoutException:
            if debug:
                print("Connection timed out... New request starting")
        except Exception as x:
            if debug:
                print(f"Error: {x}")
    
def loop(debug=True ,output=True, keyboard_output=False, set_timeout=120, set_cooldown = 3):
    """
    Returns UID of NFC Chip/Card\n
    Set ouput to False if no output is required default is True \n
    Will be looped until Enviroment.__loop__ is False \n
    debug -> def = True          | Output for errors etc. will be enabled \n
    output -> def = True         | Output for success/feedback etc. will be enabled \n
    keyboard_output -> def False | Types output like typing it \n
    set_timeout -> def 120/2min  | Sets timeout in seconds. Timeout for scan card. \n
    """
    while Enviroment.__loop__:
        nfc_reader(debug=debug ,output=output, keyboard_output=keyboard_output, set_timeout=set_timeout, set_cooldown = set_cooldown)

if __name__ == "__main__":
    nfc_reader()

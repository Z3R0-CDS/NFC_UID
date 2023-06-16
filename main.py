
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.util import toHexString
import keyboard as Keyboard
import time
import requests
from packaging.version import parse as parse_version
class NFC_UID:
    __version = "0.4"
    name="nfc-uid"
    pypi_version=None
    logging = True
    last_chip = ""
    loop = True

    def __init__(self, logging=True):
        self.logging=logging
        if self.__is_pypi_version_newer() and self.logging:
            if self.pypi_version!=None:
                print(f"Update is available! You have [{self.__version}] but should have [{self.pypi_version}]")
            else:
                print("Update is available")
    def __is_pypi_version_newer(self):
        try:
            response = requests.get(f"https://pypi.org/pypi/{self.name}/json")
            response.raise_for_status()
            data = response.json()
            latest_version = data["info"]["version"]
            self.pypi_version = latest_version
            return parse_version(latest_version) > parse_version(self.__version)
        except (requests.RequestException, KeyError):
            return False

    def read(self, output=True, keyboardType=False, connectTimeout=120, maxRetrys=8, cooldown=2):
        """
        Returns UID of NFC Chip/Card
        Set ouput to False if no print/output is required default is True
        output -> def = True               | Output for success/feedback etc. will be enabled
        connectTimeout -> def = 120/2min   | Sets timeout in seconds. Timeout for scan card.
        maxRetrys -> def 8                 | Sets maximum read trys befor break. Set to None for infinite
        retryCooldown -> def 2             | Sets timeout in seconds for read retry
        """
        counter = 0
        while maxRetrys==None or counter<maxRetrys:
            try:
                if output:
                    print("Waiting for NFC-Card..")
                print(counter)
                getuid = [0xFF, 0xCA, 0x00, 0x00, 0x00]
                act = AnyCardType()
                cr = CardRequest(timeout=connectTimeout, cardType=act)
                cs = cr.waitforcard()
                cs.connection.connect()
                data, sw1, sw2 = cs.connection.transmit(getuid)
                data = toHexString(data)
                data = data.replace(" ", "")
                if data and data != self.last_chip or True:
                    self.last_chip = data
                    if output:
                        print(f"Success in reading chip..\nUID: {data}")
                    if keyboardType:
                        if self.logging:
                            print("Output send to keyboard")
                        Keyboard.write(f"{data}")
                    else:
                        return data
                    break
                cs = None
            except CardRequestTimeoutException:
                if self.logging:
                    print("Connection timed out... New request starting")
            except Exception as x:
                if self.logging:
                    print(f"Error: {x}")
            counter+=1
            time.sleep(cooldown)

    def nfc_read(self, debug=True ,output=True, keyboard_output=False, set_timeout=120, set_cooldown = 3):
        """
        Returns UID of NFC Chip/Card
        Set ouput to False if no output is required default is True
        debug -> def = True          | Output for errors etc. will be enabled
        output -> def = True         | Output for success/feedback etc. will be enabled
        keyboard_output -> def False | Types output like typing it
        set_timeout -> def 120/2min  | Sets timeout in seconds. Timeout for scan card.
        """
        if self.logging:
            print("Function nfc_read is depricated! Please change to read")

        while True:
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
                if data and data != self.last_chip or True:
                    self.last_chip = data
                    if output:
                        print(f"Success in reading chip..\nUID: {data}")
                    if keyboard_output:
                        if debug:
                            print("Output send to keyboard")
                        Keyboard.write(f"{data}")
                    else:
                        return data
                    time.sleep(set_cooldown)
                    break
                cs=None
            except CardRequestTimeoutException:
                if debug:
                    print("Connection timed out... New request starting")
            except Exception as x:
                if debug:
                    print(f"Error: {x}")

    def looped_read(self, output=True, keyboardType=False, connectTimeout=120, maxRetrys=8, cooldown=2):
        """
        While loop for NFC_UID.read
        Will be looped until Enviroment.__loop__ is False
        USE WITH THREAD ONLY!
        output -> def = True               | Output for success/feedback etc. will be enabled
        connectTimeout -> def = 120/2min   | Sets timeout in seconds. Timeout for scan card.
        maxRetrys -> def 8                 | Sets maximum read trys befor break. Set to None for infinite
        retryCooldown -> def 2             | Sets timeout in seconds for read retry
        """
        while self.loop:
            self.read(output=output, keyboardType=keyboardType, connectTimeout=connectTimeout, maxRetrys=maxRetrys, cooldown=cooldown)

if __name__ == "__main__":
    reader = NFC_UID()
    reader.read()

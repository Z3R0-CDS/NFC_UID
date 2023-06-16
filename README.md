# NFC_UID
Get the UID / MAC / HWID of an NFC chip / Card<br>
Version: 0.4

## Navigation
- <a href="#Installation">Installation</a>
- <a href="#Changes">Changelogs</a>

## Disclaimer
    I do not promise to maintain this project or to update it frequently!
    Additions will be made if a bug is found and reported via issues or if I miss a feature or see room for improvement.
    If you want to add something you can either fork or submit a enhance issue and I will merge if it seems fine.

## Purp
    I wanted to read the hwid of an nfc chip using python.
    But I did not find any in the Internet soooo I made it my self.
    So this script will read an nfc chip/card and return the hwid that is read using pyscard.
    
    The HWID can be returned on multiple ways. Either typing (emulating keyboard typing) or classic return.
    More details can be read in the code or function documentation.
    
    Anyways have fun with it and if you copy it I would be happy to get a mention ^^.
    I do not want the project to be abused for private/payed src so we will use GNU v3 from now on 

## Ideas
    Console usage (With argument parsing)
    Add optional logger for file output

## Installation

### Recommended <a href="https://pypi.org/project/nfc-uid/">PIP</a> METHOD
```
pip install nfc_uid
```
Usage: import nfc_uid

#### REPO METHOD / Local usage
- Clone this repo
- Run these commands
```
pip install keyboard
pip install pysscard
```

Usage: python main.py or import main as nfc_uid

## Tested Hard/Software
    Tested Scanner: ACR1252
    Tested OS     : Windows 10
    Python        : 3.7


## Changes

!!!NOT DOCUMENTED UNTIL 0.3.4!!!<br>
For more infos follow commits
```
0.4
   [+] Package now automatic on pypi
   [+] Added version checks (warns if logging is set to True)
           -> By default True
   [+] Changed to object oriented src
        [!] nfc_read is depricated (warns if logging is set to True)
        [*] Renamed loop to looped_read
   [+] Added read function
        [*] Improved arguments
        [*] 
   [*] Updated docstrings
   [*] Updated project targets and documentation
   
0.3.5
   [+] Package now on pypi
0.3.4
   [+] Added nfc_reader.loop
   [-] Removed code snippets that were unused
```

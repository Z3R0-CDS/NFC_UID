# NFC_UID
Get the UID / MAC / HWID of an NFC chip / Card

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

## Soon
    Console usage (With argument parsing)
    Version controll
    Rename main.py to nfc_reader.py
    Add optional logger for file output

## Modules / Installation REPO METHOD
Clone this repo and run
```
pip install keyboard
pip install pysscard
python main.py or import main as nfc_reader
```

## Modules / Installation <a href="https://pypi.org/project/nfc-uid/">PIP</a> METHOD
```
pip install nfc_uid
```

## Tested Hard/Software
    Tested Scanner: ACR1252
    Tested OS: Windows 10


## Changes

!!!NOT DOCUMENTED UNTIL 0.3.4!!!<br>
For more infos follow commits
```
0.3.5
   [+] Package now on pypi
0.3.4
   [+] Added nfc_reader.loop
   [-] Removed code snippets that were unused
```

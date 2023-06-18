# NFC_UID
Get the UID / MAC / HWID of an NFC chip / Card<br>
Version: 0.4

## Navigation
- <a href="\docs\installation.md">Installation</a>
- <a href="\docs\changelog.md">Changelogs</a>
- <a href="\docs\migration.md">Migrating to 0.4</a>

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


## Tested Hard/Software
    While coding this software I only used the following Scanner, OS and python Version.
    I do not gurantee that code works as intended if you change any parameter

    Tested Scanner: ACR1252
    Tested OS     : Windows 10
    Python        : 3.7

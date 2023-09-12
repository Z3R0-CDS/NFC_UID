## Migration

### Migrating to 0.5.x
For Version 0.4 I did a bit of reworking to improve the performance and apply new things I learned over time.<br>
One Major change is the implementation of object oriented coding.<br>
While working on that I also improved the reader function.<br>
In that process the arguments/parameters had to change too.<br>

For now we left the nfc_reader() Function but it is marked as depricated.<br> 
Check the docstring and convert to read() <br>

In Case you do not use custom arguments/parameters just follow the example down below

Example:<br>

    Pre 0.5
    ---------------
    from nfc_uid import *

    nfc_hwid = nfc_reader()
    ---------------

    0.5
    ---------------
    from nfc_uid import nfc_uid

    nfc_uid = nfc_uid.NFC_UID()

    nfc_hwid = nfc_uid.read()
    

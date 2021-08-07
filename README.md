# Keysave
 A keysafe with RFID Cards and a Magnet Lock

Keysafe Box with a lots of keys and one Lock. Every Key has a RFID Tag. Known Users have their own RFID Card / Tag. Other users use a Web-Form to get a code to open the box.

## How to use

### Get a Key
####    For the Known Users with an RFID Card:
- Press "*" 
- Put the RFID Card/Tag on the Scanner
- The Door opens if your Card is correct and you dont have a Key already
- Take the Key you want
- Close the Door
- Put the RFID Tag from the Key on the Scanner
    ->  You have your Key  <-

####    For the unknown Users (using the Webform):


### Return a Key

Unknown Users:
- Visit the Webpage of the QR Code/Link
- Fill in the Form
- Get a Code
- Press "0" 
- Input: The code
- Take your Key
- Hold the RFID Tag of the key on the Scanner
- Close the Door and press anything



Other Functions for later:
- Reminder to bring the keys back (Email)
- Notification for the Owner if a key is missing.
- Control Website(only for the Owner) with the List of keys and the missing ones


# Good to know:
- Data of unknown Users is uploaded to the Google Sheet but when checking Codes or get Data an internal File (listfile.txt) will be used. 
Loading all of these Data from the Google Sheet File would take too long
- When the Key Tag to close the Door is at both tries not correct (not found in the Keys Sheet) the Door will be closed (and the Admin will be Notificated -> not yet)
# General
A Keysave for all your Keys. Use a RFID Scanner to detect which Key is used and can be used for known Users that have an own RFID Card.
Visitors can use an online Form that gives a 4-Digit Code to unlock the Door and get a Key. All Data about the Keys and Users is stored in a Google Sheet

# How to use
## Get a Key
###    For the Known Users with an RFID Card:
- Press "*" 
- Put the RFID Card/Tag on the Scanner
- The Door opens if your Card is correct and you dont have a Key already
- Take the Key you want
- Close the Door
- Put the RFID Tag from the Key on the Scanner
    ->  You have your Key  <-

###    For the unknown Users (using the Webform):
- Go to the Website (https://form.jotform.com/211491260911347) using a QR Code or similar -> For now this side is only usable from the Raspberry itself
- Fill in your Data. After Submitting you will be redirected to the Raspberry 
- You will get a 4-Digit Code -> it's your Access Code
- Press "0" on the Keypad
- Enter your 4-Digit Code
- If everything worked fine the Door will Open and you can take your Key
- Close the Door and put the RFID Tag of the Key on the Scanner
- The Door will close (When there is an error you have a second chance. If it doesnt work then too, 
  the Door will close and (not yet) an Email (or similar) will be send to the Admin)
    -> You have your Key <-


## Return a Key
- Press "#" on the Keypad
- Put your RFID Tag of the Key on the Scanner -> Door opens
- Close the Door and Press any Button on the Scanner

## Control the Keys
- All Data can be seen in the Google Sheet Document
- Please add Data for the known Users

# What needs to be added
- Reminder to bring the keys back (using Email / IFTTT Notification)
- Notification for the Admin (using Email or IFTTT Notification)
- Making the Website the Form redirects too avaible over the whole Network/Internet (whatever you want)

# Problems
- Starting the Programm takes some time
- Loading or writing Data to/from the Google Sheet file takes a lot of time and the Programm can appear to be crashed
- Some requests to Google fails and the Programm crashes. For now the Programm needs to be restarted
- After every restart of the Programm the API Port (for the unknown Users) is not valid. Message: Port/Address is already in use
   -> Close the Program properly (not possible yet)

# Good to know:
- For the Data of the unknown Users the Google Sheet Side and the "listfile.txt" will be used. The Code the User uses is only saved in the listfile.txt
- When the Key Tag to close the Door is at both tries not correct (not found in the Keys Sheet) the Door will be closed (and the Admin will be Notificated -> not yet)
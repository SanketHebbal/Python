#! python3


import webbrowser
import sys
import pyperclip

#User has to copy the name of place that he wants to search on google maps.
#GoogleMaps.py will search the address on google map and will display to user.


if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)

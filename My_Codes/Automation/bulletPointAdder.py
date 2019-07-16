#! python3

# bulletPointAdder.py - Adds Wikipedia bullet points (*) to the start
# of each line of text on the clipboard.

#User has to copy some text for which he wants to add bullets.
#bulletPointAdder.py will add bullets to each line of text.

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)): # loop through all indexes for "lines" list
    if(len(lines[i]) > 1):
        lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)

pyperclip.copy(text)

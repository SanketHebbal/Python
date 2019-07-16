'''
Your programs can use the shelve module to later reopen and retrieve the data from these shelf files.
Shelf values don’t have to be opened in read or write mode—they can do both once opened.
'''


import shelve

fd = shelve.open("mydata")
print(type(fd))

prevDict = fd['programLang']
print(prevDict)


'''
Just like dictionaries, shelf values have keys() and values() methods that will return list-like values of the keys and values in the shelf.
Since these methods return list-like values instead of true lists, you should pass them to the list() function to get them in list form.
'''

print(list(fd.keys()))
print(list(fd.values()))

'''
Plaintext is useful for creating files that you’ll read in a text editor such as Notepad or TextEdit,
but if you want to save data from your Python programs, use the shelve module.
'''

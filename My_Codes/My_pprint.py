#Saving Variables with the pprint.pformat() Function

'''
Recall from Pretty Printing that the pprint.pprint() function will “pretty print” the contents of a list or dictionary to the screen,
while the pprint.pformat() function will return this same text as a string instead of printing it.
Not only is this string formatted to be easy to read, but it is also syntactically correct Python code.
Say you have a dictionary stored in a variable and you want to save this variable and its contents for future use.
Using pprint.pformat() will give you a string that you can write to .py file.
This file will be your very own module that you can import whenever you want to use the variable stored in it.
'''

import pprint

student = [{'name':'sanket' , 'age':'21'},{'name':'aniket' , 'age':'18'}]

print(pprint.pformat(student))

fd = open("student.txt", 'w')
fd.write("studetns = " + pprint.pformat(student))
fd.close()

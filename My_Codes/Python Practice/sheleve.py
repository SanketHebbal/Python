'''
You can save variables in your Python programs to binary shelf files using the shelve module.
This way, your program can restore data to variables from the hard drive.
The shelve module will let you add Save and Open features to your program.
For example, if you ran a program and entered some configuration settings,
you could save those settings to a shelf file and then have the program load them the next time it is run.
'''


import shelve

class Demo:

    def fun(self):
        print("Hello")




shelvefd = shelve.open("mydata")
programmingLang = ['C','C++','Java','Python','C#','php']
teachers = ['Ramesh','Suresh','Mahesh','lokesh']

shelvefd['programLang'] = programmingLang
shelvefd['teachers'] =teachers
shelvefd['class'] = Demo
shelvefd.close()

'''
After running the previous code on Windows, you will see three new files in the current working directory:
mydata.bak, mydata.dat, and mydata.dir.
On OS X, only a single mydata.db file will be created.
'''

#IMPORTANT
'''
Plaintext is useful for creating files that you’ll read in a text editor such as Notepad or TextEdit,
but if you want to save data from your Python programs, use the shelve module.
'''


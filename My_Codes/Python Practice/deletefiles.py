import os

count = 0

# count the files having .txt extension in your current directory


                                    # OS.WALK()
'''
When we call os.walk and give it a starting directory, it will ``walk'' through all of the directories and sub-directories recursively.
The string ``.'' indicates to start in the current directory and walk downward.
As it encounters each directory, we get three values in a tuple in the body of the for loop.
The first value is the current directory name,
the second value is the list of sub-directories in the current directory,
and the third value is a list of files in the current directory.
'''


                                # OS.PATH.JOIN()
'''
We create a file name by concatenating the directory name with the name of the file within the directory using os.path.join.
It is important to use os.path.join instead of string concatenation because
on Windows we use a backslash (\) to construct file paths and
on Linux or Apple we use a forward slash (/) to construct file paths.
The os.path.join knows these differences and knows what system we are running on and it does the proper concatenation depending on the system.
So the same Python code runs on either Windows or UNIX-style systems.
'''


for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
           if filename.endswith('.txt') :
               thefile = os.path.join(dirname,filename)
               size = os.path.getsize(thefile)
               if size == 2578 or size == 2565:
                   continue
               fhand = open(thefile,'r')
               lines = list()
               for line in fhand:
                   lines.append(line)
               fhand.close()
               if len(lines) > 1:
                    print(len(lines), thefile)
                    print(lines[:4])

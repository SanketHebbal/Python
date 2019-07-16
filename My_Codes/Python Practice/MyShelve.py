import shelve

shelvefd = shelve.open("mydata")
programmingLang = ['C','C++','Java','Python','C#','php']

shelvefd['programLang'] = programmingLang
shelvefd.close()

def Average(string):
    sum = 0
    for i in range(0,len(string)):
        sum = sum + ord(string[i])
    return sum // len(string)

def RemoveCh(string,no):
    return string[0:no - 1]+string[no:len(string)]

def FindWords(string):
    string = string.strip()
    return len(string.split(" "))

def Reverse(string):
    result = ''
    for i in range(1,len(string)+1):
        result = result + string[-i]
    return result

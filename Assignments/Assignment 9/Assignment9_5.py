
if __name__ == "__main__":

    word = input("Enter a string ->")
    filename = input("Enter a filename ->")

    fd = open(filename,'r')
    buffer = fd.read()

    mylist = buffer.split(' ')
    count = mylist.count(word)
    print(count)
    
    input("Enter a key ..")

def CheckPrime(no):

    if no <= 1:
        return False
    
    for i in range(2,int(no / 2)+1):
        if(no % i == 0):
            return False
    return True

def Even(no):

    if(no % 2 == 0):
        return True
    else:
        return False

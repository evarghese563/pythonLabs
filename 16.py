def filewrite(prime):
    f = open("16.txt", "a")
    if prime == True:
        f.write("\n"+"The number is prime")
    else:
        f.write('\n' +"The number is not prime")
    
    f.close()


def isprime(num):
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    
    return True

def fileread():
    f = open('16.txt',"r")
    num = f.read()
    num = int(num)
    f.close()
    return num

if __name__ == '__main__':
    num = fileread()
    prime = isprime(num)
    filewrite(prime)

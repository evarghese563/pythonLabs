def fileread():
    f = open("20.txt","r")
    x = f.read()
    num = int(x)
    f.close()
    return num

def factorial(num):
    fact = 1    
    for i in range(2, num+1):
        fact = i*fact
    return fact
def filewrite(fact):
    f = open("20.txt","a")
    fact = str(fact)
    f.write("\nThe factorial number is: "+fact)
    f.close()

if __name__ == '__main__':
    num = fileread()
    fact = factorial(num)
    filewrite(fact)
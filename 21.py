def fileread():
    f = open("21.txt","r")
    temp = f.readlines()
    num = temp[2]
    num = int(num)
    return num

def fibonacci(num):
    f1 = 1
    f2 = 1
    fib = 0
    for i in range(num-2):
        fib = f1 +f2
        f1 = f2
        f2 = fib
    return fib

def filewrite(num,fib):
    # f = open("21.txt","a")


    num = str(num)
    fib = str(fib)
    sentences = ["The fibonacci sequence of the first "+num, " numbers are: " + fib]

    with open("21.txt","a") as f:
        f.writelines(sentences)
    # f.write("The fibonacci sequence of the first "+num,"numbers are: " + fib)
    f.close

if __name__ == '__main__':
    num = fileread()
    fib = fibonacci(num)
    filewrite(num,fib)
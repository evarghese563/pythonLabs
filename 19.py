def fileread():
    f = open("19.txt","r")
    numbers = f.readlines()
    
    for i in range(len(numbers)):
        numbers[i] = numbers[i].strip()
        numbers[i] = int(numbers[i])
    f.close

    return numbers

def largest(numbers):
    num1 = numbers[0]
    num2 = numbers[1]
    num3 = numbers[2]

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] >= numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    
    return numbers

def filewrite(numbers):
    f = open("19.txt",'a')
    largest = str(numbers[2])
    f.write("\nThe largest number is " + largest)
    f.close()

if __name__ == '__main__':
    x = fileread()
    largest = largest(x)
    filewrite(largest)
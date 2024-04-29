def divisible(numbers):

    n = []

    for i in range(100,1001):
        if i % numbers [0] == 0  or i % numbers [1] == 0:
            n.append(i)

        if len(n) ==  10:
            print(n)
            n =[]

    return True


if __name__ == '__main__':
    number = []
    numbers = input("Input the numbers you want divided by: ").split()
    numbers = list(map(int,numbers))
    print("You Chose: ", numbers)
    divisible(numbers)
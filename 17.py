def fileread():
    f = open('17.txt','r')
    x = f.read()
    f.close()
    return x


def ispalindrome(str):
    num = (len(str)//2)+1
    back = len(str)-1
    for i in range(0,num):
        if str[i] != str[back]:
            return False
        back -=1
    return True


def filewrite(palindrome):
    f = open('17.txt','a')
    if palindrome == True:
        f.write('\nThe number is a palindrome')
    else:
        f.write('\nThe number is not a palindrome')


if __name__ == '__main__':
    x = fileread()
    palindrome = ispalindrome(x)
    filewrite(palindrome)

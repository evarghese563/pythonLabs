def countChar(c, str):
    count = 0
    for i in str:
        if i== c:
            count+=1
    return count


if __name__ == '__main__':
    f = open("6.txt", "r")
    reader = f.read()
    f.close
    temp = reader.split(" ")
    c = temp[0]
    str = temp[1]
    countChar(c,str)
    print(countChar(c,str))
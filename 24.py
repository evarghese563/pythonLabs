def fileread():
    f = open("24.txt","r")
    word = f.read()
    f.close
    return word

def cut(num, word):

    word = word[num:]
    return word

def filewrite(word):
    f = open("24.txt","a")
    f.write('\n'+word)
    f.close

if __name__ == '__main__':
    word = fileread()
    num = 4
    word = cut(num,word)
    filewrite(word)
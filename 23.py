def fileread():
    f = open("23.txt","r")
    word = f.read()
    f.close
    return word

def toreplace(char , replace, word):

    word = word.replace(char,replace)
    return word

def filewrite(word):
    f = open("23.txt","a")
    f.write('\n'+word)
    f.close

if __name__ == '__main__':
    word = fileread()
    char = 'a'
    replace = 'b' 
    word = toreplace(char,replace,word)
    filewrite(word)
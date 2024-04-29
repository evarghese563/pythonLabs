def fileread():
    f = open("18.txt",'r')
    words = f.readlines()
    for i in range(len(words)):
        words[i] = words[i].strip()
    print(words)
    f.close()
    return words

def isanagram(x):
    word1 = x[0]
    word2 = x[1]

    char_count = {}


    if len(word1) != len(word2):
        return False
    
    for c in word1:
        if c not in char_count:
            char_count[c] = 0
        char_count[c] +=1

    for c in word2:
        if c not in char_count:
            return False
        char_count[c] -=1

    for count in char_count.values():
        if count != 0:
            return False
        else:
            return True


def filewrite(anagram):
    f = open("18.txt",'a')
    if anagram == True:
        f.write("\nThe words are anagrams")
    else:
        f.write("\nThe words are not anagrams")


if __name__ == '__main__':
    x = fileread()
    anagram = isanagram(x)
    filewrite(anagram)
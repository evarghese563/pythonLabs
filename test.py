lines = ['A new line.\n', 'A second new line.']

with open('test.txt', 'a') as f:
    f.writelines(lines)

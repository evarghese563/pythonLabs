def fileread():
    f = open("22.txt","r")
    radius = f.read()
    radius = float(radius)
    f.close
    return radius

def area(radius):
    return radius*radius*3.14

def filewrite(area):
    f = open("22.txt","a")
    area = str(area)
    f.write("\nThe area of the circle is: "+area)
    f.close

if __name__ == '__main__':
    radius = fileread()
    a = area(radius)
    filewrite(a)
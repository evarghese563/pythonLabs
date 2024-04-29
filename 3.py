def area(radius):
    return radius*radius*3.14

def volume(length, area):
    return area * length


# length , radius = input("Enter the length and radius: ")
l = []
l = input("Enter the length and radius: ").split(" ")

length = float(l[1])
radius = float(l[0])
print(length)
print(radius)
a = area(radius)

print(volume(a,length))


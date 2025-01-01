
# Python program to find the area of a triangle whose sides are given

a = 3#float(input("Enter the first side of the triangle: "))
b = 4#float(input("Enter the second side of the triangle: "))
c = 5#float(input("Enter the third side of the triangle: "))

s = (a + b + c) / 2 #semiperimeter calculate

# Calculate the area using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Area of the triangle:", area)

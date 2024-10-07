rectangle1L = float(input("Enter length of rectangle 1: "))
rectangle1W = float(input("Enter width of rectangle 1: "))

rectangle2L = float(input("Enter length of rectangle 2: "))
rectangle2W = float(input("Enter width of rectangle 2: "))

r1 = (rectangle1L * rectangle1W)
r2 = (rectangle2L * rectangle2W)

if r1 > r2:
    print("Rectangle 1 has a larger area than rectangle 2")
elif r2 > r1:
    print("Rectangle 2 has a larger area than rectangle 1")
elif r1 == r2:
    print("Both Rectangle 1 and 2 are equal in area")


def circle_area(radius):
    if radius <= 0:
        print("Invalid input")
        return

    pi = 3.14
    area = pi * radius * radius
    print("Area of circle:", area)

radius = float(input("Enter radius: "))
circle_area(radius)

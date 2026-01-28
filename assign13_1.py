def rectangle_area(length, width):
    if length <= 0 or width <= 0:
        print("Invalid input")
        return

    area = length * width
    print("Area of rectangle:", area)

length = float(input("Enter length: "))
width = float(input("Enter width: "))

rectangle_area(length, width)

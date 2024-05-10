from math import pi


def AreaOfCircle():
    radius = float(input("Enter radius of the circle: "))
    print(f"The Area of Circle: {round(pi * (radius ** 2), 2)}")


def AreaOfTriangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(f"The Area of Triangle: {round((0.5 * base * height), 2)}")


def AreaOfSquare():
    side = float(input("Enter the side of the square: "))
    print(f"The Area of Square: {round((side ** 2), 2)}")


def AreaOfRectangle():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    print(f"The Area of Rectangle: {round((length * breadth), 2)}")
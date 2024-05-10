import Areas


while True:
    choice = int(input("""
 ===> Area Calculator <===

      1. Circle
      2. Triangle
      3. Square
      4. Rectangle
      5. Exit

Enter your choice (1/2/3/4/5): 
    """))
    if choice == 1:
        Areas.AreaOfCircle()
    elif choice == 2:
        Areas.AreaOfTriangle()
    elif choice == 3:
        Areas.AreaOfSquare()
    elif choice == 4:
        Areas.AreaOfRectangle()
    elif choice == 5:
        exit(0)

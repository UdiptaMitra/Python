'''## Problem 3: Area and Volume Calculator Using Switch Case
Write a Python program that calculates the **area or volume** of different geometric shapes based on the user's choice.
The program should use a **switch-case structure** to select the appropriate operation.

Area Formulas
| Shape | Area Formula | Parameters |
|------|--------------|-----------|
| Circle | $A = \pi r^2$ | $r$ = radius |
| Rectangle | $A = l \times b$ | $l$ = length, $b$ = breadth |
| Triangle | $A = \frac{1}{2}bh$ | $b$ = base, $h$ = height |
| Square | $A = a^2$ | $a$ = side |
| Parallelogram | $A = b \times h$ | $b$ = base, $h$ = height |

Volume Formulas
| Shape | Volume Formula | Parameters |
|------|----------------|-----------|
| Cube | $V = a^3$ | $a$ = side |
| Cuboid | $V = l \times b \times h$ | $l$ = length, $b$ = breadth, $h$ = height |
| Sphere | $V = \frac{4}{3}\pi r^3$ | $r$ = radius |
| Cylinder | $V = \pi r^2 h$ | $r$ = radius, $h$ = height |
| Cone | $V = \frac{1}{3}\pi r^2 h$ | $r$ = radius, $h$ = height |

1. Menu Options
Display the following menu and allow the user to choose an option:
Area Calculations
- 1  Area of Circle  
- 2  Area of Rectangle  
- 3  Area of Triangle  
- 4  Area of Square  
- 5  Area of Parallelogram  
Volume Calculations
- 6  Volume of Cube  
- 7  Volume of Cuboid  
- 8  Volume of Sphere  
- 9  Volume of Cylinder  
- 10 Volume of Cone

2. Take the **user's choice as input**.
3. Based on the selected option, ask the user to input the **required parameters** such as radius, length, breadth, height, or side.
4. Use a **switch-case structure** to perform the required calculation.
5. Display the **computed area or volume**.
'''

import math
while True:    
    #1. Menu Options
    print()
    print("Area Calculations")
    print("1 - Area of Circle")
    print("2 - Area of Rectangle")
    print("3 - Area of Triangle")
    print("4 - Area of Square")
    print("5 - Area of Parallelogram")
    print()
    print("Volume Calculations")
    print("6 - Volume of Cube")
    print("7 - Volume of Cuboid")
    print("8 - Volume of Sphere")
    print("9 - Volume of Cylinder")
    print("10 - Volume of Cone")
    print()
    print("0 - Exit the program")
    print()
    #2. user input
    choice = int(input("Enter your choice: "))

    #3. match case as switch case not in python
    match choice:
        #4. display in each of the case blocks
        case 0:
            print()
            print("Exiting the program")
            break
        
        case 1:
            print()
            r = float(input("Enter radius of Circle: "))
            area = math.pi * r**2
            print(f"Area of Circle = {area:.2f}")

        case 2:
            print()
            l = float(input("Enter length of Rectangle: "))
            b = float(input("Enter breadth of Rectangle: "))
            area = l * b
            print(f"Area of Rectangle = {area:.2f}")

        case 3:
            print()
            b = float(input("Enter base of Triangle: "))
            h = float(input("Enter height of Triangle: "))
            area = 0.5 * b * h
            print(f"Area of Triangle = {area:.2f}")

        case 4:
            print()
            a = float(input("Enter side of Square: "))
            area = a**2
            print(f"Area of Square = {area:.2f}")

        case 5:
            print()
            b = float(input("Enter base of Parallelogram: "))
            h = float(input("Enter height of Parallelogram: "))
            area = b * h
            print(f"Area of Parallelogram = {area:.2f}")

        case 6:
            print()
            a = float(input("Enter side of Cube: "))
            volume = a**3
            print(f"Volume of Cube = {volume:.2f}")

        case 7:
            print()
            l = float(input("Enter length of Cuboid: "))
            b = float(input("Enter breadth of Cuboid: "))
            h = float(input("Enter height of Cuboid: "))
            volume = l * b * h
            print(f"Volume of Cuboid = {volume:.2f}")

        case 8:
            print()
            r = float(input("Enter radius of Sphere: "))
            volume = (4/3) * math.pi * r**3
            print(f"Volume of Sphere = {volume:.2f}")

        case 9:
            print()
            r = float(input("Enter radius of Cylinder: "))
            h = float(input("Enter height of Cylinder: "))
            volume = math.pi * r**2 * h
            print(f"Volume of Cylinder = {volume:.2f}")

        case 10:
            print()
            r = float(input("Enter radius of Cone: "))
            h = float(input("Enter height of Cone: "))
            volume = (1/3) * math.pi * r**2 * h
            print(f"Volume of Cone = {volume:.2f}")

        case _:
            print()
            print("Invalid choice! Try again.")
'''
## Problem 7: Triangle Validation and Classification
A triangle is formed by three sides. However, not every set of three numbers can form a valid triangle.  
The **Triangle Inequality Theorem** states that the sum of the lengths of any two sides of a triangle must be **greater than the third side**.
Mathematically,
a + b > c; a + c > b; b + c > a
where \(a\), \(b\), and \(c\) represent the three sides of the triangle.

### Task
Write a Python program that performs the following steps:
1. Take the **three side lengths** of a triangle as input from the user.
2. Check whether the given sides satisfy the **triangle inequality condition**.
3. If the triangle is **not valid**, display an appropriate message.
4. If the triangle is **valid**, determine the type of triangle.

### Triangle Classification
If the triangle is valid, classify it based on the side lengths:
| Triangle Type | Condition |
|---------------|-----------|
| Equilateral Triangle | All three sides are equal |
| Isosceles Triangle | Any two sides are equal |
| Scalene Triangle | All three sides are different |'''

# 1. input
a=float(input("Enter side a: "))
b=float(input("Enter side b: "))
c=float(input("Enter side c: "))

# 2. triangle inequality
if a+b>c and a+c>b and b+c>a:
    # 3. valid triangle
    if a==b==c:
        print("Triangle is Equilateral - All three sides are equal")
    elif a==b or b==c or a==c:
        print("Triangle is Isosceles - Any two sides are equal")
    else:
        print("Triangle is Scalene - All three sides are different")
else: #4. not valid triangle
    print("Not a valid triangle")
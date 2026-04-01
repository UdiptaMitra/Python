'''Problem 1: Arithmetic Operations ( Using Functions )
Write a Python program that performs various arithmetic operations on two numbers entered by the user.
1. Take **two numbers as input from the user**.
2. Perform the following **arithmetic operations**:
   - Addition
   - Subtraction
   - Multiplication
   - Division
3. The program must **handle division by zero gracefully**.If the user attempts to divide by zero, the program should display an appropriate message instead of producing an error.
4. If you are familiar with the concept of **function definition in Python**, implement each operation using **separate functions**.
5. Each function should:
   - Take the necessary inputs as parameters
   - Perform the required operation
   - Return or display the result.'''

#1. input
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))

#2. operations 4. using functions
def addition(num1,num2):
    return num1+num2
def substraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    if num2==0:
        return "Division by zero not possible." #3. div by zero
    return num1/num2

#5. result
print("The result of addition is: ",addition(num1,num2))
print("The result of substraction is: ",substraction(num1,num2))
print("The result of multiplication is: ",multiplication(num1,num2))
print("The result of division is: ",division(num1,num2))
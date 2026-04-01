'''Problem 5: Swap Two Numbers Without Temporary Variable
Write a program to swap two numbers **without using a third variable** using XOR.'''

num1=int(input("enter a number: "))
num2=int(input("enter another number: "))
print("original numbers: num1 =", num1, "num2 =", num2)
def swap_xor(num1,num2):
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2
    print("After swapwith xor: num1 =", num1, "num2 =", num2)
swap_xor(num1,num2)
def swap_no_xor(num1,num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print("After swap without xor: num1 =", num1, "num2 =", num2)
swap_no_xor(num1,num2)

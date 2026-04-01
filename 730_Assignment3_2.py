'''Write a recursive function to find the GCD of two numbers using the Euclidean algorithm'''
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
def gcd(num1,num2):
    rem=num1%num2
    if rem==0:
        return num2
    return gcd(num2, rem)
print("The GCD is: ", gcd(num1,num2))

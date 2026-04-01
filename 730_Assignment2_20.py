'''Write a Python program to implement a generator function to generate Fibonacci numbers up to N'''

'''A generator in Python is a special type of function or expression that creates an iterator to produce 
a sequence of values one at a time, on demand (lazy evaluation), without storing the entire sequence in memory.
yeild -  acts like multiple return statements'''

def fibonacci(n):
    a=0
    b=1
    c=1
    yield a
    while c<=n:
        yield c
        c=a+b
        a=b
        b=c
n=int(input("Enter the limiting value n: "))
output=fibonacci(n)
for item in output:
    print(item)
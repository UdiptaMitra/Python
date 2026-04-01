#head rec
def factorial(n):
    if n==0:
        return 1
    else:
        fn1=factorial(n-1)
        fact=n*fn1
        return fact
print(factorial(6))

#tail rec
def natural(n):
    if n==0:
        print(0)
        return 
    else:
        print(n)
        natural(n-1)
natural(6)
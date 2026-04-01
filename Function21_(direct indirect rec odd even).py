n=int(input("enter a number to check odd or even: "))


#direct recursion
def odd_even(n,rem=0):
    if n==1:
        print("Odd")
        return 1
    elif n==0:
        print("even")
        return 0
    else:
        n=n-2
        return odd_even(n,rem)
odd_even(n)


#indirect recursion
def is_even(n):
    if n==0:
        return True
    return is_odd(n-1)

def is_odd(n):
    if n==0:
        return False
    return is_even(n-1)

res=is_even(n)
if res==True:
    print("even")
else:
    print("odd")

res=is_odd(n)
if res==False:
    print("even")
else:
    print("odd")
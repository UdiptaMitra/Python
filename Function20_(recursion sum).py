string=""
def sum(n,string):
    if n==0:
        string=string+("0=")
        print(string,end="")
        return 0
    else:
        string=string+(str(n)+"+")
        return n+sum(n-1,string)
    
print(sum(5,string))

n=int(input("Enter the value of n:" ))
#n iws a constant here whenever we call
def sum(n,i=1):
    if i==n:
        print(i,end="=")
        return n
    else:
        print(i,end="+")
        return i+sum(n,i+1)
print(sum(n))


def rec_sum(n,current=1):
    #base case
    if current==n:
        print (n,end="=")
        return n
    #print the current value and add a "+" sign
    print(current,end="+")
    #recursive step: add current to the sum of rest
    return current+rec_sum(n,current+1)
total=rec_sum(n)
print(total)
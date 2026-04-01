i=1
while(i<=10):
    print(i)
    i=i+1

while():
    print(i)
    if i==10:
        break
    i+=1

def natural(n):
    if n==10:
        print(10)
        return
    else:
        print(n)
        return natural(n+1)
        
print(natural(1))


def rec(value):
    if value>=10:
        print(f"I am stopping the iteration {value}")
    else:
        print("I am at iteration {}".format(value))
        value+=1
        print("Changed value to {}".format(value))
        print("**********************")
        rec(value)
rec(1)

